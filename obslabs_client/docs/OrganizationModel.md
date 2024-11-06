# OrganizationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**is_trial** | **bool** |  | 
**trial_ends_at** | **datetime** |  | [optional] 
**members** | [**List[OrganizationMemberModel]**](OrganizationMemberModel.md) |  | 
**projects** | [**List[OrganizationProjectModel]**](OrganizationProjectModel.md) |  | 
**subscription** | [**OrganizationSubscriptionModel**](.md) |  | [optional] 
**period_usage** | [**OrganizationUsageModel**](OrganizationUsageModel.md) |  | 

## Example

```python
from obslabs_client.models.organization_model import OrganizationModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationModel from a JSON string
organization_model_instance = OrganizationModel.from_json(json)
# print the JSON string representation of the object
print(OrganizationModel.to_json())

# convert the object into a dict
organization_model_dict = organization_model_instance.to_dict()
# create an instance of OrganizationModel from a dict
organization_model_from_dict = OrganizationModel.from_dict(organization_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


