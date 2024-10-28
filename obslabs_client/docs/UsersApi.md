# obslabs_client.UsersApi

All URIs are relative to *https://api.obslabs.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_my_user**](UsersApi.md#v1_my_user) | **GET** /v1/users/me | My User


# **v1_my_user**
> V1MyUser200Response v1_my_user()

My User

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_my_user200_response import V1MyUser200Response
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
    api_instance = obslabs_client.UsersApi(api_client)

    try:
        # My User
        api_response = api_instance.v1_my_user()
        print("The response of UsersApi->v1_my_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v1_my_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1MyUser200Response**](V1MyUser200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get User. |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

