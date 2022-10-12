# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import sedaro_base_client
from sedaro_base_client.paths.models_branches_branch_id_gnc_algorithms_attitude_determination_averaging_block_id import patch  # noqa: E501
from sedaro_base_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModelsBranchesBranchIdGncAlgorithmsAttitudeDeterminationAveragingBlockId(ApiTestMixin, unittest.TestCase):
    """
    ModelsBranchesBranchIdGncAlgorithmsAttitudeDeterminationAveragingBlockId unit test stubs
        Update Averaging Algorithm  # noqa: E501
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
