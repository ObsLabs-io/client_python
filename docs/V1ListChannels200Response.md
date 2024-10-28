# V1ListChannels200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**List[ChannelModel]**](ChannelModel.md) |  | 

## Example

```python
from obslabs_client.models.v1_list_channels200_response import V1ListChannels200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ListChannels200Response from a JSON string
v1_list_channels200_response_instance = V1ListChannels200Response.from_json(json)
# print the JSON string representation of the object
print(V1ListChannels200Response.to_json())

# convert the object into a dict
v1_list_channels200_response_dict = v1_list_channels200_response_instance.to_dict()
# create an instance of V1ListChannels200Response from a dict
v1_list_channels200_response_from_dict = V1ListChannels200Response.from_dict(v1_list_channels200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


