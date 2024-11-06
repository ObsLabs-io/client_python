# ProbeStatusChangeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**probe_id** | **str** |  | 
**new_status** | [**ProbeStatusModel**](ProbeStatusModel.md) |  | 
**prev_status** | [**ProbeStatusModel**](ProbeStatusModel.md) |  | 
**changed_at** | **datetime** |  | 

## Example

```python
from obslabs_client.models.probe_status_change_model import ProbeStatusChangeModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeStatusChangeModel from a JSON string
probe_status_change_model_instance = ProbeStatusChangeModel.from_json(json)
# print the JSON string representation of the object
print(ProbeStatusChangeModel.to_json())

# convert the object into a dict
probe_status_change_model_dict = probe_status_change_model_instance.to_dict()
# create an instance of ProbeStatusChangeModel from a dict
probe_status_change_model_from_dict = ProbeStatusChangeModel.from_dict(probe_status_change_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


