# obslabs_client.IntegrationsApi

All URIs are relative to *https://api.obslabs.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_delete_integrations**](IntegrationsApi.md#v1_delete_integrations) | **DELETE** /v1/organizations/{oID}/projects/{pID}/integrations/{intID} | Delete Integration
[**v1_list_integrations**](IntegrationsApi.md#v1_list_integrations) | **GET** /v1/organizations/{oID}/projects/{pID}/integrations | List Integrations


# **v1_delete_integrations**
> v1_delete_integrations(o_id, p_id, int_id)

Delete Integration

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
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
    api_instance = obslabs_client.IntegrationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    int_id = 'int_id_example' # str | Integration ID

    try:
        # Delete Integration
        api_instance.v1_delete_integrations(o_id, p_id, int_id)
    except Exception as e:
        print("Exception when calling IntegrationsApi->v1_delete_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **int_id** | **str**| Integration ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_integrations**
> V1ListIntegrations200Response v1_list_integrations(o_id, p_id)

List Integrations

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_list_integrations200_response import V1ListIntegrations200Response
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
    api_instance = obslabs_client.IntegrationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID

    try:
        # List Integrations
        api_response = api_instance.v1_list_integrations(o_id, p_id)
        print("The response of IntegrationsApi->v1_list_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->v1_list_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 

### Return type

[**V1ListIntegrations200Response**](V1ListIntegrations200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Integrations |  -  |
**401** | Error Unauthorized  |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

