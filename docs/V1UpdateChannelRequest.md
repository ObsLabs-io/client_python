# V1UpdateChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**emails** | [**List[V1UpdateChannelRequestEmailsInner]**](V1UpdateChannelRequestEmailsInner.md) |  | [optional] 
**webhooks** | [**List[V1UpdateChannelRequestWebhooksInner]**](V1UpdateChannelRequestWebhooksInner.md) |  | [optional] 
**slacks** | [**List[V1UpdateChannelRequestSlacksInner]**](V1UpdateChannelRequestSlacksInner.md) |  | [optional] 
**smss** | [**List[V1UpdateChannelRequestSmssInner]**](V1UpdateChannelRequestSmssInner.md) |  | [optional] 

## Example

```python
from obslabs_client.models.v1_update_channel_request import V1UpdateChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UpdateChannelRequest from a JSON string
v1_update_channel_request_instance = V1UpdateChannelRequest.from_json(json)
# print the JSON string representation of the object
print(V1UpdateChannelRequest.to_json())

# convert the object into a dict
v1_update_channel_request_dict = v1_update_channel_request_instance.to_dict()
# create an instance of V1UpdateChannelRequest from a dict
v1_update_channel_request_from_dict = V1UpdateChannelRequest.from_dict(v1_update_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


