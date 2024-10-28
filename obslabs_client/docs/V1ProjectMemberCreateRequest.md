# V1ProjectMemberCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from obslabs_client.models.v1_project_member_create_request import V1ProjectMemberCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ProjectMemberCreateRequest from a JSON string
v1_project_member_create_request_instance = V1ProjectMemberCreateRequest.from_json(json)
# print the JSON string representation of the object
print(V1ProjectMemberCreateRequest.to_json())

# convert the object into a dict
v1_project_member_create_request_dict = v1_project_member_create_request_instance.to_dict()
# create an instance of V1ProjectMemberCreateRequest from a dict
v1_project_member_create_request_from_dict = V1ProjectMemberCreateRequest.from_dict(v1_project_member_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


