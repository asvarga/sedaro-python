import time
from contextlib import contextmanager
from typing import (TYPE_CHECKING, Any, Dict, Generator, List, Optional, Tuple,
                    Union)
import concurrent.futures
import json
import math
import os
import pathlib
import tempfile
from threading import Lock
import traceback
from typing import Dict, List, Optional, Tuple
from zipfile import ZipFile, ZIP_DEFLATED

import numpy as np
from sedaro_base_client.apis.tags import externals_api, jobs_api

from ...exceptions import NoSimResultsError, SedaroApiException
from ...results import SimulationResult
from ...settings import COMMON_API_KWARGS
from ...utils import body_from_res, parse_urllib_response, progress_bar

if TYPE_CHECKING:
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

mutex = Lock() TODODODODODODODODODODO

class Simulation:
    """A client to interact with the Sedaro API simulation (jobs) routes"""

    def __init__(self, sedaro: 'SedaroApiClient', branch_id: int):
        """Instantiate a Sedaro `Simulation` instance

        Args:
            sedaro (`SedaroApiClient`): the `SedaroApiClient`
            branch_id (`int`): id of the desired Sedaro Scenario Branch to interact with its simulations (jobs).
        """
        self.__branch_id = branch_id
        self.__sedaro = sedaro

    @contextmanager
    def __jobs_client(self) -> Generator['jobs_api.JobsApi', Any, None]:
        with self.__sedaro.api_client() as api:
            yield jobs_api.JobsApi(api)

    @contextmanager
    def externals_client(self) -> Generator['externals_api.ExternalsApi', Any, None]:
        with self.__sedaro.api_client() as api:
            yield externals_api.ExternalsApi(api)

    def start(self) -> 'SimulationHandle':
        """Starts simulation corresponding to the respective Sedaro Scenario Branch id.

        Returns:
            SimulationHandle
        """
        with self.__jobs_client() as jobs:
            res = jobs.start_simulation(
                path_params={'branchId': self.__branch_id},
                **COMMON_API_KWARGS
            )
        return SimulationHandle(body_from_res(res), self)

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

    def results_plain(
        self,
        *,
        id: str = None,
        start: float = None,
        stop: float = None,
        binWidth: float = None,
        limit: float = None,
        axisOrder: str = None,
        streams: Optional[List[Tuple[str, ...]]] = None
    ):
        """Query latest scenario and return results as a plain dictionary from the Data Service with options to
        customize the response. If an `id` is passed, query for corresponding result rather than latest.

        Args:
            id (str, optional): `id` of the data array to fetch (found on `dataArray` attribute on a response from the\
                `status` or `start` methods)

            start (float, optional): the start time of the data to fetch, in MJD format. Defaults to the start of the\
                simulation.

            stop (float, optional): the end time of the data to fetch, in MJD format. Defaults to the end of the\
                simulation.

            limit (int, optional): the maximum number of points in time for which to fetch data for any stream. If not
                specified, there is no limit and data is fetched at full resolution. If a limit is specified, the\
                duration of the time from `start` to `stop` is divided into the specified number of bins of equal\
                duration, and data is selected from at most one point in time within each bin. Not that it is not\
                guaranteed that you will receive exactly as many points in time as the limit you specify; you may\
                receive fewer, depending on the length of a data stream and/or the distribution of data point timestamps\
                through the simulation.

            binWidth (float, optional): the width of the bins used in downsampling data, as described for `limit`. Note\
                that `binWidth` and `limit` are not meant to be used together; undefined behavior may occur. If you\
                would like to downsample data, use either `limit` or `binWidth`, but not both.

            streams (list, optional): specify which data streams you would like to fetch data for, according to the\
                format described in the previous section. If no list is provided, data is fetched for all streams.

            axisOrder (enum, optional): the shape of each series in the response. Options: `'TIME_MAJOR'` and\
                `'TIME_MINOR'`. Default value, if not specified, is `'TIME_MAJOR'`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            dict: response from the `get` request
        """
        if id == None:
            id = self.status()['dataArray']
        url = f'/data/{id}?'
        if start is not None:
            url += f'&start={start}'
        if stop is not None:
            url += f'&stop={stop}'
        if binWidth is not None:
            url += f'&binWidth={binWidth}'
        elif limit is not None:
            url += f'&limit={limit}'
        streams = streams or []
        if len(streams) > 0:
            encodedStreams = ','.join(['.'.join(x) for x in streams])
            url += f'&streams={encodedStreams}'
        if axisOrder is not None:
            if axisOrder not in {'TIME_MAJOR',  'TIME_MINOR'}:
                raise ValueError(
                    'axisOrder must be either "TIME_MAJOR" or "TIME_MINOR"')
            url += f'&axisOrder={axisOrder}'
        with self.__sedaro.api_client() as api:
            response = api.call_api(url, 'GET')
        _response = None
        try:
            _response = parse_urllib_response(response)
            if response.status != 200:
                raise Exception()
        except:
            reason = _response['error']['message'] if _response and 'error' in _response else 'An unknown error occurred.'
            raise SedaroApiException(status=response.status, reason=reason)
        return _response

    def results(self, job_id: str = None, streams: Optional[List[Tuple[str, ...]]] = None) -> SimulationResult:
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
        data = self.results_plain(id=job['dataArray'], streams=streams or [])
        return SimulationResult(job, data)

    def results_poll(
        self,
        job_id: str = None,
        streams: List[Tuple[str, ...]] = None,
        retry_interval: int = 2
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
        options = {'PENDING', 'RUNNING'}

        while job['status'] in options:
            progress_bar(job['progress']['percentComplete'])
            job = self.status()
            time.sleep(retry_interval)

        return self.results(streams=streams or [])
    
    def build_progress_bar(self, progress):
        fullBlock = '█'
        partialBlocks = [' ', '▎', '▍', '▌', '▋', '▊', '▉', '█']

        percentage = (float(progress['count'] / progress['total'])) * 100.0

        blocks = ''
        for i in range(25):
            if percentage >= (i + 1) * 4:
                blocks += fullBlock
            elif percentage <= i * 4:
                blocks += ' '
            else:
                remainder = (percentage - (i * 4)) * 2.0
                try:
                    blocks += partialBlocks[math.floor(remainder) - 1]
                except Exception: # float imprecision caused remainder value slightly > 8
                    blocks += partialBlocks[-1]

        progressBar = f"Progress: {blocks}|  {percentage:.2f}%  "
        print(progressBar, end='\r')

    def download_data_in_parallel(self, agents, id, dirname: str, progress):
        MAX_ATTEMPTS = 3
        for agent in agents:
            attempts = MAX_ATTEMPTS
            while attempts > 0:
                agentData = self.get_data(id, limit=None, streams=[(agent,)])
                if 'series' in agentData:
                    break
                else:
                    attempts -= 1
            if attempts == 0:
                raise f"Data retrieval for agent {agent} failed after {MAX_ATTEMPTS} attempts"
            with open(f'{dirname}/{agent}.json', 'w') as fd:
                mutex.acquire()
                try:
                    progress['count'] += 1
                    self.build_progress_bar(progress)
                finally:
                    mutex.release()
                json.dump(agentData, fd)
        return agents

    def download_data(self, branch, id, filename: str):
        # check if filename already exists
        if pathlib.Path(filename).exists():
            raise FileExistsError('Provided file name is already in use. Please try again with a different file name.')

        # create temp directory in which to build zip
        archive = ZipFile(filename, 'w')
        with tempfile.TemporaryDirectory() as dirname:
            try:
                # get list of agents
                agents = []
                for agent in branch.Agent.get_all():
                    agents.append(agent.id)
                
                # get data for one agent at a time
                MAX_CHUNKS = 4
                if len(agents) < MAX_CHUNKS:
                    NUM_CHUNKS = len(agents)
                else:
                    NUM_CHUNKS = MAX_CHUNKS
                chunks = []
                for _ in range(NUM_CHUNKS):
                    chunks.append([])
                for i in range(len(agents)):
                    chunks[i % NUM_CHUNKS].append(agents[i])
                progress = {'count': 0, 'total': len(agents)}

                with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_CHUNKS) as executor:
                    _id = [id] * NUM_CHUNKS
                    _dirname = [dirname] * NUM_CHUNKS
                    _progress = [progress] * NUM_CHUNKS
                    done = executor.map(self.download_data_in_parallel, chunks, _id, _dirname, _progress)
                for chunk in done:
                    for agent in chunk:
                        archive.write(f'{dirname}/{agent}.json', f'{agent}.json', ZIP_DEFLATED)
                
                # save zip file
                archive.close()
                print(f'\nZip file created: {filename}')
            
            except Exception:
                try:
                    archive.close()
                except Exception:
                    pass
                if pathlib.Path(filename).exists():
                    os.remove(filename)
                print(traceback.format_exc())
                print("Error: Unable to download data and build archive.")
                return


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
        return self := self.__sim_client.status(self.__job['id'], err_if_empty=err_if_empty)

    def terminate(self):
        """Terminate the running simulation.

        Returns:
            SimulationHandle (self)
        """
        self.__sim_client.terminate(self.__job['id'])
        return self

    def results_plain(
        self,
        start: float = None,
        stop: float = None,
        binWidth: float = None,
        limit: float = None,
        axisOrder: str = None,
        streams: Optional[List[Tuple[str, ...]]] = None
    ):
        """Query simulation results as a plain dictionary from the Data Service with options to
        customize the response.

        Args:
            start (float, optional): the start time of the data to fetch, in MJD format. Defaults to the start of the\
                simulation.

            stop (float, optional): the end time of the data to fetch, in MJD format. Defaults to the end of the\
                simulation.

            limit (int, optional): the maximum number of points in time for which to fetch data for any stream. If not
                specified, there is no limit and data is fetched at full resolution. If a limit is specified, the\
                duration of the time from `start` to `stop` is divided into the specified number of bins of equal\
                duration, and data is selected from at most one point in time within each bin. Not that it is not\
                guaranteed that you will receive exactly as many points in time as the limit you specify; you may\
                receive fewer, depending on the length of a data stream and/or the distribution of data point timestamps\
                through the simulation.

            binWidth (float, optional): the width of the bins used in downsampling data, as described for `limit`. Note\
                that `binWidth` and `limit` are not meant to be used together; undefined behavior may occur. If you\
                would like to downsample data, use either `limit` or `binWidth`, but not both.

            streams (list, optional): specify which data streams you would like to fetch data for, according to the\
                format described in the previous section. If no list is provided, data is fetched for all streams.

            axisOrder (enum, optional): the shape of each series in the response. Options: `'TIME_MAJOR'` and\
                `'TIME_MINOR'`. Default value, if not specified, is `'TIME_MAJOR'`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            dict: response from the `get` request
        """
        return self.__sim_client.results_plain(
            id=self.__job['dataArray'],
            start=start,
            stop=stop,
            binWidth=binWidth,
            limit=limit,
            axisOrder=axisOrder,
            streams=streams
        )

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
