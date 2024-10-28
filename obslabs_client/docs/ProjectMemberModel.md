# ProjectMemberModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from obslabs_client.models.project_member_model import ProjectMemberModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMemberModel from a JSON string
project_member_model_instance = ProjectMemberModel.from_json(json)
# print the JSON string representation of the object
print(ProjectMemberModel.to_json())

# convert the object into a dict
project_member_model_dict = project_member_model_instance.to_dict()
# create an instance of ProjectMemberModel from a dict
project_member_model_from_dict = ProjectMemberModel.from_dict(project_member_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


