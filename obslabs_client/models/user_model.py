# coding: utf-8

"""
    ObsLabs API

    # Authentication  ObsLabs uses basic auth to authenticate the API. You can create API keys in the account settings. Use your API key as the basic auth password. The username should be left blank (notice the colon sign before api-key that must be included). All requests must be made over https.  Example usage: ```bash curl -u :<YOUR API KEY> https://api.obslabs.io/v1/account ```  # Errors  The API returns a structured error response in case of failure. Below is the format of the error response object:  ```json {   \"error\": {     \"status\": 400,     \"code\": \"VALIDATION\",     \"message\": \"Validation errors occurred.\",     \"details\": [       {         \"field\": \"email\",         \"issue\": \"The email address is not in a valid format.\"       },       {         \"field\": \"password\",         \"issue\": \"The password must be at least 8 characters long.\"       }     ]   } } 

    The version of the OpenAPI document: 1.0
    Contact: contact@obslabs.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from obslabs_client.models.user_organization_role_model import UserOrganizationRoleModel
from obslabs_client.models.user_project_role_model import UserProjectRoleModel
from typing import Optional, Set
from typing_extensions import Self

class UserModel(BaseModel):
    """
    UserModel
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    email: StrictStr
    organizations_role: List[UserOrganizationRoleModel]
    projects_role: List[UserProjectRoleModel]
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "name", "email", "organizations_role", "projects_role"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in organizations_role (list)
        _items = []
        if self.organizations_role:
            for _item_organizations_role in self.organizations_role:
                if _item_organizations_role:
                    _items.append(_item_organizations_role.to_dict())
            _dict['organizations_role'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in projects_role (list)
        _items = []
        if self.projects_role:
            for _item_projects_role in self.projects_role:
                if _item_projects_role:
                    _items.append(_item_projects_role.to_dict())
            _dict['projects_role'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "organizations_role": [UserOrganizationRoleModel.from_dict(_item) for _item in obj["organizations_role"]] if obj.get("organizations_role") is not None else None,
            "projects_role": [UserProjectRoleModel.from_dict(_item) for _item in obj["projects_role"]] if obj.get("projects_role") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


