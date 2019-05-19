# coding: utf-8

# flake8: noqa
"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.admin_settings import AdminSettings
from swagger_client.models.admin_settings_id import AdminSettingsId
from swagger_client.models.alarm import Alarm
from swagger_client.models.alarm_id import AlarmId
from swagger_client.models.alarm_info import AlarmInfo
from swagger_client.models.asset import Asset
from swagger_client.models.asset_id import AssetId
from swagger_client.models.asset_search_query import AssetSearchQuery
from swagger_client.models.attributes_entity_view import AttributesEntityView
from swagger_client.models.audit_log import AuditLog
from swagger_client.models.audit_log_id import AuditLogId
from swagger_client.models.component_descriptor import ComponentDescriptor
from swagger_client.models.component_descriptor_id import ComponentDescriptorId
from swagger_client.models.customer import Customer
from swagger_client.models.customer_id import CustomerId
from swagger_client.models.dashboard import Dashboard
from swagger_client.models.dashboard_id import DashboardId
from swagger_client.models.dashboard_info import DashboardInfo
from swagger_client.models.deferred_result_response_entity import DeferredResultResponseEntity
from swagger_client.models.device import Device
from swagger_client.models.device_credentials import DeviceCredentials
from swagger_client.models.device_credentials_id import DeviceCredentialsId
from swagger_client.models.device_id import DeviceId
from swagger_client.models.device_search_query import DeviceSearchQuery
from swagger_client.models.entity_id import EntityId
from swagger_client.models.entity_relation import EntityRelation
from swagger_client.models.entity_relation_info import EntityRelationInfo
from swagger_client.models.entity_relations_query import EntityRelationsQuery
from swagger_client.models.entity_subtype import EntitySubtype
from swagger_client.models.entity_type_filter import EntityTypeFilter
from swagger_client.models.entity_view import EntityView
from swagger_client.models.entity_view_id import EntityViewId
from swagger_client.models.entity_view_search_query import EntityViewSearchQuery
from swagger_client.models.event import Event
from swagger_client.models.event_id import EventId
from swagger_client.models.node_connection_info import NodeConnectionInfo
from swagger_client.models.relations_search_parameters import RelationsSearchParameters
from swagger_client.models.response_entity import ResponseEntity
from swagger_client.models.rule_chain import RuleChain
from swagger_client.models.rule_chain_connection_info import RuleChainConnectionInfo
from swagger_client.models.rule_chain_id import RuleChainId
from swagger_client.models.rule_chain_meta_data import RuleChainMetaData
from swagger_client.models.rule_node import RuleNode
from swagger_client.models.rule_node_id import RuleNodeId
from swagger_client.models.short_customer_info import ShortCustomerInfo
from swagger_client.models.telemetry_entity_view import TelemetryEntityView
from swagger_client.models.tenant import Tenant
from swagger_client.models.tenant_id import TenantId
from swagger_client.models.text_page_data_asset import TextPageDataAsset
from swagger_client.models.text_page_data_customer import TextPageDataCustomer
from swagger_client.models.text_page_data_dashboard_info import TextPageDataDashboardInfo
from swagger_client.models.text_page_data_device import TextPageDataDevice
from swagger_client.models.text_page_data_entity_view import TextPageDataEntityView
from swagger_client.models.text_page_data_rule_chain import TextPageDataRuleChain
from swagger_client.models.text_page_data_tenant import TextPageDataTenant
from swagger_client.models.text_page_data_user import TextPageDataUser
from swagger_client.models.text_page_data_widgets_bundle import TextPageDataWidgetsBundle
from swagger_client.models.text_page_link import TextPageLink
from swagger_client.models.time_page_data_alarm_info import TimePageDataAlarmInfo
from swagger_client.models.time_page_data_audit_log import TimePageDataAuditLog
from swagger_client.models.time_page_data_dashboard_info import TimePageDataDashboardInfo
from swagger_client.models.time_page_data_event import TimePageDataEvent
from swagger_client.models.time_page_link import TimePageLink
from swagger_client.models.update_message import UpdateMessage
from swagger_client.models.user import User
from swagger_client.models.user_id import UserId
from swagger_client.models.widget_type import WidgetType
from swagger_client.models.widget_type_id import WidgetTypeId
from swagger_client.models.widgets_bundle import WidgetsBundle
from swagger_client.models.widgets_bundle_id import WidgetsBundleId
