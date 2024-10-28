# V1ProjectMemberUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from obslabs_client.models.v1_project_member_update_request import V1ProjectMemberUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ProjectMemberUpdateRequest from a JSON string
v1_project_member_update_request_instance = V1ProjectMemberUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(V1ProjectMemberUpdateRequest.to_json())

# convert the object into a dict
v1_project_member_update_request_dict = v1_project_member_update_request_instance.to_dict()
# create an instance of V1ProjectMemberUpdateRequest from a dict
v1_project_member_update_request_from_dict = V1ProjectMemberUpdateRequest.from_dict(v1_project_member_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


