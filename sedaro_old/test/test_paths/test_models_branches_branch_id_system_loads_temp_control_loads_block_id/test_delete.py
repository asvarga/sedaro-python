# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import sedaro_old
from sedaro_old.paths.models_branches_branch_id_system_loads_temp_control_loads_block_id import delete  # noqa: E501
from sedaro_old import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModelsBranchesBranchIdSystemLoadsTempControlLoadsBlockId(ApiTestMixin, unittest.TestCase):
    """
    ModelsBranchesBranchIdSystemLoadsTempControlLoadsBlockId unit test stubs
        Delete Temperature Controller Load  # noqa: E501
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
