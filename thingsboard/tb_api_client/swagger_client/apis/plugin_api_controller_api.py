# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class PluginApiControllerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def process_request_using_delete(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_delete(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.process_request_using_delete_with_http_info(plugin_token, **kwargs)
        else:
            (data) = self.process_request_using_delete_with_http_info(plugin_token, **kwargs)
            return data

    def process_request_using_delete_with_http_info(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_delete_with_http_info(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plugin_token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plugin_token' is set
        if ('plugin_token' not in params) or (params['plugin_token'] is None):
            raise ValueError("Missing the required parameter `plugin_token` when calling `process_request_using_delete`")


        collection_formats = {}

        path_params = {}
        if 'plugin_token' in params:
            path_params['pluginToken'] = params['plugin_token']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api('/api/plugins/{pluginToken}/**', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeferredResultResponseEntity',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def process_request_using_get(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_get(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.process_request_using_get_with_http_info(plugin_token, **kwargs)
        else:
            (data) = self.process_request_using_get_with_http_info(plugin_token, **kwargs)
            return data

    def process_request_using_get_with_http_info(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_get_with_http_info(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plugin_token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plugin_token' is set
        if ('plugin_token' not in params) or (params['plugin_token'] is None):
            raise ValueError("Missing the required parameter `plugin_token` when calling `process_request_using_get`")


        collection_formats = {}

        path_params = {}
        if 'plugin_token' in params:
            path_params['pluginToken'] = params['plugin_token']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api('/api/plugins/{pluginToken}/**', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeferredResultResponseEntity',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def process_request_using_head(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_head(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.process_request_using_head_with_http_info(plugin_token, **kwargs)
        else:
            (data) = self.process_request_using_head_with_http_info(plugin_token, **kwargs)
            return data

    def process_request_using_head_with_http_info(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_head_with_http_info(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plugin_token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_head" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plugin_token' is set
        if ('plugin_token' not in params) or (params['plugin_token'] is None):
            raise ValueError("Missing the required parameter `plugin_token` when calling `process_request_using_head`")


        collection_formats = {}

        path_params = {}
        if 'plugin_token' in params:
            path_params['pluginToken'] = params['plugin_token']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api('/api/plugins/{pluginToken}/**', 'HEAD',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeferredResultResponseEntity',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def process_request_using_options(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_options(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.process_request_using_options_with_http_info(plugin_token, **kwargs)
        else:
            (data) = self.process_request_using_options_with_http_info(plugin_token, **kwargs)
            return data

    def process_request_using_options_with_http_info(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_options_with_http_info(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plugin_token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plugin_token' is set
        if ('plugin_token' not in params) or (params['plugin_token'] is None):
            raise ValueError("Missing the required parameter `plugin_token` when calling `process_request_using_options`")


        collection_formats = {}

        path_params = {}
        if 'plugin_token' in params:
            path_params['pluginToken'] = params['plugin_token']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api('/api/plugins/{pluginToken}/**', 'OPTIONS',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeferredResultResponseEntity',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def process_request_using_patch(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_patch(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.process_request_using_patch_with_http_info(plugin_token, **kwargs)
        else:
            (data) = self.process_request_using_patch_with_http_info(plugin_token, **kwargs)
            return data

    def process_request_using_patch_with_http_info(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_patch_with_http_info(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plugin_token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plugin_token' is set
        if ('plugin_token' not in params) or (params['plugin_token'] is None):
            raise ValueError("Missing the required parameter `plugin_token` when calling `process_request_using_patch`")


        collection_formats = {}

        path_params = {}
        if 'plugin_token' in params:
            path_params['pluginToken'] = params['plugin_token']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api('/api/plugins/{pluginToken}/**', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeferredResultResponseEntity',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def process_request_using_post(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_post(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.process_request_using_post_with_http_info(plugin_token, **kwargs)
        else:
            (data) = self.process_request_using_post_with_http_info(plugin_token, **kwargs)
            return data

    def process_request_using_post_with_http_info(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_post_with_http_info(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plugin_token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plugin_token' is set
        if ('plugin_token' not in params) or (params['plugin_token'] is None):
            raise ValueError("Missing the required parameter `plugin_token` when calling `process_request_using_post`")


        collection_formats = {}

        path_params = {}
        if 'plugin_token' in params:
            path_params['pluginToken'] = params['plugin_token']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api('/api/plugins/{pluginToken}/**', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeferredResultResponseEntity',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def process_request_using_put(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_put(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.process_request_using_put_with_http_info(plugin_token, **kwargs)
        else:
            (data) = self.process_request_using_put_with_http_info(plugin_token, **kwargs)
            return data

    def process_request_using_put_with_http_info(self, plugin_token, **kwargs):
        """
        processRequest
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.process_request_using_put_with_http_info(plugin_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str plugin_token: pluginToken (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plugin_token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plugin_token' is set
        if ('plugin_token' not in params) or (params['plugin_token'] is None):
            raise ValueError("Missing the required parameter `plugin_token` when calling `process_request_using_put`")


        collection_formats = {}

        path_params = {}
        if 'plugin_token' in params:
            path_params['pluginToken'] = params['plugin_token']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api('/api/plugins/{pluginToken}/**', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeferredResultResponseEntity',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
