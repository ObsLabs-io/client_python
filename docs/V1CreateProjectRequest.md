# V1CreateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from obslabs_client.models.v1_create_project_request import V1CreateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateProjectRequest from a JSON string
v1_create_project_request_instance = V1CreateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(V1CreateProjectRequest.to_json())

# convert the object into a dict
v1_create_project_request_dict = v1_create_project_request_instance.to_dict()
# create an instance of V1CreateProjectRequest from a dict
v1_create_project_request_from_dict = V1CreateProjectRequest.from_dict(v1_create_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


