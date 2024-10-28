# V1UpdateChannelRequestWebhooksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from obslabs_client.models.v1_update_channel_request_webhooks_inner import V1UpdateChannelRequestWebhooksInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1UpdateChannelRequestWebhooksInner from a JSON string
v1_update_channel_request_webhooks_inner_instance = V1UpdateChannelRequestWebhooksInner.from_json(json)
# print the JSON string representation of the object
print(V1UpdateChannelRequestWebhooksInner.to_json())

# convert the object into a dict
v1_update_channel_request_webhooks_inner_dict = v1_update_channel_request_webhooks_inner_instance.to_dict()
# create an instance of V1UpdateChannelRequestWebhooksInner from a dict
v1_update_channel_request_webhooks_inner_from_dict = V1UpdateChannelRequestWebhooksInner.from_dict(v1_update_channel_request_webhooks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


