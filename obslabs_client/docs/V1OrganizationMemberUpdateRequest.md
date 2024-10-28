# V1OrganizationMemberUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from obslabs_client.models.v1_organization_member_update_request import V1OrganizationMemberUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1OrganizationMemberUpdateRequest from a JSON string
v1_organization_member_update_request_instance = V1OrganizationMemberUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(V1OrganizationMemberUpdateRequest.to_json())

# convert the object into a dict
v1_organization_member_update_request_dict = v1_organization_member_update_request_instance.to_dict()
# create an instance of V1OrganizationMemberUpdateRequest from a dict
v1_organization_member_update_request_from_dict = V1OrganizationMemberUpdateRequest.from_dict(v1_organization_member_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


