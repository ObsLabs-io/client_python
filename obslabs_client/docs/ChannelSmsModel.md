# ChannelSmsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from obslabs_client.models.channel_sms_model import ChannelSmsModel

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelSmsModel from a JSON string
channel_sms_model_instance = ChannelSmsModel.from_json(json)
# print the JSON string representation of the object
print(ChannelSmsModel.to_json())

# convert the object into a dict
channel_sms_model_dict = channel_sms_model_instance.to_dict()
# create an instance of ChannelSmsModel from a dict
channel_sms_model_from_dict = ChannelSmsModel.from_dict(channel_sms_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


