# ProbeScheduleModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**failure_threshold** | **int** |  | [default to 1]
**success_threshold** | **int** |  | [default to 1]
**expression** | **str** | Required if type is \&quot;cron\&quot; | [optional] 
**period_seconds** | **int** | Required if type is \&quot;period\&quot; | [optional] [default to 360]

## Example

```python
from obslabs_client.models.probe_schedule_model import ProbeScheduleModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeScheduleModel from a JSON string
probe_schedule_model_instance = ProbeScheduleModel.from_json(json)
# print the JSON string representation of the object
print(ProbeScheduleModel.to_json())

# convert the object into a dict
probe_schedule_model_dict = probe_schedule_model_instance.to_dict()
# create an instance of ProbeScheduleModel from a dict
probe_schedule_model_from_dict = ProbeScheduleModel.from_dict(probe_schedule_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


