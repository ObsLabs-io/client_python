# IntegrationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**slack** | [**IntegrationSlackModel**](IntegrationSlackModel.md) |  | [optional] 

## Example

```python
from obslabs_client.models.integration_model import IntegrationModel

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationModel from a JSON string
integration_model_instance = IntegrationModel.from_json(json)
# print the JSON string representation of the object
print(IntegrationModel.to_json())

# convert the object into a dict
integration_model_dict = integration_model_instance.to_dict()
# create an instance of IntegrationModel from a dict
integration_model_from_dict = IntegrationModel.from_dict(integration_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


