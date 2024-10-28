# V1ListInvitations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitations** | [**List[InvitationModel]**](InvitationModel.md) |  | 

## Example

```python
from obslabs_client.models.v1_list_invitations200_response import V1ListInvitations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ListInvitations200Response from a JSON string
v1_list_invitations200_response_instance = V1ListInvitations200Response.from_json(json)
# print the JSON string representation of the object
print(V1ListInvitations200Response.to_json())

# convert the object into a dict
v1_list_invitations200_response_dict = v1_list_invitations200_response_instance.to_dict()
# create an instance of V1ListInvitations200Response from a dict
v1_list_invitations200_response_from_dict = V1ListInvitations200Response.from_dict(v1_list_invitations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


