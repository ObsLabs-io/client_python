# V1CreateChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**emails** | [**List[V1CreateChannelRequestEmailsInner]**](V1CreateChannelRequestEmailsInner.md) |  | [optional] 
**webhooks** | [**List[V1CreateChannelRequestWebhooksInner]**](V1CreateChannelRequestWebhooksInner.md) |  | [optional] 
**slacks** | [**List[V1CreateChannelRequestSlacksInner]**](V1CreateChannelRequestSlacksInner.md) |  | [optional] 
**smss** | [**List[V1CreateChannelRequestSmssInner]**](V1CreateChannelRequestSmssInner.md) |  | [optional] 

## Example

```python
from obslabs_client.models.v1_create_channel_request import V1CreateChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateChannelRequest from a JSON string
v1_create_channel_request_instance = V1CreateChannelRequest.from_json(json)
# print the JSON string representation of the object
print(V1CreateChannelRequest.to_json())

# convert the object into a dict
v1_create_channel_request_dict = v1_create_channel_request_instance.to_dict()
# create an instance of V1CreateChannelRequest from a dict
v1_create_channel_request_from_dict = V1CreateChannelRequest.from_dict(v1_create_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


