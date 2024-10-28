# ChannelWebhookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from obslabs_client.models.channel_webhook_model import ChannelWebhookModel

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelWebhookModel from a JSON string
channel_webhook_model_instance = ChannelWebhookModel.from_json(json)
# print the JSON string representation of the object
print(ChannelWebhookModel.to_json())

# convert the object into a dict
channel_webhook_model_dict = channel_webhook_model_instance.to_dict()
# create an instance of ChannelWebhookModel from a dict
channel_webhook_model_from_dict = ChannelWebhookModel.from_dict(channel_webhook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


