# UserOrganizationRoleModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from obslabs_client.models.user_organization_role_model import UserOrganizationRoleModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserOrganizationRoleModel from a JSON string
user_organization_role_model_instance = UserOrganizationRoleModel.from_json(json)
# print the JSON string representation of the object
print(UserOrganizationRoleModel.to_json())

# convert the object into a dict
user_organization_role_model_dict = user_organization_role_model_instance.to_dict()
# create an instance of UserOrganizationRoleModel from a dict
user_organization_role_model_from_dict = UserOrganizationRoleModel.from_dict(user_organization_role_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


