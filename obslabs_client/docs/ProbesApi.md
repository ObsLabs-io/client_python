# obslabs_client.ProbesApi

All URIs are relative to *https://api.obslabs.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_create_probe**](ProbesApi.md#v1_create_probe) | **POST** /v1/organizations/{oID}/projects/{pID}/probes | Create Probe
[**v1_delete_probe**](ProbesApi.md#v1_delete_probe) | **DELETE** /v1/organizations/{oID}/projects/{pID}/probes/{prID} | Delete Probe
[**v1_get_probe**](ProbesApi.md#v1_get_probe) | **GET** /v1/organizations/{oID}/projects/{pID}/probes/{prID} | Get Probe
[**v1_list_probes**](ProbesApi.md#v1_list_probes) | **GET** /v1/organizations/{oID}/projects/{pID}/probes | List Probes
[**v1_probe_status_changes**](ProbesApi.md#v1_probe_status_changes) | **GET** /v1/organizations/{oID}/projects/{pID}/probes/{prID}/status-changes | List Probe Status Changes
[**v1_update_probe**](ProbesApi.md#v1_update_probe) | **PATCH** /v1/organizations/{oID}/projects/{pID}/probes/{prID} | Update Probe


# **v1_create_probe**
> V1CreateProbe201Response v1_create_probe(o_id, p_id, v1_create_probe_request=v1_create_probe_request)

Create Probe

Create Probe

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_probe201_response import V1CreateProbe201Response
from obslabs_client.models.v1_create_probe_request import V1CreateProbeRequest
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
    api_instance = obslabs_client.ProbesApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    v1_create_probe_request = obslabs_client.V1CreateProbeRequest() # V1CreateProbeRequest | Create Probe (optional)

    try:
        # Create Probe
        api_response = api_instance.v1_create_probe(o_id, p_id, v1_create_probe_request=v1_create_probe_request)
        print("The response of ProbesApi->v1_create_probe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProbesApi->v1_create_probe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **v1_create_probe_request** | [**V1CreateProbeRequest**](V1CreateProbeRequest.md)| Create Probe | [optional] 

### Return type

[**V1CreateProbe201Response**](V1CreateProbe201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create Probe |  -  |
**400** | Error Response |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_probe**
> v1_delete_probe(o_id, p_id, pr_id)

Delete Probe

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
    api_instance = obslabs_client.ProbesApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    pr_id = 'ECD3gsVktn1E_xuPYMlrig' # str | Probe ID

    try:
        # Delete Probe
        api_instance.v1_delete_probe(o_id, p_id, pr_id)
    except Exception as e:
        print("Exception when calling ProbesApi->v1_delete_probe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **pr_id** | **str**| Probe ID | 

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

# **v1_get_probe**
> V1CreateProbe201Response v1_get_probe(o_id, p_id, pr_id)

Get Probe

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_probe201_response import V1CreateProbe201Response
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
    api_instance = obslabs_client.ProbesApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    pr_id = 'ECD3gsVktn1E_xuPYMlrig' # str | Probe ID

    try:
        # Get Probe
        api_response = api_instance.v1_get_probe(o_id, p_id, pr_id)
        print("The response of ProbesApi->v1_get_probe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProbesApi->v1_get_probe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **pr_id** | **str**| Probe ID | 

### Return type

[**V1CreateProbe201Response**](V1CreateProbe201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Probe |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_probes**
> V1ListProbes200Response v1_list_probes(o_id, p_id)

List Probes

List probes

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_list_probes200_response import V1ListProbes200Response
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
    api_instance = obslabs_client.ProbesApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID

    try:
        # List Probes
        api_response = api_instance.v1_list_probes(o_id, p_id)
        print("The response of ProbesApi->v1_list_probes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProbesApi->v1_list_probes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 

### Return type

[**V1ListProbes200Response**](V1ListProbes200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Probes |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_probe_status_changes**
> V1ProbeStatusChanges200Response v1_probe_status_changes(o_id, p_id, pr_id, limit=limit, offset=offset)

List Probe Status Changes

List Probe Status Changes

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_probe_status_changes200_response import V1ProbeStatusChanges200Response
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
    api_instance = obslabs_client.ProbesApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    pr_id = 'ECD3gsVktn1E_xuPYMlrig' # str | Probe ID
    limit = 100 # int | Response items limit (optional) (default to 100)
    offset = 0 # int | Response items offset (optional) (default to 0)

    try:
        # List Probe Status Changes
        api_response = api_instance.v1_probe_status_changes(o_id, p_id, pr_id, limit=limit, offset=offset)
        print("The response of ProbesApi->v1_probe_status_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProbesApi->v1_probe_status_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **pr_id** | **str**| Probe ID | 
 **limit** | **int**| Response items limit | [optional] [default to 100]
 **offset** | **int**| Response items offset | [optional] [default to 0]

### Return type

[**V1ProbeStatusChanges200Response**](V1ProbeStatusChanges200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Probe Status Changes |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_probe**
> V1CreateProbe201Response v1_update_probe(o_id, p_id, pr_id, v1_update_probe_request=v1_update_probe_request)

Update Probe

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_probe201_response import V1CreateProbe201Response
from obslabs_client.models.v1_update_probe_request import V1UpdateProbeRequest
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
    api_instance = obslabs_client.ProbesApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    pr_id = 'ECD3gsVktn1E_xuPYMlrig' # str | Probe ID
    v1_update_probe_request = obslabs_client.V1UpdateProbeRequest() # V1UpdateProbeRequest | Update Probe (optional)

    try:
        # Update Probe
        api_response = api_instance.v1_update_probe(o_id, p_id, pr_id, v1_update_probe_request=v1_update_probe_request)
        print("The response of ProbesApi->v1_update_probe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProbesApi->v1_update_probe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **pr_id** | **str**| Probe ID | 
 **v1_update_probe_request** | [**V1UpdateProbeRequest**](V1UpdateProbeRequest.md)| Update Probe | [optional] 

### Return type

[**V1CreateProbe201Response**](V1CreateProbe201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Probe |  -  |
**400** | Error Response |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

