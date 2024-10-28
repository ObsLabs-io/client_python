# IntegrationSlackModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | 
**team_name** | **str** |  | 
**channel_id** | **str** |  | 
**channel** | **str** |  | 

## Example

```python
from obslabs_client.models.integration_slack_model import IntegrationSlackModel

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationSlackModel from a JSON string
integration_slack_model_instance = IntegrationSlackModel.from_json(json)
# print the JSON string representation of the object
print(IntegrationSlackModel.to_json())

# convert the object into a dict
integration_slack_model_dict = integration_slack_model_instance.to_dict()
# create an instance of IntegrationSlackModel from a dict
integration_slack_model_from_dict = IntegrationSlackModel.from_dict(integration_slack_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


