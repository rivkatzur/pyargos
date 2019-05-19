# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from  ..api_client import ApiClient


class TenantControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_tenant_using_delete(self, tenant_id, **kwargs):  # noqa: E501
        """deleteTenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_tenant_using_delete(tenant_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tenant_id: tenantId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_tenant_using_delete_with_http_info(tenant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_tenant_using_delete_with_http_info(tenant_id, **kwargs)  # noqa: E501
            return data

    def delete_tenant_using_delete_with_http_info(self, tenant_id, **kwargs):  # noqa: E501
        """deleteTenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_tenant_using_delete_with_http_info(tenant_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tenant_id: tenantId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tenant_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `delete_tenant_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenantId'] = params['tenant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenant/{tenantId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenant_by_id_using_get(self, tenant_id, **kwargs):  # noqa: E501
        """getTenantById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tenant_by_id_using_get(tenant_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tenant_id: tenantId (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_tenant_by_id_using_get_with_http_info(tenant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenant_by_id_using_get_with_http_info(tenant_id, **kwargs)  # noqa: E501
            return data

    def get_tenant_by_id_using_get_with_http_info(self, tenant_id, **kwargs):  # noqa: E501
        """getTenantById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tenant_by_id_using_get_with_http_info(tenant_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tenant_id: tenantId (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tenant_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_tenant_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenantId'] = params['tenant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenant/{tenantId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tenant',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenants_using_get(self, limit, **kwargs):  # noqa: E501
        """getTenants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tenants_using_get(limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataTenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_tenants_using_get_with_http_info(limit, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenants_using_get_with_http_info(limit, **kwargs)  # noqa: E501
            return data

    def get_tenants_using_get_with_http_info(self, limit, **kwargs):  # noqa: E501
        """getTenants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tenants_using_get_with_http_info(limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataTenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'text_search', 'id_offset', 'text_offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tenants_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_tenants_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'id_offset' in params:
            query_params.append(('idOffset', params['id_offset']))  # noqa: E501
        if 'text_offset' in params:
            query_params.append(('textOffset', params['text_offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenants{?textSearch,idOffset,textOffset,limit}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TextPageDataTenant',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_tenant_using_post(self, tenant, **kwargs):  # noqa: E501
        """saveTenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.save_tenant_using_post(tenant, async=True)
        >>> result = thread.get()

        :param async bool
        :param Tenant tenant: tenant (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.save_tenant_using_post_with_http_info(tenant, **kwargs)  # noqa: E501
        else:
            (data) = self.save_tenant_using_post_with_http_info(tenant, **kwargs)  # noqa: E501
            return data

    def save_tenant_using_post_with_http_info(self, tenant, **kwargs):  # noqa: E501
        """saveTenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.save_tenant_using_post_with_http_info(tenant, async=True)
        >>> result = thread.get()

        :param async bool
        :param Tenant tenant: tenant (required)
        :return: Tenant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_tenant_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant' is set
        if ('tenant' not in params or
                params['tenant'] is None):
            raise ValueError("Missing the required parameter `tenant` when calling `save_tenant_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tenant' in params:
            body_params = params['tenant']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenant', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tenant',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
