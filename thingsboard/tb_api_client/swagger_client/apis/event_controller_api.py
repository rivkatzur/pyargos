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


class EventControllerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_events_using_get(self, entity_type, entity_id, event_type, tenant_id, limit, **kwargs):
        """
        getEvents
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_events_using_get(entity_type, entity_id, event_type, tenant_id, limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :param str event_type: eventType (required)
        :param str tenant_id: tenantId (required)
        :param int limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_events_using_get_with_http_info(entity_type, entity_id, event_type, tenant_id, limit, **kwargs)
        else:
            (data) = self.get_events_using_get_with_http_info(entity_type, entity_id, event_type, tenant_id, limit, **kwargs)
            return data

    def get_events_using_get_with_http_info(self, entity_type, entity_id, event_type, tenant_id, limit, **kwargs):
        """
        getEvents
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_events_using_get_with_http_info(entity_type, entity_id, event_type, tenant_id, limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :param str event_type: eventType (required)
        :param str tenant_id: tenantId (required)
        :param int limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'event_type', 'tenant_id', 'limit', 'start_time', 'end_time', 'asc_order', 'offset']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params) or (params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_events_using_get`")
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params) or (params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_events_using_get`")
        # verify the required parameter 'event_type' is set
        if ('event_type' not in params) or (params['event_type'] is None):
            raise ValueError("Missing the required parameter `event_type` when calling `get_events_using_get`")
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_events_using_get`")
        # verify the required parameter 'limit' is set
        if ('limit' not in params) or (params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_events_using_get`")


        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']
        if 'event_type' in params:
            path_params['eventType'] = params['event_type']

        query_params = []
        if 'tenant_id' in params:
            query_params.append(('tenantId', params['tenant_id']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))
        if 'asc_order' in params:
            query_params.append(('ascOrder', params['asc_order']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))

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

        return self.api_client.call_api('/api/events/{entityType}/{entityId}/{eventType}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TimePageDataEvent',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_events_using_get1(self, entity_type, entity_id, tenant_id, limit, **kwargs):
        """
        getEvents
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_events_using_get1(entity_type, entity_id, tenant_id, limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :param str tenant_id: tenantId (required)
        :param int limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_events_using_get1_with_http_info(entity_type, entity_id, tenant_id, limit, **kwargs)
        else:
            (data) = self.get_events_using_get1_with_http_info(entity_type, entity_id, tenant_id, limit, **kwargs)
            return data

    def get_events_using_get1_with_http_info(self, entity_type, entity_id, tenant_id, limit, **kwargs):
        """
        getEvents
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_events_using_get1_with_http_info(entity_type, entity_id, tenant_id, limit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :param str tenant_id: tenantId (required)
        :param int limit: limit (required)
        :param int start_time: startTime
        :param int end_time: endTime
        :param bool asc_order: ascOrder
        :param str offset: offset
        :return: TimePageDataEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'tenant_id', 'limit', 'start_time', 'end_time', 'asc_order', 'offset']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params) or (params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_events_using_get1`")
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params) or (params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_events_using_get1`")
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_events_using_get1`")
        # verify the required parameter 'limit' is set
        if ('limit' not in params) or (params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_events_using_get1`")


        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']

        query_params = []
        if 'tenant_id' in params:
            query_params.append(('tenantId', params['tenant_id']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))
        if 'asc_order' in params:
            query_params.append(('ascOrder', params['asc_order']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))

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

        return self.api_client.call_api('/api/events/{entityType}/{entityId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TimePageDataEvent',
                                        auth_settings=auth_settings,
                                        asynch=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
