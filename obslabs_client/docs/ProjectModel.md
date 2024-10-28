# ProjectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**members** | [**List[ProjectMemberModel]**](ProjectMemberModel.md) |  | 

## Example

```python
from obslabs_client.models.project_model import ProjectModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectModel from a JSON string
project_model_instance = ProjectModel.from_json(json)
# print the JSON string representation of the object
print(ProjectModel.to_json())

# convert the object into a dict
project_model_dict = project_model_instance.to_dict()
# create an instance of ProjectModel from a dict
project_model_from_dict = ProjectModel.from_dict(project_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


