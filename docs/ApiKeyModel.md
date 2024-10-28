# ApiKeyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**last_used** | **datetime** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from obslabs_client.models.api_key_model import ApiKeyModel

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyModel from a JSON string
api_key_model_instance = ApiKeyModel.from_json(json)
# print the JSON string representation of the object
print(ApiKeyModel.to_json())

# convert the object into a dict
api_key_model_dict = api_key_model_instance.to_dict()
# create an instance of ApiKeyModel from a dict
api_key_model_from_dict = ApiKeyModel.from_dict(api_key_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


