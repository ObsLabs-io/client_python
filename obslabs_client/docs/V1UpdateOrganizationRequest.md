# V1UpdateOrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from obslabs_client.models.v1_update_organization_request import V1UpdateOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UpdateOrganizationRequest from a JSON string
v1_update_organization_request_instance = V1UpdateOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(V1UpdateOrganizationRequest.to_json())

# convert the object into a dict
v1_update_organization_request_dict = v1_update_organization_request_instance.to_dict()
# create an instance of V1UpdateOrganizationRequest from a dict
v1_update_organization_request_from_dict = V1UpdateOrganizationRequest.from_dict(v1_update_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


