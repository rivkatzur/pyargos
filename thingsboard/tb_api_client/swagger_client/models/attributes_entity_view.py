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


class AttributesEntityView(object):
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
        'cs': 'list[str]',
        'sh': 'list[str]',
        'ss': 'list[str]'
    }

    attribute_map = {
        'cs': 'cs',
        'sh': 'sh',
        'ss': 'ss'
    }

    def __init__(self, cs=None, sh=None, ss=None):  # noqa: E501
        """AttributesEntityView - a model defined in Swagger"""  # noqa: E501

        self._cs = None
        self._sh = None
        self._ss = None
        self.discriminator = None

        if cs is not None:
            self.cs = cs
        if sh is not None:
            self.sh = sh
        if ss is not None:
            self.ss = ss

    @property
    def cs(self):
        """Gets the cs of this AttributesEntityView.  # noqa: E501


        :return: The cs of this AttributesEntityView.  # noqa: E501
        :rtype: list[str]
        """
        return self._cs

    @cs.setter
    def cs(self, cs):
        """Sets the cs of this AttributesEntityView.


        :param cs: The cs of this AttributesEntityView.  # noqa: E501
        :type: list[str]
        """

        self._cs = cs

    @property
    def sh(self):
        """Gets the sh of this AttributesEntityView.  # noqa: E501


        :return: The sh of this AttributesEntityView.  # noqa: E501
        :rtype: list[str]
        """
        return self._sh

    @sh.setter
    def sh(self, sh):
        """Sets the sh of this AttributesEntityView.


        :param sh: The sh of this AttributesEntityView.  # noqa: E501
        :type: list[str]
        """

        self._sh = sh

    @property
    def ss(self):
        """Gets the ss of this AttributesEntityView.  # noqa: E501


        :return: The ss of this AttributesEntityView.  # noqa: E501
        :rtype: list[str]
        """
        return self._ss

    @ss.setter
    def ss(self, ss):
        """Sets the ss of this AttributesEntityView.


        :param ss: The ss of this AttributesEntityView.  # noqa: E501
        :type: list[str]
        """

        self._ss = ss

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
        if not isinstance(other, AttributesEntityView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
