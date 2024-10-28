# ErrorDetailModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**issue** | **str** |  | 

## Example

```python
from obslabs_client.models.error_detail_model import ErrorDetailModel

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetailModel from a JSON string
error_detail_model_instance = ErrorDetailModel.from_json(json)
# print the JSON string representation of the object
print(ErrorDetailModel.to_json())

# convert the object into a dict
error_detail_model_dict = error_detail_model_instance.to_dict()
# create an instance of ErrorDetailModel from a dict
error_detail_model_from_dict = ErrorDetailModel.from_dict(error_detail_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


