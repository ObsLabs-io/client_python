# V1SendInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from obslabs_client.models.v1_send_invitation_request import V1SendInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SendInvitationRequest from a JSON string
v1_send_invitation_request_instance = V1SendInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(V1SendInvitationRequest.to_json())

# convert the object into a dict
v1_send_invitation_request_dict = v1_send_invitation_request_instance.to_dict()
# create an instance of V1SendInvitationRequest from a dict
v1_send_invitation_request_from_dict = V1SendInvitationRequest.from_dict(v1_send_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


