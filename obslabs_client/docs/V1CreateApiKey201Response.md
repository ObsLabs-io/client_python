# V1CreateApiKey201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | [**ApiKeyModel**](ApiKeyModel.md) |  | 

## Example

```python
from obslabs_client.models.v1_create_api_key201_response import V1CreateApiKey201Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateApiKey201Response from a JSON string
v1_create_api_key201_response_instance = V1CreateApiKey201Response.from_json(json)
# print the JSON string representation of the object
print(V1CreateApiKey201Response.to_json())

# convert the object into a dict
v1_create_api_key201_response_dict = v1_create_api_key201_response_instance.to_dict()
# create an instance of V1CreateApiKey201Response from a dict
v1_create_api_key201_response_from_dict = V1CreateApiKey201Response.from_dict(v1_create_api_key201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


