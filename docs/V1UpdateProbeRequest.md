# V1UpdateProbeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** | Only pull probes can have updated URL | [optional] 
**schedule** | [**ProbeScheduleModel**](.md) |  | [optional] 
**channels** | **List[str]** |  | [optional] 

## Example

```python
from obslabs_client.models.v1_update_probe_request import V1UpdateProbeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UpdateProbeRequest from a JSON string
v1_update_probe_request_instance = V1UpdateProbeRequest.from_json(json)
# print the JSON string representation of the object
print(V1UpdateProbeRequest.to_json())

# convert the object into a dict
v1_update_probe_request_dict = v1_update_probe_request_instance.to_dict()
# create an instance of V1UpdateProbeRequest from a dict
v1_update_probe_request_from_dict = V1UpdateProbeRequest.from_dict(v1_update_probe_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


