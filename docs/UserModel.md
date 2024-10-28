# UserModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**organizations_role** | [**List[UserOrganizationRoleModel]**](UserOrganizationRoleModel.md) |  | 
**projects_role** | [**List[UserProjectRoleModel]**](UserProjectRoleModel.md) |  | 

## Example

```python
from obslabs_client.models.user_model import UserModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserModel from a JSON string
user_model_instance = UserModel.from_json(json)
# print the JSON string representation of the object
print(UserModel.to_json())

# convert the object into a dict
user_model_dict = user_model_instance.to_dict()
# create an instance of UserModel from a dict
user_model_from_dict = UserModel.from_dict(user_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


