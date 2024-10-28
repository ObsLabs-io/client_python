# ChannelSlackModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**integration_id** | **str** |  | 

## Example

```python
from obslabs_client.models.channel_slack_model import ChannelSlackModel

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelSlackModel from a JSON string
channel_slack_model_instance = ChannelSlackModel.from_json(json)
# print the JSON string representation of the object
print(ChannelSlackModel.to_json())

# convert the object into a dict
channel_slack_model_dict = channel_slack_model_instance.to_dict()
# create an instance of ChannelSlackModel from a dict
channel_slack_model_from_dict = ChannelSlackModel.from_dict(channel_slack_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


