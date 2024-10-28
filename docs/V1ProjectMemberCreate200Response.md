# V1ProjectMemberCreate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**ProjectMemberModel**](ProjectMemberModel.md) |  | 

## Example

```python
from obslabs_client.models.v1_project_member_create200_response import V1ProjectMemberCreate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ProjectMemberCreate200Response from a JSON string
v1_project_member_create200_response_instance = V1ProjectMemberCreate200Response.from_json(json)
# print the JSON string representation of the object
print(V1ProjectMemberCreate200Response.to_json())

# convert the object into a dict
v1_project_member_create200_response_dict = v1_project_member_create200_response_instance.to_dict()
# create an instance of V1ProjectMemberCreate200Response from a dict
v1_project_member_create200_response_from_dict = V1ProjectMemberCreate200Response.from_dict(v1_project_member_create200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


