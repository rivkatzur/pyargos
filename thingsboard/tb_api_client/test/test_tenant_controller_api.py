# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.tenant_controller_api import TenantControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTenantControllerApi(unittest.TestCase):
    """TenantControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.tenant_controller_api.TenantControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tenant_using_delete(self):
        """Test case for delete_tenant_using_delete

        deleteTenant  # noqa: E501
        """
        pass

    def test_get_tenant_by_id_using_get(self):
        """Test case for get_tenant_by_id_using_get

        getTenantById  # noqa: E501
        """
        pass

    def test_get_tenants_using_get(self):
        """Test case for get_tenants_using_get

        getTenants  # noqa: E501
        """
        pass

    def test_save_tenant_using_post(self):
        """Test case for save_tenant_using_post

        saveTenant  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
