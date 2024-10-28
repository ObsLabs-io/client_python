# obslabs_client.InvitationsApi

All URIs are relative to *https://api.obslabs.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_accept_invitation**](InvitationsApi.md#v1_accept_invitation) | **POST** /v1/organizations/{oID}/invitations/{invID}/accept | Accept Invitation
[**v1_get_invitation**](InvitationsApi.md#v1_get_invitation) | **GET** /v1/organizations/{oID}/invitations/{invID} | Get Invitation
[**v1_list_invitations**](InvitationsApi.md#v1_list_invitations) | **GET** /v1/organizations/{oID}/invitations | List Invitations
[**v1_resend_invitation**](InvitationsApi.md#v1_resend_invitation) | **POST** /v1/organizations/{oID}/invitations/{invID}/resend | Resend Invitation
[**v1_revoke_invitation**](InvitationsApi.md#v1_revoke_invitation) | **DELETE** /v1/organizations/{oID}/invitations/{invID} | Revoke Invitation
[**v1_send_invitation**](InvitationsApi.md#v1_send_invitation) | **POST** /v1/organizations/{oID}/invitations | Send Invitation


# **v1_accept_invitation**
> v1_accept_invitation(o_id, inv_id, v1_accept_invitation_request=v1_accept_invitation_request)

Accept Invitation

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_accept_invitation_request import V1AcceptInvitationRequest
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
    api_instance = obslabs_client.InvitationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    inv_id = '2pg7EQvDIFjREnMBuRQ30Q' # str | Invitation ID
    v1_accept_invitation_request = obslabs_client.V1AcceptInvitationRequest() # V1AcceptInvitationRequest |  (optional)

    try:
        # Accept Invitation
        api_instance.v1_accept_invitation(o_id, inv_id, v1_accept_invitation_request=v1_accept_invitation_request)
    except Exception as e:
        print("Exception when calling InvitationsApi->v1_accept_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **inv_id** | **str**| Invitation ID | 
 **v1_accept_invitation_request** | [**V1AcceptInvitationRequest**](V1AcceptInvitationRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_invitation**
> V1SendInvitation201Response v1_get_invitation(o_id, inv_id)

Get Invitation

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_send_invitation201_response import V1SendInvitation201Response
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
    api_instance = obslabs_client.InvitationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    inv_id = '2pg7EQvDIFjREnMBuRQ30Q' # str | Invitation ID

    try:
        # Get Invitation
        api_response = api_instance.v1_get_invitation(o_id, inv_id)
        print("The response of InvitationsApi->v1_get_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->v1_get_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **inv_id** | **str**| Invitation ID | 

### Return type

[**V1SendInvitation201Response**](V1SendInvitation201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Error Response |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_invitations**
> V1ListInvitations200Response v1_list_invitations(o_id)

List Invitations

List Invitations

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_list_invitations200_response import V1ListInvitations200Response
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
    api_instance = obslabs_client.InvitationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID

    try:
        # List Invitations
        api_response = api_instance.v1_list_invitations(o_id)
        print("The response of InvitationsApi->v1_list_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->v1_list_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 

### Return type

[**V1ListInvitations200Response**](V1ListInvitations200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Invitations |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_resend_invitation**
> V1SendInvitation201Response v1_resend_invitation(o_id, inv_id)

Resend Invitation

Resend Invitation

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_send_invitation201_response import V1SendInvitation201Response
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
    api_instance = obslabs_client.InvitationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    inv_id = '2pg7EQvDIFjREnMBuRQ30Q' # str | Invitation ID

    try:
        # Resend Invitation
        api_response = api_instance.v1_resend_invitation(o_id, inv_id)
        print("The response of InvitationsApi->v1_resend_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->v1_resend_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **inv_id** | **str**| Invitation ID | 

### Return type

[**V1SendInvitation201Response**](V1SendInvitation201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_revoke_invitation**
> v1_revoke_invitation(o_id, inv_id)

Revoke Invitation

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
    api_instance = obslabs_client.InvitationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    inv_id = '2pg7EQvDIFjREnMBuRQ30Q' # str | Invitation ID

    try:
        # Revoke Invitation
        api_instance.v1_revoke_invitation(o_id, inv_id)
    except Exception as e:
        print("Exception when calling InvitationsApi->v1_revoke_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **inv_id** | **str**| Invitation ID | 

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

# **v1_send_invitation**
> V1SendInvitation201Response v1_send_invitation(o_id, v1_send_invitation_request=v1_send_invitation_request)

Send Invitation

Send Invitation

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_send_invitation201_response import V1SendInvitation201Response
from obslabs_client.models.v1_send_invitation_request import V1SendInvitationRequest
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
    api_instance = obslabs_client.InvitationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    v1_send_invitation_request = obslabs_client.V1SendInvitationRequest() # V1SendInvitationRequest |  (optional)

    try:
        # Send Invitation
        api_response = api_instance.v1_send_invitation(o_id, v1_send_invitation_request=v1_send_invitation_request)
        print("The response of InvitationsApi->v1_send_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->v1_send_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **v1_send_invitation_request** | [**V1SendInvitationRequest**](V1SendInvitationRequest.md)|  | [optional] 

### Return type

[**V1SendInvitation201Response**](V1SendInvitation201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Send Invitation |  -  |
**400** | Error Response |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

