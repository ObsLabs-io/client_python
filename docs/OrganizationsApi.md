# obslabs_client.OrganizationsApi

All URIs are relative to *https://api.obslabs.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_create_organization**](OrganizationsApi.md#v1_create_organization) | **POST** /v1/organizations | Create Organization
[**v1_delete_organization**](OrganizationsApi.md#v1_delete_organization) | **DELETE** /v1/organizations/{oID} | Delete Organization
[**v1_get_organization**](OrganizationsApi.md#v1_get_organization) | **GET** /v1/organizations/{oID} | Get Organization
[**v1_list_organizations**](OrganizationsApi.md#v1_list_organizations) | **GET** /v1/organizations | List Organizations
[**v1_organization_member_delete**](OrganizationsApi.md#v1_organization_member_delete) | **DELETE** /v1/organizations/{oID}/members/{uID} | Delete Organization Memeber
[**v1_organization_member_update**](OrganizationsApi.md#v1_organization_member_update) | **PATCH** /v1/organizations/{oID}/members/{uID} | Update Organization Member
[**v1_update_organization**](OrganizationsApi.md#v1_update_organization) | **PATCH** /v1/organizations/{oID} | Update Organization


# **v1_create_organization**
> V1CreateOrganization201Response v1_create_organization(v1_create_organization_request=v1_create_organization_request)

Create Organization

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_organization201_response import V1CreateOrganization201Response
from obslabs_client.models.v1_create_organization_request import V1CreateOrganizationRequest
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
    api_instance = obslabs_client.OrganizationsApi(api_client)
    v1_create_organization_request = obslabs_client.V1CreateOrganizationRequest() # V1CreateOrganizationRequest |  (optional)

    try:
        # Create Organization
        api_response = api_instance.v1_create_organization(v1_create_organization_request=v1_create_organization_request)
        print("The response of OrganizationsApi->v1_create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_create_organization_request** | [**V1CreateOrganizationRequest**](V1CreateOrganizationRequest.md)|  | [optional] 

### Return type

[**V1CreateOrganization201Response**](V1CreateOrganization201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create Organization |  -  |
**400** | Error Response |  -  |
**401** | Error Unauthorized  |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_organization**
> v1_delete_organization(o_id)

Delete Organization

Delete Organization

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
    api_instance = obslabs_client.OrganizationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID

    try:
        # Delete Organization
        api_instance.v1_delete_organization(o_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_delete_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 

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

# **v1_get_organization**
> V1CreateOrganization201Response v1_get_organization(o_id)

Get Organization

Get Organization

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_organization201_response import V1CreateOrganization201Response
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
    api_instance = obslabs_client.OrganizationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID

    try:
        # Get Organization
        api_response = api_instance.v1_get_organization(o_id)
        print("The response of OrganizationsApi->v1_get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 

### Return type

[**V1CreateOrganization201Response**](V1CreateOrganization201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Organization |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_organizations**
> V1ListOrganizations200Response v1_list_organizations()

List Organizations

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_list_organizations200_response import V1ListOrganizations200Response
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
    api_instance = obslabs_client.OrganizationsApi(api_client)

    try:
        # List Organizations
        api_response = api_instance.v1_list_organizations()
        print("The response of OrganizationsApi->v1_list_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_list_organizations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ListOrganizations200Response**](V1ListOrganizations200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Organizations |  -  |
**401** | Error Unauthorized  |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_organization_member_delete**
> v1_organization_member_delete(o_id, u_id)

Delete Organization Memeber

Delete Organization Member

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
    api_instance = obslabs_client.OrganizationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    u_id = 'iaI_KnKzSNxMhqwNKfvEuw' # str | User ID

    try:
        # Delete Organization Memeber
        api_instance.v1_organization_member_delete(o_id, u_id)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organization_member_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **u_id** | **str**| User ID | 

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

# **v1_organization_member_update**
> V1OrganizationMemberUpdate200Response v1_organization_member_update(o_id, u_id, v1_organization_member_update_request=v1_organization_member_update_request)

Update Organization Member

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_organization_member_update200_response import V1OrganizationMemberUpdate200Response
from obslabs_client.models.v1_organization_member_update_request import V1OrganizationMemberUpdateRequest
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
    api_instance = obslabs_client.OrganizationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    u_id = 'iaI_KnKzSNxMhqwNKfvEuw' # str | User ID
    v1_organization_member_update_request = obslabs_client.V1OrganizationMemberUpdateRequest() # V1OrganizationMemberUpdateRequest |  (optional)

    try:
        # Update Organization Member
        api_response = api_instance.v1_organization_member_update(o_id, u_id, v1_organization_member_update_request=v1_organization_member_update_request)
        print("The response of OrganizationsApi->v1_organization_member_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organization_member_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **u_id** | **str**| User ID | 
 **v1_organization_member_update_request** | [**V1OrganizationMemberUpdateRequest**](V1OrganizationMemberUpdateRequest.md)|  | [optional] 

### Return type

[**V1OrganizationMemberUpdate200Response**](V1OrganizationMemberUpdate200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Organization Member |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_organization**
> V1CreateOrganization201Response v1_update_organization(o_id, v1_update_organization_request=v1_update_organization_request)

Update Organization

Update Organization

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_organization201_response import V1CreateOrganization201Response
from obslabs_client.models.v1_update_organization_request import V1UpdateOrganizationRequest
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
    api_instance = obslabs_client.OrganizationsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    v1_update_organization_request = obslabs_client.V1UpdateOrganizationRequest() # V1UpdateOrganizationRequest |  (optional)

    try:
        # Update Organization
        api_response = api_instance.v1_update_organization(o_id, v1_update_organization_request=v1_update_organization_request)
        print("The response of OrganizationsApi->v1_update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **v1_update_organization_request** | [**V1UpdateOrganizationRequest**](V1UpdateOrganizationRequest.md)|  | [optional] 

### Return type

[**V1CreateOrganization201Response**](V1CreateOrganization201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Ogranization |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

