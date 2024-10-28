# OrganizationSubscriptionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**plan** | **str** |  | 
**status** | **str** |  | 
**next_billed_at** | **datetime** |  | [optional] 
**scheduled_change** | [**OrganizationSubscriptionScheduledChangeModel**](OrganizationSubscriptionScheduledChangeModel.md) |  | [optional] 
**paddle_customer_id** | **str** |  | 

## Example

```python
from obslabs_client.models.organization_subscription_model import OrganizationSubscriptionModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSubscriptionModel from a JSON string
organization_subscription_model_instance = OrganizationSubscriptionModel.from_json(json)
# print the JSON string representation of the object
print(OrganizationSubscriptionModel.to_json())

# convert the object into a dict
organization_subscription_model_dict = organization_subscription_model_instance.to_dict()
# create an instance of OrganizationSubscriptionModel from a dict
organization_subscription_model_from_dict = OrganizationSubscriptionModel.from_dict(organization_subscription_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


