# V1ListProjects200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[ProjectModel]**](ProjectModel.md) |  | 

## Example

```python
from obslabs_client.models.v1_list_projects200_response import V1ListProjects200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ListProjects200Response from a JSON string
v1_list_projects200_response_instance = V1ListProjects200Response.from_json(json)
# print the JSON string representation of the object
print(V1ListProjects200Response.to_json())

# convert the object into a dict
v1_list_projects200_response_dict = v1_list_projects200_response_instance.to_dict()
# create an instance of V1ListProjects200Response from a dict
v1_list_projects200_response_from_dict = V1ListProjects200Response.from_dict(v1_list_projects200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


