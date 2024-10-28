# InvitationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**status** | **str** |  | 
**role** | **str** |  | 
**sent_at** | **datetime** |  | 

## Example

```python
from obslabs_client.models.invitation_model import InvitationModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationModel from a JSON string
invitation_model_instance = InvitationModel.from_json(json)
# print the JSON string representation of the object
print(InvitationModel.to_json())

# convert the object into a dict
invitation_model_dict = invitation_model_instance.to_dict()
# create an instance of InvitationModel from a dict
invitation_model_from_dict = InvitationModel.from_dict(invitation_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


