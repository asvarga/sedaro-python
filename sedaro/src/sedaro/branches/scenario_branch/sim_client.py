from concurrent.futures import ThreadPoolExecutor
import dask.dataframe
import json
import msgpack
import os
import pathlib
import requests
import shutil
import time
from contextlib import contextmanager
from typing import (TYPE_CHECKING, Any, Generator, List, Optional, Tuple,
                    Union)
import uuid6

import numpy as np
from sedaro.results.simulation_result import SimulationResult
from sedaro_base_client.apis.tags import externals_api, jobs_api
from sedaro.branches.scenario_branch.download import ArchiveProgressBar, DownloadWorker, ProgressBar
from ...exceptions import (NoSimResultsError, SedaroApiException,
                           SimInitializationError)
from ...settings import COMMON_API_KWARGS
from ...utils import body_from_res, parse_urllib_response, progress_bar

if TYPE_CHECKING:
    from ...branches import ScenarioBranch
    from ...sedaro_api_client import SedaroApiClient


def serdes(v):
    if type(v) is dict and 'ndarray' in v:
        return np.array(v['ndarray'])
    if type(v) is np.ndarray:
        return {'ndarray': v.tolist()}
    if type(v) is dict:
        return {k: serdes(v) for k, v in v.items()}
    if type(v) in {list, tuple}:
        return [serdes(v) for v in v]
    return v

def concat_stream_data(main, other, len_main, len_other):
    assert type(main) == dict and type(other) == dict
    for k in other:
        if k not in main:
            main[k] = [None for _ in range(len_main)]
        main[k].extend(other[k])
    for k in main:
        if k not in other:
            main[k].extend([None for _ in range(len_other)])

def concat_stream(main, other, stream_id):
    len_main = len(main[0])
    len_other = len(other[0])
    main[0].extend(other[0])
    stream_id_short = stream_id.split('/')[0]
    concat_stream_data(main[1][stream_id_short], other[1][stream_id_short], len_main, len_other)

def concat_results(main, other):
    for stream in other:
        if stream not in main:
            main[stream] = other[stream]
        else: # concat stream parts
            concat_stream(main[stream], other[stream], stream)

def update_metadata(main, other):
    for k in other['counts']:
        if k not in main['counts']:
            main['counts'][k] = 0
        main['counts'][k] += other['counts'][k]

def set_numeric_as_list(d):
    if isinstance(d, dict):
        if all(key.isdigit() for key in d.keys()):  # Check if all keys are array indexes in string form
            return [set_numeric_as_list(d[key]) for key in sorted(d.keys(), key=int)]
        else:
            return {k: set_numeric_as_list(v) for k, v in d.items()}
    return d

def __set_nested(results):
    nested = {}
    for k in sorted(list(results.keys())):
        v = results[k]
        try:
            ptr = nested
            tokens = k.split('.')
            for token in tokens[:-1]:
                if token not in ptr:
                    ptr[token] = {}
                ptr = ptr[token]
            ptr[tokens[-1]] = v
        except TypeError:
            ptr = nested
            for token in tokens[:-1]:
                if type(ptr[token]) == list:
                    del ptr[token]
                    break
                else:
                    ptr = ptr[token]
            ptr = nested
            for token in tokens[:-1]:
                if token not in ptr:
                    ptr[token] = {}
                ptr = ptr[token]
            ptr[tokens[-1]] = v
    return nested

# TODO: edge case where one page has all nones for a SV, then the next page has a bunch of vectors for it
def set_nested(results):
    nested = {}
    for k in results:
        kspl = k.split('/')[0]
        nested[k] = (results[k][0], {kspl: set_numeric_as_list(__set_nested(results[k][1][kspl]))})
    return nested

class FastFetcherResponse:
    def __init__(self, response: requests.Response):
        if response.headers['Content-Type'] == 'application/json':
            self.type = 'application/json'
            self.data = response.text
        elif response.headers['Content-Type'] == 'application/msgpack':
            self.type = 'application/msgpack'
            self.data = response.content
        else:
            raise Exception("Unexpected MIME type")
        self.status = response.status_code
        self.response = response

    def __getattr__(self, key):
        return self.response[key]

    def parse(self):
        if self.type == 'application/json':
            return parse_urllib_response(self)
        elif self.type == 'application/msgpack':
            return msgpack.unpackb(self.data)
        else:
            raise Exception("Unexpected MIME type")

