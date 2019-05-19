# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from  ..models.component_descriptor_id import ComponentDescriptorId  # noqa: F401,E501


class ComponentDescriptor(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'actions': 'str',
        'clazz': 'str',
        'configuration_descriptor': 'str',
        'created_time': 'int',
        'id': 'ComponentDescriptorId',
        'name': 'str',
        'scope': 'str',
        'type': 'str'
    }

    attribute_map = {
        'actions': 'actions',
        'clazz': 'clazz',
        'configuration_descriptor': 'configurationDescriptor',
        'created_time': 'createdTime',
        'id': 'id',
        'name': 'name',
        'scope': 'scope',
        'type': 'type'
    }

    def __init__(self, actions=None, clazz=None, configuration_descriptor=None, created_time=None, id=None, name=None, scope=None, type=None):  # noqa: E501
        """ComponentDescriptor - a model defined in Swagger"""  # noqa: E501

        self._actions = None
        self._clazz = None
        self._configuration_descriptor = None
        self._created_time = None
        self._id = None
        self._name = None
        self._scope = None
        self._type = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        if clazz is not None:
            self.clazz = clazz
        if configuration_descriptor is not None:
            self.configuration_descriptor = configuration_descriptor
        if created_time is not None:
            self.created_time = created_time
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if scope is not None:
            self.scope = scope
        if type is not None:
            self.type = type

    @property
    def actions(self):
        """Gets the actions of this ComponentDescriptor.  # noqa: E501


        :return: The actions of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ComponentDescriptor.


        :param actions: The actions of this ComponentDescriptor.  # noqa: E501
        :type: str
        """

        self._actions = actions

    @property
    def clazz(self):
        """Gets the clazz of this ComponentDescriptor.  # noqa: E501


        :return: The clazz of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._clazz

    @clazz.setter
    def clazz(self, clazz):
        """Sets the clazz of this ComponentDescriptor.


        :param clazz: The clazz of this ComponentDescriptor.  # noqa: E501
        :type: str
        """

        self._clazz = clazz

    @property
    def configuration_descriptor(self):
        """Gets the configuration_descriptor of this ComponentDescriptor.  # noqa: E501


        :return: The configuration_descriptor of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._configuration_descriptor

    @configuration_descriptor.setter
    def configuration_descriptor(self, configuration_descriptor):
        """Sets the configuration_descriptor of this ComponentDescriptor.


        :param configuration_descriptor: The configuration_descriptor of this ComponentDescriptor.  # noqa: E501
        :type: str
        """

        self._configuration_descriptor = configuration_descriptor

    @property
    def created_time(self):
        """Gets the created_time of this ComponentDescriptor.  # noqa: E501


        :return: The created_time of this ComponentDescriptor.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ComponentDescriptor.


        :param created_time: The created_time of this ComponentDescriptor.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def id(self):
        """Gets the id of this ComponentDescriptor.  # noqa: E501


        :return: The id of this ComponentDescriptor.  # noqa: E501
        :rtype: ComponentDescriptorId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentDescriptor.


        :param id: The id of this ComponentDescriptor.  # noqa: E501
        :type: ComponentDescriptorId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ComponentDescriptor.  # noqa: E501


        :return: The name of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentDescriptor.


        :param name: The name of this ComponentDescriptor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def scope(self):
        """Gets the scope of this ComponentDescriptor.  # noqa: E501


        :return: The scope of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ComponentDescriptor.


        :param scope: The scope of this ComponentDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYSTEM", "TENANT"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def type(self):
        """Gets the type of this ComponentDescriptor.  # noqa: E501


        :return: The type of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComponentDescriptor.


        :param type: The type of this ComponentDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENRICHMENT", "FILTER", "TRANSFORMATION", "ACTION", "EXTERNAL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ComponentDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
