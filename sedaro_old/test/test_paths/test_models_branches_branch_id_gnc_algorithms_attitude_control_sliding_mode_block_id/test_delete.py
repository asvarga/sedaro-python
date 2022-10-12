# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import sedaro
from sedaro.paths.models_branches_branch_id_gnc_algorithms_attitude_control_sliding_mode_block_id import delete  # noqa: E501
from sedaro import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModelsBranchesBranchIdGncAlgorithmsAttitudeControlSlidingModeBlockId(ApiTestMixin, unittest.TestCase):
    """
    ModelsBranchesBranchIdGncAlgorithmsAttitudeControlSlidingModeBlockId unit test stubs
        Delete Sliding Mode 3x3 Algorithm  # noqa: E501
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
