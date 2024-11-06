# obslabs_client.AccountApi

All URIs are relative to *https://api.obslabs.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_my_account**](AccountApi.md#v1_my_account) | **GET** /v1/account | My Account


# **v1_my_account**
> V1MyAccount200Response v1_my_account()

My Account

My account

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_my_account200_response import V1MyAccount200Response
from obslabs_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.obslabs.io
# See configuration.py for a list of all supported configuration parameters.
configuration = obslabs_client.Configuration(
    host = "https://api.obslabs.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = obslabs_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with obslabs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = obslabs_client.AccountApi(api_client)

    try:
        # My Account
        api_response = api_instance.v1_my_account()
        print("The response of AccountApi->v1_my_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->v1_my_account: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1MyAccount200Response**](V1MyAccount200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | My account info |  -  |
**401** | Error Unauthorized  |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

