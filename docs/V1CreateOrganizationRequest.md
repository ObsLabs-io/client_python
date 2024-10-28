# V1CreateOrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from obslabs_client.models.v1_create_organization_request import V1CreateOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateOrganizationRequest from a JSON string
v1_create_organization_request_instance = V1CreateOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(V1CreateOrganizationRequest.to_json())

# convert the object into a dict
v1_create_organization_request_dict = v1_create_organization_request_instance.to_dict()
# create an instance of V1CreateOrganizationRequest from a dict
v1_create_organization_request_from_dict = V1CreateOrganizationRequest.from_dict(v1_create_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


