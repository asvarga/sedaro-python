# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import sedaro
from sedaro.paths.models_branches_branch_id_gnc_sensors_vector_sensors_block_id import delete  # noqa: E501
from sedaro import configuration, schemas, api_client

from .. import ApiTestMixin


class TestModelsBranchesBranchIdGncSensorsVectorSensorsBlockId(ApiTestMixin, unittest.TestCase):
    """
    ModelsBranchesBranchIdGncSensorsVectorSensorsBlockId unit test stubs
        Delete Vector Sensor  # noqa: E501
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