class FastFetcher:
    """Accelerated request handler for data page fetching."""
    def __init__(self, api_key, host):
        self.headers = {
            'X_API_KEY': api_key,
            'User-Agent': 'OpenAPI-Generator/1.0.0/python',
            'Content-Type': 'application/json',
        }
        self.host = host

    def get(self, url):
        return FastFetcherResponse(requests.get(url=self.host + url, headers=self.headers))

class Simulation:
    """A client to interact with the Sedaro API simulation (jobs) routes"""

    def __init__(self, sedaro: 'SedaroApiClient', branch: 'ScenarioBranch'):
        """Instantiate a Sedaro `Simulation` instance

        Args:
            sedaro (`SedaroApiClient`): the `SedaroApiClient`
            branch_id (`int`): id of the desired Sedaro Scenario Branch to interact with its simulations (jobs).
        """
        self.__branch = branch
        self.__branch_id = branch.id
        self.__sedaro = sedaro

    @contextmanager
    def __jobs_client(self) -> Generator['jobs_api.JobsApi', Any, None]:
        with self.__sedaro.api_client() as api:
            yield jobs_api.JobsApi(api)

    @contextmanager
    def externals_client(self) -> Generator['externals_api.ExternalsApi', Any, None]:
        with self.__sedaro.api_client() as api:
            yield externals_api.ExternalsApi(api)

    def start(self, wait=False, timeout=None) -> 'SimulationHandle':
        """Starts simulation corresponding to the respective Sedaro Scenario Branch id.

        Args:
            wait (bool, optional): Triggers waiting for simulation to deploy and transition to `RUNNING` before returning. Defaults to `False`.
            timeout (int, optional): Seconds to wait for simulation to deploy and transition to `RUNNING` before raising an error. Defaults to `None`.

        Returns:
            SimulationHandle
        """
        with self.__jobs_client() as jobs:
            res = jobs.start_simulation(
                path_params={'branchId': self.__branch_id},
                **COMMON_API_KWARGS
            )
        handle = SimulationHandle(body_from_res(res), self)
        if not wait:
            return handle

        t = 0
        while t < (timeout or float('inf')):
            if (handle := handle.status())['status'] in {'PENDING', 'QUEUED'}:
                time.sleep(0.1)
                t += 0.1
            elif handle['status'] in {'FAILED', 'ERROR'}:
                raise SimInitializationError(handle['message'])
            else:
                return handle
        raise TimeoutError(f'Simulation did not deploy before timeout of {timeout}.')

    def status(self, job_id: str = None, *, err_if_empty: bool = True) -> 'SimulationHandle':
        """Gets the latest simulation corresponding to the respective Sedaro Scenario Branch id. This can return a
        response even before the simulation is done.

        Args:
            job_id (str, optional): triggers getting the simulation job assocciated with the `id` rather than the\
                default latest.
            err_if_empty (bool, optional): Triggers raising an error if no simulation results and `err_if_empty`.\
                Defaults to `True`.

        Raises:
            NoSimResultsError: if no simulation has been started and `err_if_empty` set to `True`

        Returns:
            SimulationHandle
        """
        if job_id is None:
            with self.__jobs_client() as jobs:
                res = jobs.get_simulations(
                    path_params={'branchId': self.__branch_id},
                    query_params={'latest': ''},
                    **COMMON_API_KWARGS
                )
            if len(body := body_from_res(res)):
                return SimulationHandle(body[0], self)
            if err_if_empty:
                raise NoSimResultsError(
                    status=404,
                    reason=f'Could not find any simulations for scenario: {self.__branch_id}'
                )
            return SimulationHandle(None, self)

        else:
            with self.__jobs_client() as jobs:
                res = jobs.get_simulation(
                    path_params={
                        'branchId': self.__branch_id,
                        'jobId': job_id
                    },
                    **COMMON_API_KWARGS
                )
                return SimulationHandle(body_from_res(res), self)

    def terminate(self, job_id: int = None) -> None:
        """Terminate latest running simulation job corresponding to the respective Sedaro Scenario Branch id. If a
        `job_id` is provided, that simulation job will be terminated rather than the latest.

        Args:
            job_id (`int`, optional): id of the simulation (job) to terminate.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            SimulationHandle
        """
        if job_id is None:
            job_id = self.status()['id']

        with self.__jobs_client() as jobs:
            jobs.terminate_simulation(
                path_params={
                    'branchId': self.__branch_id,
                    'jobId': job_id
                },
                **COMMON_API_KWARGS
            )

    def __fetch(
        self,
        *,
        id: str = None,
        start: float = None,
        stop: float = None,
        binWidth: float = None,
        limit: float = None,
        streams: Optional[List[Tuple[str, ...]]] = None,
        sampleRate: int = None,
        continuationToken: str = None,
        download_manager: DownloadWorker = None,
    ):
        if sampleRate is None and continuationToken is None:
            sampleRate = 1

        with self.__sedaro.api_client() as api:
            fast_fetcher = FastFetcher(self.__sedaro._api_key, api.configuration.host)

        if id == None:
            id = self.status()['dataArray']
        url = f'/data/{id}?'
        if start is not None:
            url += f'&start={start}'
        if stop is not None:
            url += f'&stop={stop}'
        if binWidth is not None:
            print("WARNING: the parameter `binWidth` is deprecated and will be removed in a future release.")
            url += f'&binWidth={binWidth}'
        elif limit is not None:
            print("WARNING: the parameter `limit` is deprecated and will be removed in a future release.")
            url += f'&limit={limit}'
        streams = streams or []
        if len(streams) > 0:
            encodedStreams = ','.join(['.'.join(x) for x in streams])
            url += f'&streams={encodedStreams}'
        url += f'&axisOrder=TIME_MINOR'
        if sampleRate is not None:
            url += f'&sampleRate={sampleRate}'
        if continuationToken is not None:
            url += f'&continuationToken={continuationToken}'
        url += '&encoding=msgpack'

        response = fast_fetcher.get(url)
        _response = None
        has_nonempty_ctoken = False
        try:
            _response = response.parse()
            if 'version' in _response['meta'] and _response['meta']['version'] == 3:
                is_v3 = True
                download_manager.ingest(_response['series'])
                if 'continuationToken' in _response['meta'] and _response['meta']['continuationToken'] is not None:
                    has_nonempty_ctoken = True
                    ctoken = _response['meta']['continuationToken']
            else:
                is_v3 = False
            if response.status != 200:
                raise Exception()
        except:
            reason = _response['error']['message'] if _response and 'error' in _response else 'An unknown error occurred.'
            raise SedaroApiException(status=response.status, reason=reason)
        if is_v3: # keep fetching pages until we get an empty continuation token
            if has_nonempty_ctoken: # need to fetch more pages
                result = _response
                while has_nonempty_ctoken:
                    # fetch page
                    request_url = f'/data/{id}?&continuationToken={ctoken}'
                    page = fast_fetcher.get(request_url)
                    _page = page.parse()
                    download_manager.ingest(_page['series'])
                    try:
                        if 'continuationToken' in _page['meta'] and _page['meta']['continuationToken'] is not None:
                            has_nonempty_ctoken = True
                            ctoken = _page['meta']['continuationToken']
                        else:
                            has_nonempty_ctoken = False
                        if page.status != 200:
                            raise Exception()
                    except Exception:
                        reason = _page['error']['message'] if _page and 'error' in _page else 'An unknown error occurred.'
                        raise SedaroApiException(status=page.status, reason=reason)
                    concat_results(result['series'], _page['series'])
                    update_metadata(result['meta'], _page['meta'])
                _response = result
        download_manager.finalize()

    def __get_filtered_streams(self, requested_streams: list, metadata: dict):
        streams_raw = metadata['streams']
        streams_true = {}
        for stream in streams_raw:
            assert len(stream) == 2
            if stream[0] not in streams_true:
                streams_true[stream[0]] = []
            streams_true[stream[0]].append(stream[1])
        filtered_streams = []
        for stream in requested_streams:
            if stream[0] in streams_true:
                if len(stream) == 1:
                    for v in streams_true[stream[0]]:
                        filtered_streams.append((stream[0], v))
                else:
                    if stream[0] in streams_true:
                        if stream[1] in streams_true[stream[0]]:
                            filtered_streams.append(stream[0], stream[1])
        return filtered_streams

    def __downloadInParallel(self, sim_id, streams, params, download_manager):
        start = params['start']
        stop = params['stop']
        sampleRate = params['sampleRate']
        streams_fmt = [tuple(stream.split('.')) for stream in streams]
        self.__fetch(id=sim_id, streams=streams_fmt, sampleRate=sampleRate, start=start, stop=stop, download_manager=download_manager)

    def __results(self,
                job_id: str = None,
                start: float = None,
                stop: float = None,
                streams: Optional[List[Tuple[str, ...]]] = None,
                sampleRate: int = None,
                num_workers: int = 2) -> "dict[str, dask.dataframe]":

        metadata = self.__get_metadata(sim_id := job_id['dataArray'])
        filtered_streams = self.__get_filtered_streams(streams, metadata)
        num_workers = min(num_workers, len(filtered_streams))
        workers = [[] for _ in range(num_workers)]
        for i, stream in enumerate(streams):
            workers[i % num_workers].append(stream)

        download_bar = ProgressBar(metadata['start'], metadata['stop'], len(metadata['streams']), "Downloading...")
        download_managers = [DownloadWorker(download_bar) for _ in range(num_workers)]
        params = {'start': start, 'stop': stop, 'sampleRate': sampleRate}
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            executor.map(self.__downloadInParallel, [sim_id] * num_workers, workers, [params] * num_workers, download_managers)
            executor.shutdown(wait=True)
        download_bar.complete()

        stream_results = {}

    def results(self,
                job_id: str = None,
                start: float = None,
                stop: float = None,
                streams: Optional[List[Tuple[str, ...]]] = None,
                sampleRate: int = None,
                num_workers: int = 2) -> SimulationResult:
        """Query latest scenario result. If a `job_id` is passed, query for corresponding sim results rather than
        latest.

        If no argument is provided for `streams`, all data will be fetched. If you pass an argument to `streams`, it
        must be a list of tuples following particular rules:

        - Each tuple in the list can contain either 1 or 2 items.
        - If a tuple contains 1 item, that item must be the agent ID, as a string. Data for all engines of this agent\
            will be fetched. Remember that a 1-item tuple is written like `(foo,)`, NOT like `(foo)`.
        - If a tuple contains 2 items, the first item must be the same as above. The second item must be one of the\
            following strings, specifying an engine: `'GNC`, `'CDH'`, `'Thermal'`, `'Power'`. Data for the specified\
            agent of this engine will be fetched.

        For example, with the following code, `results` will only contain data for all engines of agent `foo` and the
        `Power` and `Thermal` engines of agent `bar`.

        ```py
        selected_streams=[
            ('foo',),
            ('bar', 'Thermal'),
            ('bar', 'Power')
        ]
        results = sim.results(streams=selected_streams)
        ```

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.
            streams (Optional[List[Tuple[str, ...]]], optional): Streams to query for. Defaults to `None`.

        Raises:
            NoSimResultsError: if no simulation has been started.
            SedaroApiException: if no simulation has completed.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        '''Query latest scenario result.'''
        job = self.status(job_id)
        # data = self.results_plain(id=job['dataArray'], start=start, stop=stop, streams=streams or [], sampleRate=sampleRate, num_workers=num_workers)
        data = NotImplemented
        return SimulationResult(job, data)

    def results_poll(
        self,
        job_id: str = None,
        streams: List[Tuple[str, ...]] = None,
        sampleRate: int = None,
        retry_interval: int = 2,
    ) -> SimulationResult:
        """Query latest scenario result and wait for sim to finish if it's running. If a `job_id` is passed, query for
        corresponding sim results rather than latest. See `results` method for details on using the `streams` kwarg.

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.
            streams (List[Tuple[str, ...]], optional): Streams to query for. Defaults to `None`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        job = self.status(job_id)
        options = {'QUEUED', 'PENDING', 'RUNNING'}

        while job['status'] in options:
            if job['status'] == 'QUEUED':
                print('Simulation is queued...', end='\r')
            if job['status'] == 'PENDING':
                print('Simulation is building...', end='\r')
            else:
                progress_bar(job['progress']['percentComplete'])
            job = self.status()
            time.sleep(retry_interval)

        return self.results(streams=streams or [], sampleRate=sampleRate)

    def __get_metadata(self, sim_id: str = None):
        request_url = f'/data/{sim_id}/metadata?'
        with self.__sedaro.api_client() as api:
            response = api.call_api(request_url, 'GET', headers={'Content-Type': 'application/json'})
        response_dict = json.loads(response.data)
        return response_dict

    def download(
        self,
        simulation_id: str = None,
        filename: str = None,
        streams: List[str] = None,
        num_workers: int = 2,
        overwrite: bool = False
    ):

        if filename is None:
            raise ValueError('No filename provided. Please provide a filename via the `filename` argument.')

        if not overwrite and pathlib.Path(filename).exists():
            raise FileExistsError(
                f'The file {filename} already exists. Please delete it or provide a different filename via the `filename` argument.')

        job_id = self.status(simulation_id)
        metadata = self.__get_metadata(sim_id := job_id['dataArray'])
        if streams is not None:
            metadata['streams'] = streams
        os.mkdir(tmpdir := f".{uuid6.uuid7()}")

        success = False
        try:
            workers = [[] for _ in range(num_workers)]
            for i, stream in enumerate(metadata['streams']):
                workers[i % num_workers].append(stream)
            download_bar = ProgressBar(metadata['start'], metadata['stop'], len(metadata['streams']), "Downloading...")
            archive_bar = ArchiveProgressBar(len(metadata['streams']))

            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                executor.map(self.__downloadInParallel,
                            [sim_id] * num_workers,
                            workers,
                            [tmpdir] * num_workers,
                            [filename] * num_workers,
                            [download_bar] * num_workers,
                            [archive_bar] * num_workers)
                executor.shutdown(wait=True)
            download_bar.complete()
            archive_bar.complete()

            print("Building zip file...")
            shutil.make_archive(tmpzip := f"{uuid6.uuid7()}", 'zip', tmpdir)
            curr_zip_base = ''
            # if the path is to another directory, make that directory if nonexistent, and move the zip there
            if len(path_split := filename.split('/')) > 1:
                path_dirs = '/'.join(path_split[:-1])
                pathlib.Path(path_dirs).mkdir(parents=True, exist_ok=True)
                shutil.move(f"{tmpzip}.zip", f"{(curr_zip_base := path_dirs)}/{tmpzip}.zip")
                zip_desired_name = path_split[-1]
            else:
                zip_desired_name = filename
            # rename zip to specified name
            if len(curr_zip_base) > 0:
                zip_new_path = f"{curr_zip_base}/{zip_desired_name}"
                curr_zip_name = f"{curr_zip_base}/{tmpzip}"
            else:
                zip_new_path = zip_desired_name
                curr_zip_name = tmpzip
            os.rename(f"{curr_zip_name}.zip", zip_new_path)
            # remove tmpdir
            os.system(f"rm -r {tmpdir}")
            success = True
            print(f"Successfully archived at {zip_new_path}")
        except Exception as e:
            raise e
        finally: # remove tmpdir even if an error occurs
            if not success:
                os.system(f"rm -r {tmpdir}")

