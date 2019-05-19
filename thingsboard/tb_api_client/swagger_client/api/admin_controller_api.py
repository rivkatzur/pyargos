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

from ..api_client import ApiClient


class AdminControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def check_updates_using_get(self, **kwargs):  # noqa: E501
        """checkUpdates  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.check_updates_using_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: UpdateMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.check_updates_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.check_updates_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def check_updates_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """checkUpdates  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.check_updates_using_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: UpdateMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_updates_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/admin/updates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateMessage',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_admin_settings_using_get(self, key, **kwargs):  # noqa: E501
        """getAdminSettings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_admin_settings_using_get(key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str key: key (required)
        :return: AdminSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_admin_settings_using_get_with_http_info(key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_admin_settings_using_get_with_http_info(key, **kwargs)  # noqa: E501
            return data

    def get_admin_settings_using_get_with_http_info(self, key, **kwargs):  # noqa: E501
        """getAdminSettings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_admin_settings_using_get_with_http_info(key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str key: key (required)
        :return: AdminSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_admin_settings_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if ('key' not in params or
                params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `get_admin_settings_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

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
            '/api/admin/settings/{key}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdminSettings',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_admin_settings_using_post(self, admin_settings, **kwargs):  # noqa: E501
        """saveAdminSettings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.save_admin_settings_using_post(admin_settings, async=True)
        >>> result = thread.get()

        :param async bool
        :param AdminSettings admin_settings: adminSettings (required)
        :return: AdminSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.save_admin_settings_using_post_with_http_info(admin_settings, **kwargs)  # noqa: E501
        else:
            (data) = self.save_admin_settings_using_post_with_http_info(admin_settings, **kwargs)  # noqa: E501
            return data

    def save_admin_settings_using_post_with_http_info(self, admin_settings, **kwargs):  # noqa: E501
        """saveAdminSettings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.save_admin_settings_using_post_with_http_info(admin_settings, async=True)
        >>> result = thread.get()

        :param async bool
        :param AdminSettings admin_settings: adminSettings (required)
        :return: AdminSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['admin_settings']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_admin_settings_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'admin_settings' is set
        if ('admin_settings' not in params or
                params['admin_settings'] is None):
            raise ValueError("Missing the required parameter `admin_settings` when calling `save_admin_settings_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'admin_settings' in params:
            body_params = params['admin_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/admin/settings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdminSettings',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_test_mail_using_post(self, admin_settings, **kwargs):  # noqa: E501
        """sendTestMail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_test_mail_using_post(admin_settings, async=True)
        >>> result = thread.get()

        :param async bool
        :param AdminSettings admin_settings: adminSettings (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.send_test_mail_using_post_with_http_info(admin_settings, **kwargs)  # noqa: E501
        else:
            (data) = self.send_test_mail_using_post_with_http_info(admin_settings, **kwargs)  # noqa: E501
            return data

    def send_test_mail_using_post_with_http_info(self, admin_settings, **kwargs):  # noqa: E501
        """sendTestMail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_test_mail_using_post_with_http_info(admin_settings, async=True)
        >>> result = thread.get()

        :param async bool
        :param AdminSettings admin_settings: adminSettings (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['admin_settings']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_test_mail_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'admin_settings' is set
        if ('admin_settings' not in params or
                params['admin_settings'] is None):
            raise ValueError("Missing the required parameter `admin_settings` when calling `send_test_mail_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'admin_settings' in params:
            body_params = params['admin_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/admin/settings/testMail', 'POST',
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
