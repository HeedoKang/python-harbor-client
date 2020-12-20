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


class ProjectMetadata(object):
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
        'public': 'str',
        'enable_content_trust': 'str',
        'prevent_vul': 'str',
        'severity': 'str',
        'auto_scan': 'str',
        'reuse_sys_cve_allowlist': 'str',
        'retention_id': 'str'
    }

    attribute_map = {
        'public': 'public',
        'enable_content_trust': 'enable_content_trust',
        'prevent_vul': 'prevent_vul',
        'severity': 'severity',
        'auto_scan': 'auto_scan',
        'reuse_sys_cve_allowlist': 'reuse_sys_cve_allowlist',
        'retention_id': 'retention_id'
    }

    def __init__(self, public=None, enable_content_trust=None, prevent_vul=None, severity=None, auto_scan=None, reuse_sys_cve_allowlist=None, retention_id=None):  # noqa: E501
        """ProjectMetadata - a model defined in Swagger"""  # noqa: E501

        self._public = None
        self._enable_content_trust = None
        self._prevent_vul = None
        self._severity = None
        self._auto_scan = None
        self._reuse_sys_cve_allowlist = None
        self._retention_id = None
        self.discriminator = None

        if public is not None:
            self.public = public
        if enable_content_trust is not None:
            self.enable_content_trust = enable_content_trust
        if prevent_vul is not None:
            self.prevent_vul = prevent_vul
        if severity is not None:
            self.severity = severity
        if auto_scan is not None:
            self.auto_scan = auto_scan
        if reuse_sys_cve_allowlist is not None:
            self.reuse_sys_cve_allowlist = reuse_sys_cve_allowlist
        if retention_id is not None:
            self.retention_id = retention_id

    @property
    def public(self):
        """Gets the public of this ProjectMetadata.  # noqa: E501

        The public status of the project. The valid values are \"true\", \"false\".  # noqa: E501

        :return: The public of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ProjectMetadata.

        The public status of the project. The valid values are \"true\", \"false\".  # noqa: E501

        :param public: The public of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._public = public

    @property
    def enable_content_trust(self):
        """Gets the enable_content_trust of this ProjectMetadata.  # noqa: E501

        Whether content trust is enabled or not. If it is enabled, user can't pull unsigned images from this project. The valid values are \"true\", \"false\".  # noqa: E501

        :return: The enable_content_trust of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._enable_content_trust

    @enable_content_trust.setter
    def enable_content_trust(self, enable_content_trust):
        """Sets the enable_content_trust of this ProjectMetadata.

        Whether content trust is enabled or not. If it is enabled, user can't pull unsigned images from this project. The valid values are \"true\", \"false\".  # noqa: E501

        :param enable_content_trust: The enable_content_trust of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._enable_content_trust = enable_content_trust

    @property
    def prevent_vul(self):
        """Gets the prevent_vul of this ProjectMetadata.  # noqa: E501

        Whether prevent the vulnerable images from running. The valid values are \"true\", \"false\".  # noqa: E501

        :return: The prevent_vul of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._prevent_vul

    @prevent_vul.setter
    def prevent_vul(self, prevent_vul):
        """Sets the prevent_vul of this ProjectMetadata.

        Whether prevent the vulnerable images from running. The valid values are \"true\", \"false\".  # noqa: E501

        :param prevent_vul: The prevent_vul of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._prevent_vul = prevent_vul

    @property
    def severity(self):
        """Gets the severity of this ProjectMetadata.  # noqa: E501

        If the vulnerability is high than severity defined here, the images can't be pulled. The valid values are \"none\", \"low\", \"medium\", \"high\", \"critical\".  # noqa: E501

        :return: The severity of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ProjectMetadata.

        If the vulnerability is high than severity defined here, the images can't be pulled. The valid values are \"none\", \"low\", \"medium\", \"high\", \"critical\".  # noqa: E501

        :param severity: The severity of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def auto_scan(self):
        """Gets the auto_scan of this ProjectMetadata.  # noqa: E501

        Whether scan images automatically when pushing. The valid values are \"true\", \"false\".  # noqa: E501

        :return: The auto_scan of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._auto_scan

    @auto_scan.setter
    def auto_scan(self, auto_scan):
        """Sets the auto_scan of this ProjectMetadata.

        Whether scan images automatically when pushing. The valid values are \"true\", \"false\".  # noqa: E501

        :param auto_scan: The auto_scan of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._auto_scan = auto_scan

    @property
    def reuse_sys_cve_allowlist(self):
        """Gets the reuse_sys_cve_allowlist of this ProjectMetadata.  # noqa: E501

        Whether this project reuse the system level CVE allowlist as the allowlist of its own.  The valid values are \"true\", \"false\". If it is set to \"true\" the actual allowlist associate with this project, if any, will be ignored.  # noqa: E501

        :return: The reuse_sys_cve_allowlist of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._reuse_sys_cve_allowlist

    @reuse_sys_cve_allowlist.setter
    def reuse_sys_cve_allowlist(self, reuse_sys_cve_allowlist):
        """Sets the reuse_sys_cve_allowlist of this ProjectMetadata.

        Whether this project reuse the system level CVE allowlist as the allowlist of its own.  The valid values are \"true\", \"false\". If it is set to \"true\" the actual allowlist associate with this project, if any, will be ignored.  # noqa: E501

        :param reuse_sys_cve_allowlist: The reuse_sys_cve_allowlist of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._reuse_sys_cve_allowlist = reuse_sys_cve_allowlist

    @property
    def retention_id(self):
        """Gets the retention_id of this ProjectMetadata.  # noqa: E501

        The ID of the tag retention policy for the project  # noqa: E501

        :return: The retention_id of this ProjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._retention_id

    @retention_id.setter
    def retention_id(self, retention_id):
        """Sets the retention_id of this ProjectMetadata.

        The ID of the tag retention policy for the project  # noqa: E501

        :param retention_id: The retention_id of this ProjectMetadata.  # noqa: E501
        :type: str
        """

        self._retention_id = retention_id

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
        if issubclass(ProjectMetadata, dict):
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
        if not isinstance(other, ProjectMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
