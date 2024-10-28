# V1AcceptInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **str** |  | 

## Example

```python
from obslabs_client.models.v1_accept_invitation_request import V1AcceptInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AcceptInvitationRequest from a JSON string
v1_accept_invitation_request_instance = V1AcceptInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(V1AcceptInvitationRequest.to_json())

# convert the object into a dict
v1_accept_invitation_request_dict = v1_accept_invitation_request_instance.to_dict()
# create an instance of V1AcceptInvitationRequest from a dict
v1_accept_invitation_request_from_dict = V1AcceptInvitationRequest.from_dict(v1_accept_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


