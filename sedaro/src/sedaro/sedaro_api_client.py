from contextlib import contextmanager
from typing import Any, Dict, Generator

from sedaro_base_client import Configuration
from sedaro_base_client.api_client import ApiClient
from sedaro_base_client.apis.tags import branches_api

from sedaro.plain_request import PlainRequest

from .branches import AgentTemplateBranch, ScenarioBranch
from .settings import COMMON_API_KWARGS
from .utils import body_from_res


class SedaroApiClient(ApiClient):
    """A client to interact with the Sedaro API"""

    def __init__(
        self,
        api_key: 'str' = None,
        host='https://api.sedaro.com',
        *,
        auth_handle: 'str' = None,
        proxy_url: str = None,
        proxy_headers: Dict[str, str] = None
    ):
        '''Instantiate a SedaroApiClient. Either `api_key` or `auth_handle` must be provided.

        Args:
            api_key (str, optional): API key to authenticate with the Sedaro API
            host (str, optional): URL of the Sedaro API
            auth_handle (str, optional): Authentication handle to authenticate with the Sedaro API
            proxy_url (str, optional): URL of the proxy server
            proxy_headers (Dict[str, str], optional): Headers to send to the proxy server
        '''

        if (api_key and auth_handle) or not (api_key or auth_handle):
            raise ValueError('Either provide an `api_key` or an `auth_handle` and not both.')

        if host[-1] == '/':
            host = host[:-1]  # remove trailing forward slash

        self._api_host = host

        self._api_key = api_key
        self._auth_handle = auth_handle

        self._proxy_url = proxy_url
        self._proxy_headers = proxy_headers

    @contextmanager
    def api_client(self) -> Generator[ApiClient, Any, None]:
        """Instantiate ApiClient from sedaro_base_client

        Yields:
            Generator[ApiClient, Any, None]: ApiClient
        """
        if self._auth_handle is not None:
            header_name = 'X_AUTH_HANDLE'
            header_value = self._auth_handle
        else:
            header_name = 'X_API_KEY'
            header_value = self._api_key

        configuration = Configuration(host=self._api_host)
        configuration.proxy = self._proxy_url
        configuration.proxy_headers = self._proxy_headers

        with ApiClient(
            configuration=configuration,
            header_name=header_name,
            header_value=header_value
        ) as api:
            yield api

    def __get_branch(self, branch_id: str) -> Dict:
        """Get Sedaro `Branch` with given `branch_id` from `host`

        Args:
            branch_id (str): `id` of the Sedaro `Branch` to get

        Returns:
            Dict: `body` of the response as a `dict`
        """
        with self.api_client() as api:
            branches_api_instance = branches_api.BranchesApi(api)
            # res = branches_api_instance.get_branch(path_params={'branchId': id}) # TODO: temp_crud
            # return Branch(res.body, self)
            res = branches_api_instance.get_branch(
                path_params={'branchId': branch_id}, **COMMON_API_KWARGS)
            return body_from_res(res)

    def agent_template(self, branch_id: str) -> AgentTemplateBranch:
        """Instantiate an `AgentTemplateBranch` object associated with the Sedaro `Branch` with `branch_id`

        Args:
            branch_id (str): `id` of the Sedaro Agent Template `Branch` to get

        Returns:
            AgentTemplateBranch: `AgentTemplateBranch` object
        """
        return AgentTemplateBranch(self.__get_branch(branch_id), self)

    def scenario(self, branch_id: str) -> ScenarioBranch:
        """Instantiate an `ScenarioBranch` object associated with the Sedaro `Branch` with `branch_id`

        Args:
            branch_id (str): `id` of the Sedaro Agent Template `Branch` to get

        Returns:
            ScenarioBranch: `ScenarioBranch` object
        """
        return ScenarioBranch(self.__get_branch(branch_id), self)

    @property
    def request(self) -> PlainRequest:
        """API for sending raw `get`, `post`, `put`, `patch`, and `delete` requests to the configured Sedaro host."""
        return PlainRequest(self)
