# V1CreateChannelRequestSmssInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from obslabs_client.models.v1_create_channel_request_smss_inner import V1CreateChannelRequestSmssInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateChannelRequestSmssInner from a JSON string
v1_create_channel_request_smss_inner_instance = V1CreateChannelRequestSmssInner.from_json(json)
# print the JSON string representation of the object
print(V1CreateChannelRequestSmssInner.to_json())

# convert the object into a dict
v1_create_channel_request_smss_inner_dict = v1_create_channel_request_smss_inner_instance.to_dict()
# create an instance of V1CreateChannelRequestSmssInner from a dict
v1_create_channel_request_smss_inner_from_dict = V1CreateChannelRequestSmssInner.from_dict(v1_create_channel_request_smss_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