class SimulationJob:
    def __init__(self, job: Union[dict, None]): self.__job = job
    def get(self, key, default=None): return self.__job.get(key, default)

    def __getitem__(self, key):
        if self.__job:
            if key in self.__job:
                return self.__job[key]
            else:
                raise KeyError(
                    f'Key {key} not found in SimulationJob object. Available values are: {self.__job.keys()}')
        else:
            raise Exception(
                'No simulation is running. It was either terminated or one was never started.')


class SimulationHandle:

    def __init__(self, job: Union[dict, None], sim_client: Simulation):
        self.__job = SimulationJob(job)
        self.__sim_client = sim_client

    def __getitem__(self, key): return self.__job[key]
    def get(self, key, default=None): return self.__job.get(key, default)

    def status(self, err_if_empty: bool = True):
        """Refreshes the local simulation status.

        Args:
            err_if_empty (bool, optional): Triggers raising an error if no simulation results and `err_if_empty`.\
                Defaults to `True`.

        Raises:
            NoSimResultsError: if no simulation has been started and `err_if_empty` set to `True`

        Returns:
            SimulationHandle (self)
        """
        return (self := self.__sim_client.status(self.__job['id'], err_if_empty=err_if_empty))

    def terminate(self):
        """Terminate the running simulation.

        Returns:
            SimulationHandle (self)
        """
        self.__sim_client.terminate(self.__job['id'])
        return self

    def results(self, streams: Optional[List[Tuple[str, ...]]] = None) -> SimulationResult:
        """Query simulaiton results.

        If no argument is provided for `streams`, all data will be fetched. If you pass an argument to `streams`, it
        must be a list of tuples following particular rules:

        - Each tuple in the list can contain either 1 or 2 items.
        - If a tuple contains 1 item, that item must be the agent ID, as a string. Data for all engines of this agent\
            will be fetched. Remember that a 1-item tuple is written like `(foo,)`, NOT like `(foo)`.
        - If a tuple contains 2 items, the first item must be the same as above. The second item must be one of the\
            following strings, specifying an engine: `'GNC`, `'CDH'`, `'Thermal'`, `'Power'`. Data for the specified\
            agent of this engine will be fetched.

        For example, with the following code, `results` will only contain data for all engines of agent `foo` and the
        `Power` and `Thermal` engines of agent `bar`.

        ```py
        selected_streams=[
            ('foo',),
            ('bar', 'Thermal'),
            ('bar', 'Power')
        ]
        results = sim.results(streams=selected_streams)
        ```

        Args:
            streams (Optional[List[Tuple[str, ...]]], optional): Streams to query for. Defaults to `None`.

        Raises:
            NoSimResultsError: if no simulation has been started.
            SedaroApiException: if no simulation has completed.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        return self.__sim_client.results(job_id=self.__job['id'], streams=streams)

    def results_poll(
        self,
        streams: List[Tuple[str, ...]] = None,
        retry_interval: int = 2
    ) -> SimulationResult:
        """Query simulation results but wait for sim to finish if it's running. See `results` method for details on using the `streams` kwarg.

        Args:
            streams (List[Tuple[str, ...]], optional): Streams to query for. Defaults to `None`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        return self.__sim_client.results_poll(
            job_id=self.__job['id'],
            streams=streams,
            retry_interval=retry_interval
        )

    def download(
        self,
        streams: List[Tuple[str, ...]] = None,
        filename: str = None,
        workers: int = 2,
        overwrite: bool = False
    ):
        return self.__sim_client.download(self.__job['id'], filename=filename, workers=workers, streams=streams, overwrite=overwrite)

    def consume(self, agent_id: str, external_state_id: str, time: float = None):
        with self.__sim_client.externals_client() as externals_client:
            response = externals_client.get_external(
                path_params={
                    'jobId': self.__job['id'],
                    'agentId': agent_id,
                    'externalStateBlockId': external_state_id,
                },
                query_params=({'time': time} if time is not None else {}),
                **COMMON_API_KWARGS,
            )
        return tuple(serdes(v) for v in body_from_res(response))

    def produce(self, agent_id: str, external_state_id: str, values: tuple, timestamp: float = None):
        if type(values) is not tuple:
            raise TypeError(
                '`values` must be passed as a tuple of one or more state variable values (ex. `([x, y, z],)` where `[x, y, z]` is the external state]).')
        with self.__sim_client.externals_client() as externals_client:
            response = externals_client.put_external(
                path_params={
                    'jobId': self.__job['id'],
                    'agentId': agent_id,
                    'externalStateBlockId': external_state_id,
                },
                body=({
                    **{'values': [serdes(v) for v in values]},
                    **({'timestamp': timestamp} if timestamp is not None else {})
                }),
                **COMMON_API_KWARGS,
            )
        return tuple(serdes(v) for v in body_from_res(response))
