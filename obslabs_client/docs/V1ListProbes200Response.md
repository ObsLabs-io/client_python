# V1ListProbes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probes** | [**List[ProbeModel]**](ProbeModel.md) |  | 

## Example

```python
from obslabs_client.models.v1_list_probes200_response import V1ListProbes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ListProbes200Response from a JSON string
v1_list_probes200_response_instance = V1ListProbes200Response.from_json(json)
# print the JSON string representation of the object
print(V1ListProbes200Response.to_json())

# convert the object into a dict
v1_list_probes200_response_dict = v1_list_probes200_response_instance.to_dict()
# create an instance of V1ListProbes200Response from a dict
v1_list_probes200_response_from_dict = V1ListProbes200Response.from_dict(v1_list_probes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


