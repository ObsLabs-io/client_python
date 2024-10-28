# OrganizationProjectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from obslabs_client.models.organization_project_model import OrganizationProjectModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationProjectModel from a JSON string
organization_project_model_instance = OrganizationProjectModel.from_json(json)
# print the JSON string representation of the object
print(OrganizationProjectModel.to_json())

# convert the object into a dict
organization_project_model_dict = organization_project_model_instance.to_dict()
# create an instance of OrganizationProjectModel from a dict
organization_project_model_from_dict = OrganizationProjectModel.from_dict(organization_project_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


