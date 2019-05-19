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


class UserControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_user_using_delete(self, user_id, **kwargs):  # noqa: E501
        """deleteUser  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_user_using_delete(user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_id: userId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_user_using_delete_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_using_delete_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def delete_user_using_delete_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """deleteUser  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_user_using_delete_with_http_info(user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_id: userId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_user_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

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
            '/api/user/{userId}', 'DELETE',
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

    def get_activation_link_using_get(self, user_id, **kwargs):  # noqa: E501
        """getActivationLink  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_activation_link_using_get(user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_id: userId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_activation_link_using_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_activation_link_using_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_activation_link_using_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """getActivationLink  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_activation_link_using_get_with_http_info(user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_id: userId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_activation_link_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_activation_link_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/user/{userId}/activationLink', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_customer_users_using_get(self, customer_id, limit, **kwargs):  # noqa: E501
        """getCustomerUsers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_customer_users_using_get(customer_id, limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_id: customerId (required)
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_customer_users_using_get_with_http_info(customer_id, limit, **kwargs)  # noqa: E501
        else:
            (data) = self.get_customer_users_using_get_with_http_info(customer_id, limit, **kwargs)  # noqa: E501
            return data

    def get_customer_users_using_get_with_http_info(self, customer_id, limit, **kwargs):  # noqa: E501
        """getCustomerUsers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_customer_users_using_get_with_http_info(customer_id, limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_id: customerId (required)
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'limit', 'text_search', 'id_offset', 'text_offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_users_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_users_using_get`")  # noqa: E501
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_customer_users_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501

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
            '/api/customer/{customerId}/users{?textSearch,idOffset,textOffset,limit}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TextPageDataUser',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenant_admins_using_get(self, tenant_id, limit, **kwargs):  # noqa: E501
        """getTenantAdmins  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tenant_admins_using_get(tenant_id, limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tenant_id: tenantId (required)
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_tenant_admins_using_get_with_http_info(tenant_id, limit, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenant_admins_using_get_with_http_info(tenant_id, limit, **kwargs)  # noqa: E501
            return data

    def get_tenant_admins_using_get_with_http_info(self, tenant_id, limit, **kwargs):  # noqa: E501
        """getTenantAdmins  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tenant_admins_using_get_with_http_info(tenant_id, limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tenant_id: tenantId (required)
        :param str limit: limit (required)
        :param str text_search: textSearch
        :param str id_offset: idOffset
        :param str text_offset: textOffset
        :return: TextPageDataUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'limit', 'text_search', 'id_offset', 'text_offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tenant_admins_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_tenant_admins_using_get`")  # noqa: E501
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_tenant_admins_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenantId'] = params['tenant_id']  # noqa: E501

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
            '/api/tenant/{tenantId}/users{?textSearch,idOffset,textOffset,limit}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TextPageDataUser',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_by_id_using_get(self, user_id, **kwargs):  # noqa: E501
        """getUserById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_by_id_using_get(user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_id: userId (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_user_by_id_using_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_by_id_using_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_by_id_using_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """getUserById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_by_id_using_get_with_http_info(user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_id: userId (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

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
            '/api/user/{userId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_token_using_get(self, user_id, **kwargs):  # noqa: E501
        """getUserToken  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_token_using_get(user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_id: userId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_user_token_using_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_token_using_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_token_using_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """getUserToken  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_token_using_get_with_http_info(user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_id: userId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_token_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_token_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

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
            '/api/user/{userId}/token', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def is_user_token_access_enabled_using_get(self, **kwargs):  # noqa: E501
        """isUserTokenAccessEnabled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.is_user_token_access_enabled_using_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.is_user_token_access_enabled_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.is_user_token_access_enabled_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def is_user_token_access_enabled_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """isUserTokenAccessEnabled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.is_user_token_access_enabled_using_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: bool
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
                    " to method is_user_token_access_enabled_using_get" % key
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
            '/api/user/tokenAccessEnabled', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_user_using_post(self, user, **kwargs):  # noqa: E501
        """saveUser  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.save_user_using_post(user, async=True)
        >>> result = thread.get()

        :param async bool
        :param User user: user (required)
        :param bool send_activation_mail: sendActivationMail
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.save_user_using_post_with_http_info(user, **kwargs)  # noqa: E501
        else:
            (data) = self.save_user_using_post_with_http_info(user, **kwargs)  # noqa: E501
            return data

    def save_user_using_post_with_http_info(self, user, **kwargs):  # noqa: E501
        """saveUser  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.save_user_using_post_with_http_info(user, async=True)
        >>> result = thread.get()

        :param async bool
        :param User user: user (required)
        :param bool send_activation_mail: sendActivationMail
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user', 'send_activation_mail']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_user_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user' is set
        if ('user' not in params or
                params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `save_user_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'send_activation_mail' in params:
            query_params.append(('sendActivationMail', params['send_activation_mail']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user' in params:
            body_params = params['user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/user{?sendActivationMail}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_activation_email_using_post(self, email, **kwargs):  # noqa: E501
        """sendActivationEmail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_activation_email_using_post(email, async=True)
        >>> result = thread.get()

        :param async bool
        :param str email: email (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.send_activation_email_using_post_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.send_activation_email_using_post_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def send_activation_email_using_post_with_http_info(self, email, **kwargs):  # noqa: E501
        """sendActivationEmail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_activation_email_using_post_with_http_info(email, async=True)
        >>> result = thread.get()

        :param async bool
        :param str email: email (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_activation_email_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `send_activation_email_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'email' in params:
            query_params.append(('email', params['email']))  # noqa: E501

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
            '/api/user/sendActivationMail{?email}', 'POST',
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