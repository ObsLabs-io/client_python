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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from obslabs_client.models.v1_create_channel_request_emails_inner import V1CreateChannelRequestEmailsInner
from obslabs_client.models.v1_create_channel_request_slacks_inner import V1CreateChannelRequestSlacksInner
from obslabs_client.models.v1_create_channel_request_smss_inner import V1CreateChannelRequestSmssInner
from obslabs_client.models.v1_create_channel_request_webhooks_inner import V1CreateChannelRequestWebhooksInner
from typing import Optional, Set
from typing_extensions import Self

class V1CreateChannelRequest(BaseModel):
    """
    V1CreateChannelRequest
    """ # noqa: E501
    name: Annotated[str, Field(min_length=3, strict=True, max_length=24)]
    emails: Optional[List[V1CreateChannelRequestEmailsInner]] = None
    webhooks: Optional[List[V1CreateChannelRequestWebhooksInner]] = None
    slacks: Optional[List[V1CreateChannelRequestSlacksInner]] = None
    smss: Optional[List[V1CreateChannelRequestSmssInner]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["name", "emails", "webhooks", "slacks", "smss"]

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
        """Create an instance of V1CreateChannelRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in emails (list)
        _items = []
        if self.emails:
            for _item_emails in self.emails:
                if _item_emails:
                    _items.append(_item_emails.to_dict())
            _dict['emails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in webhooks (list)
        _items = []
        if self.webhooks:
            for _item_webhooks in self.webhooks:
                if _item_webhooks:
                    _items.append(_item_webhooks.to_dict())
            _dict['webhooks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in slacks (list)
        _items = []
        if self.slacks:
            for _item_slacks in self.slacks:
                if _item_slacks:
                    _items.append(_item_slacks.to_dict())
            _dict['slacks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in smss (list)
        _items = []
        if self.smss:
            for _item_smss in self.smss:
                if _item_smss:
                    _items.append(_item_smss.to_dict())
            _dict['smss'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1CreateChannelRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "emails": [V1CreateChannelRequestEmailsInner.from_dict(_item) for _item in obj["emails"]] if obj.get("emails") is not None else None,
            "webhooks": [V1CreateChannelRequestWebhooksInner.from_dict(_item) for _item in obj["webhooks"]] if obj.get("webhooks") is not None else None,
            "slacks": [V1CreateChannelRequestSlacksInner.from_dict(_item) for _item in obj["slacks"]] if obj.get("slacks") is not None else None,
            "smss": [V1CreateChannelRequestSmssInner.from_dict(_item) for _item in obj["smss"]] if obj.get("smss") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


