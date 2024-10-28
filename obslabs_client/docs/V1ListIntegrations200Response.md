# V1ListIntegrations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integrations** | [**List[IntegrationModel]**](IntegrationModel.md) |  | 

## Example

```python
from obslabs_client.models.v1_list_integrations200_response import V1ListIntegrations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ListIntegrations200Response from a JSON string
v1_list_integrations200_response_instance = V1ListIntegrations200Response.from_json(json)
# print the JSON string representation of the object
print(V1ListIntegrations200Response.to_json())

# convert the object into a dict
v1_list_integrations200_response_dict = v1_list_integrations200_response_instance.to_dict()
# create an instance of V1ListIntegrations200Response from a dict
v1_list_integrations200_response_from_dict = V1ListIntegrations200Response.from_dict(v1_list_integrations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


