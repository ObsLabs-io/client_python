# UserProjectRoleModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from obslabs_client.models.user_project_role_model import UserProjectRoleModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserProjectRoleModel from a JSON string
user_project_role_model_instance = UserProjectRoleModel.from_json(json)
# print the JSON string representation of the object
print(UserProjectRoleModel.to_json())

# convert the object into a dict
user_project_role_model_dict = user_project_role_model_instance.to_dict()
# create an instance of UserProjectRoleModel from a dict
user_project_role_model_from_dict = UserProjectRoleModel.from_dict(user_project_role_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


