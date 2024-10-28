# OrganizationMemberModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from obslabs_client.models.organization_member_model import OrganizationMemberModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMemberModel from a JSON string
organization_member_model_instance = OrganizationMemberModel.from_json(json)
# print the JSON string representation of the object
print(OrganizationMemberModel.to_json())

# convert the object into a dict
organization_member_model_dict = organization_member_model_instance.to_dict()
# create an instance of OrganizationMemberModel from a dict
organization_member_model_from_dict = OrganizationMemberModel.from_dict(organization_member_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


