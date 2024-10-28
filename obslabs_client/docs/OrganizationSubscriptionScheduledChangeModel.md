# OrganizationSubscriptionScheduledChangeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**effective_at** | **datetime** |  | 
**resume_at** | **datetime** |  | [optional] 

## Example

```python
from obslabs_client.models.organization_subscription_scheduled_change_model import OrganizationSubscriptionScheduledChangeModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSubscriptionScheduledChangeModel from a JSON string
organization_subscription_scheduled_change_model_instance = OrganizationSubscriptionScheduledChangeModel.from_json(json)
# print the JSON string representation of the object
print(OrganizationSubscriptionScheduledChangeModel.to_json())

# convert the object into a dict
organization_subscription_scheduled_change_model_dict = organization_subscription_scheduled_change_model_instance.to_dict()
# create an instance of OrganizationSubscriptionScheduledChangeModel from a dict
organization_subscription_scheduled_change_model_from_dict = OrganizationSubscriptionScheduledChangeModel.from_dict(organization_subscription_scheduled_change_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


