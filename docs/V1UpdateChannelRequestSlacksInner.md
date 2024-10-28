# V1UpdateChannelRequestSlacksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**integration_id** | **str** |  | 

## Example

```python
from obslabs_client.models.v1_update_channel_request_slacks_inner import V1UpdateChannelRequestSlacksInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1UpdateChannelRequestSlacksInner from a JSON string
v1_update_channel_request_slacks_inner_instance = V1UpdateChannelRequestSlacksInner.from_json(json)
# print the JSON string representation of the object
print(V1UpdateChannelRequestSlacksInner.to_json())

# convert the object into a dict
v1_update_channel_request_slacks_inner_dict = v1_update_channel_request_slacks_inner_instance.to_dict()
# create an instance of V1UpdateChannelRequestSlacksInner from a dict
v1_update_channel_request_slacks_inner_from_dict = V1UpdateChannelRequestSlacksInner.from_dict(v1_update_channel_request_slacks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


