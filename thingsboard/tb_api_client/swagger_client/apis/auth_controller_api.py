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


class AuthControllerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def activate_user_using_post(self, activate_token, password, **kwargs):
        """
        activateUser
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.activate_user_using_post(activate_token, password, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activate_token: activateToken (required)
        :param str password: password (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.activate_user_using_post_with_http_info(activate_token, password, **kwargs)
        else:
            (data) = self.activate_user_using_post_with_http_info(activate_token, password, **kwargs)
            return data

    def activate_user_using_post_with_http_info(self, activate_token, password, **kwargs):
        """
        activateUser
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.activate_user_using_post_with_http_info(activate_token, password, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activate_token: activateToken (required)
        :param str password: password (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activate_token', 'password']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_user_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activate_token' is set
        if ('activate_token' not in params) or (params['activate_token'] is None):
            raise ValueError("Missing the required parameter `activate_token` when calling `activate_user_using_post`")
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `activate_user_using_post`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'activate_token' in params:
            query_params.append(('activateToken', params['activate_token']))
        if 'password' in params:
            query_params.append(('password', params['password']))

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
        auth_settings = []

        return self.api_client.call_api('/api/noauth/activate', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def change_password_using_post(self, current_password, new_password, **kwargs):
        """
        changePassword
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.change_password_using_post(current_password, new_password, async=True)
        >>> result = thread.get()

        :param async bool
        :param str current_password: currentPassword (required)
        :param str new_password: newPassword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.change_password_using_post_with_http_info(current_password, new_password, **kwargs)
        else:
            (data) = self.change_password_using_post_with_http_info(current_password, new_password, **kwargs)
            return data

    def change_password_using_post_with_http_info(self, current_password, new_password, **kwargs):
        """
        changePassword
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.change_password_using_post_with_http_info(current_password, new_password, async=True)
        >>> result = thread.get()

        :param async bool
        :param str current_password: currentPassword (required)
        :param str new_password: newPassword (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['current_password', 'new_password']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_password_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'current_password' is set
        if ('current_password' not in params) or (params['current_password'] is None):
            raise ValueError("Missing the required parameter `current_password` when calling `change_password_using_post`")
        # verify the required parameter 'new_password' is set
        if ('new_password' not in params) or (params['new_password'] is None):
            raise ValueError("Missing the required parameter `new_password` when calling `change_password_using_post`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'current_password' in params:
            query_params.append(('currentPassword', params['current_password']))
        if 'new_password' in params:
            query_params.append(('newPassword', params['new_password']))

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

        return self.api_client.call_api('/api/auth/changePassword', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def check_activate_token_using_get(self, activate_token, **kwargs):
        """
        checkActivateToken
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.check_activate_token_using_get(activate_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activate_token: activateToken (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.check_activate_token_using_get_with_http_info(activate_token, **kwargs)
        else:
            (data) = self.check_activate_token_using_get_with_http_info(activate_token, **kwargs)
            return data

    def check_activate_token_using_get_with_http_info(self, activate_token, **kwargs):
        """
        checkActivateToken
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.check_activate_token_using_get_with_http_info(activate_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str activate_token: activateToken (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activate_token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_activate_token_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activate_token' is set
        if ('activate_token' not in params) or (params['activate_token'] is None):
            raise ValueError("Missing the required parameter `activate_token` when calling `check_activate_token_using_get`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'activate_token' in params:
            query_params.append(('activateToken', params['activate_token']))

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
        auth_settings = []

        return self.api_client.call_api('/api/noauth/activate', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def check_reset_token_using_get(self, reset_token, **kwargs):
        """
        checkResetToken
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.check_reset_token_using_get(reset_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str reset_token: resetToken (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.check_reset_token_using_get_with_http_info(reset_token, **kwargs)
        else:
            (data) = self.check_reset_token_using_get_with_http_info(reset_token, **kwargs)
            return data

    def check_reset_token_using_get_with_http_info(self, reset_token, **kwargs):
        """
        checkResetToken
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.check_reset_token_using_get_with_http_info(reset_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str reset_token: resetToken (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reset_token']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_reset_token_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reset_token' is set
        if ('reset_token' not in params) or (params['reset_token'] is None):
            raise ValueError("Missing the required parameter `reset_token` when calling `check_reset_token_using_get`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'reset_token' in params:
            query_params.append(('resetToken', params['reset_token']))

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
        auth_settings = []

        return self.api_client.call_api('/api/noauth/resetPassword', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_user_using_get(self, **kwargs):
        """
        getUser
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_using_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_user_using_get_with_http_info(**kwargs)
        else:
            (data) = self.get_user_using_get_with_http_info(**kwargs)
            return data

    def get_user_using_get_with_http_info(self, **kwargs):
        """
        getUser
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_using_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_using_get" % key
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
        header_params['Accept'] = self.api_client.\
            select_header_accept(['*/*'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['X-Authorization']

        return self.api_client.call_api('/api/auth/user', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='User',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def request_reset_password_by_email_using_post(self, email, **kwargs):
        """
        requestResetPasswordByEmail
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.request_reset_password_by_email_using_post(email, async=True)
        >>> result = thread.get()

        :param async bool
        :param str email: email (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.request_reset_password_by_email_using_post_with_http_info(email, **kwargs)
        else:
            (data) = self.request_reset_password_by_email_using_post_with_http_info(email, **kwargs)
            return data

    def request_reset_password_by_email_using_post_with_http_info(self, email, **kwargs):
        """
        requestResetPasswordByEmail
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.request_reset_password_by_email_using_post_with_http_info(email, async=True)
        >>> result = thread.get()

        :param async bool
        :param str email: email (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_reset_password_by_email_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params) or (params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `request_reset_password_by_email_using_post`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'email' in params:
            query_params.append(('email', params['email']))

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
        auth_settings = []

        return self.api_client.call_api('/api/noauth/resetPasswordByEmail', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def reset_password_using_post(self, reset_token, password, **kwargs):
        """
        resetPassword
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_password_using_post(reset_token, password, async=True)
        >>> result = thread.get()

        :param async bool
        :param str reset_token: resetToken (required)
        :param str password: password (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.reset_password_using_post_with_http_info(reset_token, password, **kwargs)
        else:
            (data) = self.reset_password_using_post_with_http_info(reset_token, password, **kwargs)
            return data

    def reset_password_using_post_with_http_info(self, reset_token, password, **kwargs):
        """
        resetPassword
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_password_using_post_with_http_info(reset_token, password, async=True)
        >>> result = thread.get()

        :param async bool
        :param str reset_token: resetToken (required)
        :param str password: password (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reset_token', 'password']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_password_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reset_token' is set
        if ('reset_token' not in params) or (params['reset_token'] is None):
            raise ValueError("Missing the required parameter `reset_token` when calling `reset_password_using_post`")
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `reset_password_using_post`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'reset_token' in params:
            query_params.append(('resetToken', params['reset_token']))
        if 'password' in params:
            query_params.append(('password', params['password']))

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
        auth_settings = []

        return self.api_client.call_api('/api/noauth/resetPassword', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
