# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import sedaro_old
from sedaro_old.paths.simulation_branches_branch_id_control_job_id import delete  # noqa: E501
from sedaro_old import configuration, schemas, api_client

from .. import ApiTestMixin


class TestSimulationBranchesBranchIdControlJobId(ApiTestMixin, unittest.TestCase):
    """
    SimulationBranchesBranchIdControlJobId unit test stubs
        Terminate a running simulation  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
