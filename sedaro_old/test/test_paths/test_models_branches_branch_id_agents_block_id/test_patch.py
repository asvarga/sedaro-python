# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import sedaro_old
from sedaro_old.paths.models_branches_branch_id_agents_block_id import patch  # noqa: E501
from sedaro_old import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModelsBranchesBranchIdAgentsBlockId(ApiTestMixin, unittest.TestCase):
    """
    ModelsBranchesBranchIdAgentsBlockId unit test stubs
        Update Simulated Agent  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = patch.ApiForpatch(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
