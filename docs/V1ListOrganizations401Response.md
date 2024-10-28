# V1ListOrganizations401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorModel**](ErrorModel.md) |  | 

## Example

```python
from obslabs_client.models.v1_list_organizations401_response import V1ListOrganizations401Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ListOrganizations401Response from a JSON string
v1_list_organizations401_response_instance = V1ListOrganizations401Response.from_json(json)
# print the JSON string representation of the object
print(V1ListOrganizations401Response.to_json())

# convert the object into a dict
v1_list_organizations401_response_dict = v1_list_organizations401_response_instance.to_dict()
# create an instance of V1ListOrganizations401Response from a dict
v1_list_organizations401_response_from_dict = V1ListOrganizations401Response.from_dict(v1_list_organizations401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


