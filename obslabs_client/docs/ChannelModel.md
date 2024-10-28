# ChannelModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**project_id** | **str** |  | 
**emails** | [**List[ChannelEmailModel]**](ChannelEmailModel.md) |  | 
**webhooks** | [**List[ChannelWebhookModel]**](ChannelWebhookModel.md) |  | 
**slacks** | [**List[ChannelSlackModel]**](ChannelSlackModel.md) |  | 
**smss** | [**List[ChannelSmsModel]**](ChannelSmsModel.md) |  | 

## Example

```python
from obslabs_client.models.channel_model import ChannelModel

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelModel from a JSON string
channel_model_instance = ChannelModel.from_json(json)
# print the JSON string representation of the object
print(ChannelModel.to_json())

# convert the object into a dict
channel_model_dict = channel_model_instance.to_dict()
# create an instance of ChannelModel from a dict
channel_model_from_dict = ChannelModel.from_dict(channel_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


