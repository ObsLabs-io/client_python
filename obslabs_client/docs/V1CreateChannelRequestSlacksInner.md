# V1CreateChannelRequestSlacksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**integration_id** | **str** |  | 

## Example

```python
from obslabs_client.models.v1_create_channel_request_slacks_inner import V1CreateChannelRequestSlacksInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1CreateChannelRequestSlacksInner from a JSON string
v1_create_channel_request_slacks_inner_instance = V1CreateChannelRequestSlacksInner.from_json(json)
# print the JSON string representation of the object
print(V1CreateChannelRequestSlacksInner.to_json())

# convert the object into a dict
v1_create_channel_request_slacks_inner_dict = v1_create_channel_request_slacks_inner_instance.to_dict()
# create an instance of V1CreateChannelRequestSlacksInner from a dict
v1_create_channel_request_slacks_inner_from_dict = V1CreateChannelRequestSlacksInner.from_dict(v1_create_channel_request_slacks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


