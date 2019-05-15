# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TimePageLink(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'asc_order': 'bool',
        'end_time': 'int',
        'id_offset': 'str',
        'limit': 'int',
        'start_time': 'int'
    }

    attribute_map = {
        'asc_order': 'ascOrder',
        'end_time': 'endTime',
        'id_offset': 'idOffset',
        'limit': 'limit',
        'start_time': 'startTime'
    }

    def __init__(self, asc_order=None, end_time=None, id_offset=None, limit=None, start_time=None):
        """
        TimePageLink - a model defined in Swagger
        """

        self._asc_order = None
        self._end_time = None
        self._id_offset = None
        self._limit = None
        self._start_time = None
        self.discriminator = None

        if asc_order is not None:
          self.asc_order = asc_order
        if end_time is not None:
          self.end_time = end_time
        if id_offset is not None:
          self.id_offset = id_offset
        if limit is not None:
          self.limit = limit
        if start_time is not None:
          self.start_time = start_time

    @property
    def asc_order(self):
        """
        Gets the asc_order of this TimePageLink.

        :return: The asc_order of this TimePageLink.
        :rtype: bool
        """
        return self._asc_order

    @asc_order.setter
    def asc_order(self, asc_order):
        """
        Sets the asc_order of this TimePageLink.

        :param asc_order: The asc_order of this TimePageLink.
        :type: bool
        """

        self._asc_order = asc_order

    @property
    def end_time(self):
        """
        Gets the end_time of this TimePageLink.

        :return: The end_time of this TimePageLink.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this TimePageLink.

        :param end_time: The end_time of this TimePageLink.
        :type: int
        """

        self._end_time = end_time

    @property
    def id_offset(self):
        """
        Gets the id_offset of this TimePageLink.

        :return: The id_offset of this TimePageLink.
        :rtype: str
        """
        return self._id_offset

    @id_offset.setter
    def id_offset(self, id_offset):
        """
        Sets the id_offset of this TimePageLink.

        :param id_offset: The id_offset of this TimePageLink.
        :type: str
        """

        self._id_offset = id_offset

    @property
    def limit(self):
        """
        Gets the limit of this TimePageLink.

        :return: The limit of this TimePageLink.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this TimePageLink.

        :param limit: The limit of this TimePageLink.
        :type: int
        """

        self._limit = limit

    @property
    def start_time(self):
        """
        Gets the start_time of this TimePageLink.

        :return: The start_time of this TimePageLink.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this TimePageLink.

        :param start_time: The start_time of this TimePageLink.
        :type: int
        """

        self._start_time = start_time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TimePageLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other