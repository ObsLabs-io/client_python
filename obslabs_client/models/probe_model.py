# coding: utf-8

"""
    ObsLabs API

    # Authentication  ObsLabs uses basic auth to authenticate the API. You can create API keys in the account settings. Use your API key as the basic auth password. The username should be left blank (notice the colon sign before api-key that must be included). All requests must be made over https.  Example usage: ```bash curl -u :<YOUR API KEY> https://api.obslabs.io/v1/users/me ```  # Errors  The API returns a structured error response in case of failure. Below is the format of the error response object:  ```json {   \"error\": {     \"status\": 400,     \"code\": \"VALIDATION\",     \"message\": \"Validation errors occurred.\",     \"details\": [       {         \"field\": \"email\",         \"issue\": \"The email address is not in a valid format.\"       },       {         \"field\": \"password\",         \"issue\": \"The password must be at least 8 characters long.\"       }     ]   } } 

    The version of the OpenAPI document: 1.0
    Contact: contact@obslabs.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from obslabs_client.models.probe_channel_model import ProbeChannelModel
from typing import Optional, Set
from typing_extensions import Self

class ProbeModel(BaseModel):
    """
    ProbeModel
    """ # noqa: E501
    id: StrictStr
    name: Annotated[str, Field(min_length=3, strict=True, max_length=16)]
    type: StrictStr
    url: StrictStr
    status: StrictStr
    status_checked_at: Optional[datetime]
    status_changed_at: Optional[datetime]
    schedule: Dict[str, Any]
    channels: List[ProbeChannelModel]
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "name", "type", "url", "status", "status_checked_at", "status_changed_at", "schedule", "channels"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['push', 'pull']):
            raise ValueError("must be one of enum values ('push', 'pull')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['success', 'failure', 'paused']):
            raise ValueError("must be one of enum values ('success', 'failure', 'paused')")
        return value

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
        """Create an instance of ProbeModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in channels (list)
        _items = []
        if self.channels:
            for _item_channels in self.channels:
                if _item_channels:
                    _items.append(_item_channels.to_dict())
            _dict['channels'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if status_checked_at (nullable) is None
        # and model_fields_set contains the field
        if self.status_checked_at is None and "status_checked_at" in self.model_fields_set:
            _dict['status_checked_at'] = None

        # set to None if status_changed_at (nullable) is None
        # and model_fields_set contains the field
        if self.status_changed_at is None and "status_changed_at" in self.model_fields_set:
            _dict['status_changed_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProbeModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "url": obj.get("url"),
            "status": obj.get("status"),
            "status_checked_at": obj.get("status_checked_at"),
            "status_changed_at": obj.get("status_changed_at"),
            "schedule": ProbeScheduleModel.from_dict(obj["schedule"]) if obj.get("schedule") is not None else None,
            "channels": [ProbeChannelModel.from_dict(_item) for _item in obj["channels"]] if obj.get("channels") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

