# OrganizationUsageModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhooks** | **int** |  | 
**emails** | **int** |  | 
**slack** | **int** |  | 
**sms** | **int** |  | 

## Example

```python
from obslabs_client.models.organization_usage_model import OrganizationUsageModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUsageModel from a JSON string
organization_usage_model_instance = OrganizationUsageModel.from_json(json)
# print the JSON string representation of the object
print(OrganizationUsageModel.to_json())

# convert the object into a dict
organization_usage_model_dict = organization_usage_model_instance.to_dict()
# create an instance of OrganizationUsageModel from a dict
organization_usage_model_from_dict = OrganizationUsageModel.from_dict(organization_usage_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


