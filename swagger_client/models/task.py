# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Task(object):
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
        'id': 'int',
        'execution_id': 'int',
        'status': 'str',
        'status_message': 'str',
        'run_count': 'int',
        'extra_attrs': 'ExtraAttrs',
        'creation_time': 'str',
        'update_time': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'execution_id': 'execution_id',
        'status': 'status',
        'status_message': 'status_message',
        'run_count': 'run_count',
        'extra_attrs': 'extra_attrs',
        'creation_time': 'creation_time',
        'update_time': 'update_time',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, execution_id=None, status=None, status_message=None, run_count=None, extra_attrs=None, creation_time=None, update_time=None, start_time=None, end_time=None):  # noqa: E501
        """Task - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._execution_id = None
        self._status = None
        self._status_message = None
        self._run_count = None
        self._extra_attrs = None
        self._creation_time = None
        self._update_time = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if execution_id is not None:
            self.execution_id = execution_id
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if run_count is not None:
            self.run_count = run_count
        if extra_attrs is not None:
            self.extra_attrs = extra_attrs
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this Task.  # noqa: E501

        The ID of task  # noqa: E501

        :return: The id of this Task.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.

        The ID of task  # noqa: E501

        :param id: The id of this Task.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def execution_id(self):
        """Gets the execution_id of this Task.  # noqa: E501

        The ID of task execution  # noqa: E501

        :return: The execution_id of this Task.  # noqa: E501
        :rtype: int
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this Task.

        The ID of task execution  # noqa: E501

        :param execution_id: The execution_id of this Task.  # noqa: E501
        :type: int
        """

        self._execution_id = execution_id

    @property
    def status(self):
        """Gets the status of this Task.  # noqa: E501

        The status of task  # noqa: E501

        :return: The status of this Task.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.

        The status of task  # noqa: E501

        :param status: The status of this Task.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this Task.  # noqa: E501

        The status message of task  # noqa: E501

        :return: The status_message of this Task.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this Task.

        The status message of task  # noqa: E501

        :param status_message: The status_message of this Task.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def run_count(self):
        """Gets the run_count of this Task.  # noqa: E501

        The count of task run  # noqa: E501

        :return: The run_count of this Task.  # noqa: E501
        :rtype: int
        """
        return self._run_count

    @run_count.setter
    def run_count(self, run_count):
        """Sets the run_count of this Task.

        The count of task run  # noqa: E501

        :param run_count: The run_count of this Task.  # noqa: E501
        :type: int
        """

        self._run_count = run_count

    @property
    def extra_attrs(self):
        """Gets the extra_attrs of this Task.  # noqa: E501


        :return: The extra_attrs of this Task.  # noqa: E501
        :rtype: ExtraAttrs
        """
        return self._extra_attrs

    @extra_attrs.setter
    def extra_attrs(self, extra_attrs):
        """Sets the extra_attrs of this Task.


        :param extra_attrs: The extra_attrs of this Task.  # noqa: E501
        :type: ExtraAttrs
        """

        self._extra_attrs = extra_attrs

    @property
    def creation_time(self):
        """Gets the creation_time of this Task.  # noqa: E501

        The creation time of task  # noqa: E501

        :return: The creation_time of this Task.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Task.

        The creation time of task  # noqa: E501

        :param creation_time: The creation_time of this Task.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this Task.  # noqa: E501

        The update time of task  # noqa: E501

        :return: The update_time of this Task.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Task.

        The update time of task  # noqa: E501

        :param update_time: The update_time of this Task.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def start_time(self):
        """Gets the start_time of this Task.  # noqa: E501

        The start time of task  # noqa: E501

        :return: The start_time of this Task.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Task.

        The start time of task  # noqa: E501

        :param start_time: The start_time of this Task.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Task.  # noqa: E501

        The end time of task  # noqa: E501

        :return: The end_time of this Task.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Task.

        The end time of task  # noqa: E501

        :param end_time: The end_time of this Task.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

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
        if issubclass(Task, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
