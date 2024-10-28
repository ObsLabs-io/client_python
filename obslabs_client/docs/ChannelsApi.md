# obslabs_client.ChannelsApi

All URIs are relative to *https://api.obslabs.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_create_channel**](ChannelsApi.md#v1_create_channel) | **POST** /v1/organizations/{oID}/projects/{pID}/channels | Create Channel
[**v1_delete_channel**](ChannelsApi.md#v1_delete_channel) | **DELETE** /v1/organizations/{oID}/projects/{pID}/channels/{chID} | Delete Channel
[**v1_get_channel**](ChannelsApi.md#v1_get_channel) | **GET** /v1/organizations/{oID}/projects/{pID}/channels/{chID} | Get Channel
[**v1_list_channels**](ChannelsApi.md#v1_list_channels) | **GET** /v1/organizations/{oID}/projects/{pID}/channels | List Channels
[**v1_update_channel**](ChannelsApi.md#v1_update_channel) | **PATCH** /v1/organizations/{oID}/projects/{pID}/channels/{chID} | Update Channel


# **v1_create_channel**
> V1CreateChannel201Response v1_create_channel(o_id, p_id, v1_create_channel_request=v1_create_channel_request)

Create Channel

Create Channel

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_channel201_response import V1CreateChannel201Response
from obslabs_client.models.v1_create_channel_request import V1CreateChannelRequest
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
    api_instance = obslabs_client.ChannelsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    v1_create_channel_request = obslabs_client.V1CreateChannelRequest() # V1CreateChannelRequest | Create Channel (optional)

    try:
        # Create Channel
        api_response = api_instance.v1_create_channel(o_id, p_id, v1_create_channel_request=v1_create_channel_request)
        print("The response of ChannelsApi->v1_create_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->v1_create_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **v1_create_channel_request** | [**V1CreateChannelRequest**](V1CreateChannelRequest.md)| Create Channel | [optional] 

### Return type

[**V1CreateChannel201Response**](V1CreateChannel201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create Channel |  -  |
**400** | Error Response |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_channel**
> v1_delete_channel(o_id, p_id, ch_id)

Delete Channel

Delete Channel

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
    api_instance = obslabs_client.ChannelsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    ch_id = 'ch_id_example' # str | Channel ID

    try:
        # Delete Channel
        api_instance.v1_delete_channel(o_id, p_id, ch_id)
    except Exception as e:
        print("Exception when calling ChannelsApi->v1_delete_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **ch_id** | **str**| Channel ID | 

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

# **v1_get_channel**
> V1CreateChannel201Response v1_get_channel(o_id, p_id, ch_id)

Get Channel

Get Channel

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_channel201_response import V1CreateChannel201Response
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
    api_instance = obslabs_client.ChannelsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    ch_id = 'ch_id_example' # str | Channel ID

    try:
        # Get Channel
        api_response = api_instance.v1_get_channel(o_id, p_id, ch_id)
        print("The response of ChannelsApi->v1_get_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->v1_get_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **ch_id** | **str**| Channel ID | 

### Return type

[**V1CreateChannel201Response**](V1CreateChannel201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Channel |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_channels**
> V1ListChannels200Response v1_list_channels(o_id, p_id)

List Channels

List Channels

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_list_channels200_response import V1ListChannels200Response
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
    api_instance = obslabs_client.ChannelsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID

    try:
        # List Channels
        api_response = api_instance.v1_list_channels(o_id, p_id)
        print("The response of ChannelsApi->v1_list_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->v1_list_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 

### Return type

[**V1ListChannels200Response**](V1ListChannels200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Channels |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_channel**
> V1CreateChannel201Response v1_update_channel(o_id, p_id, ch_id, v1_update_channel_request=v1_update_channel_request)

Update Channel

Update Channel

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_channel201_response import V1CreateChannel201Response
from obslabs_client.models.v1_update_channel_request import V1UpdateChannelRequest
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
    api_instance = obslabs_client.ChannelsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    ch_id = 'ch_id_example' # str | Channel ID
    v1_update_channel_request = obslabs_client.V1UpdateChannelRequest() # V1UpdateChannelRequest | Update Channel (optional)

    try:
        # Update Channel
        api_response = api_instance.v1_update_channel(o_id, p_id, ch_id, v1_update_channel_request=v1_update_channel_request)
        print("The response of ChannelsApi->v1_update_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->v1_update_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **ch_id** | **str**| Channel ID | 
 **v1_update_channel_request** | [**V1UpdateChannelRequest**](V1UpdateChannelRequest.md)| Update Channel | [optional] 

### Return type

[**V1CreateChannel201Response**](V1CreateChannel201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Channel |  -  |
**400** | Error Response |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

