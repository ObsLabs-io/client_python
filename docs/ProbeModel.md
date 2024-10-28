# ProbeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**url** | **str** |  | 
**status** | **str** |  | 
**status_checked_at** | **datetime** |  | 
**status_changed_at** | **datetime** |  | 
**schedule** | [**ProbeScheduleModel**](.md) |  | 
**channels** | [**List[ProbeChannelModel]**](ProbeChannelModel.md) |  | 

## Example

```python
from obslabs_client.models.probe_model import ProbeModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeModel from a JSON string
probe_model_instance = ProbeModel.from_json(json)
# print the JSON string representation of the object
print(ProbeModel.to_json())

# convert the object into a dict
probe_model_dict = probe_model_instance.to_dict()
# create an instance of ProbeModel from a dict
probe_model_from_dict = ProbeModel.from_dict(probe_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


