# ChannelEmailModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from obslabs_client.models.channel_email_model import ChannelEmailModel

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelEmailModel from a JSON string
channel_email_model_instance = ChannelEmailModel.from_json(json)
# print the JSON string representation of the object
print(ChannelEmailModel.to_json())

# convert the object into a dict
channel_email_model_dict = channel_email_model_instance.to_dict()
# create an instance of ChannelEmailModel from a dict
channel_email_model_from_dict = ChannelEmailModel.from_dict(channel_email_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


