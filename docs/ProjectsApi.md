# obslabs_client.ProjectsApi

All URIs are relative to *https://api.obslabs.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_create_project**](ProjectsApi.md#v1_create_project) | **POST** /v1/organizations/{oID}/projects | Create Project
[**v1_delete_project**](ProjectsApi.md#v1_delete_project) | **DELETE** /v1/organizations/{oID}/projects/{pID} | Delete Project
[**v1_get_project**](ProjectsApi.md#v1_get_project) | **GET** /v1/organizations/{oID}/projects/{pID} | Get Project
[**v1_list_projects**](ProjectsApi.md#v1_list_projects) | **GET** /v1/organizations/{oID}/projects | List Projects
[**v1_project_member_create**](ProjectsApi.md#v1_project_member_create) | **POST** /v1/organizations/{oID}/projects/{pID}/members | Add Project Member
[**v1_project_member_delete**](ProjectsApi.md#v1_project_member_delete) | **DELETE** /v1/organizations/{oID}/projects/{pID}/members/{uID} | Delete Project Member
[**v1_project_member_update**](ProjectsApi.md#v1_project_member_update) | **PATCH** /v1/organizations/{oID}/projects/{pID}/members/{uID} | Update Project Member
[**v1_update_project**](ProjectsApi.md#v1_update_project) | **PATCH** /v1/organizations/{oID}/projects/{pID} | Update Project


# **v1_create_project**
> V1CreateProject201Response v1_create_project(o_id, v1_create_project_request=v1_create_project_request)

Create Project

Create Project

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_project201_response import V1CreateProject201Response
from obslabs_client.models.v1_create_project_request import V1CreateProjectRequest
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
    api_instance = obslabs_client.ProjectsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    v1_create_project_request = obslabs_client.V1CreateProjectRequest() # V1CreateProjectRequest |  (optional)

    try:
        # Create Project
        api_response = api_instance.v1_create_project(o_id, v1_create_project_request=v1_create_project_request)
        print("The response of ProjectsApi->v1_create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->v1_create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **v1_create_project_request** | [**V1CreateProjectRequest**](V1CreateProjectRequest.md)|  | [optional] 

### Return type

[**V1CreateProject201Response**](V1CreateProject201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create Project |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_project**
> v1_delete_project(o_id, p_id)

Delete Project

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
    api_instance = obslabs_client.ProjectsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID

    try:
        # Delete Project
        api_instance.v1_delete_project(o_id, p_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->v1_delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 

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

# **v1_get_project**
> V1CreateProject201Response v1_get_project(o_id, p_id)

Get Project

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_create_project201_response import V1CreateProject201Response
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
    api_instance = obslabs_client.ProjectsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID

    try:
        # Get Project
        api_response = api_instance.v1_get_project(o_id, p_id)
        print("The response of ProjectsApi->v1_get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->v1_get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 

### Return type

[**V1CreateProject201Response**](V1CreateProject201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Project |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_projects**
> V1ListProjects200Response v1_list_projects(o_id)

List Projects

List Projects

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_list_projects200_response import V1ListProjects200Response
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
    api_instance = obslabs_client.ProjectsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID

    try:
        # List Projects
        api_response = api_instance.v1_list_projects(o_id)
        print("The response of ProjectsApi->v1_list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->v1_list_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 

### Return type

[**V1ListProjects200Response**](V1ListProjects200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Projects |  -  |
**401** | Error Unauthorized  |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_project_member_create**
> V1ProjectMemberCreate200Response v1_project_member_create(o_id, p_id, v1_project_member_create_request=v1_project_member_create_request)

Add Project Member

Add Organization Member to Project

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_project_member_create200_response import V1ProjectMemberCreate200Response
from obslabs_client.models.v1_project_member_create_request import V1ProjectMemberCreateRequest
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
    api_instance = obslabs_client.ProjectsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    v1_project_member_create_request = obslabs_client.V1ProjectMemberCreateRequest() # V1ProjectMemberCreateRequest |  (optional)

    try:
        # Add Project Member
        api_response = api_instance.v1_project_member_create(o_id, p_id, v1_project_member_create_request=v1_project_member_create_request)
        print("The response of ProjectsApi->v1_project_member_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->v1_project_member_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **v1_project_member_create_request** | [**V1ProjectMemberCreateRequest**](V1ProjectMemberCreateRequest.md)|  | [optional] 

### Return type

[**V1ProjectMemberCreate200Response**](V1ProjectMemberCreate200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add Project Member Response |  -  |
**400** | Error Response |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_project_member_delete**
> v1_project_member_delete(o_id, p_id, u_id)

Delete Project Member

Delete Project Member

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
    api_instance = obslabs_client.ProjectsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    u_id = 'iaI_KnKzSNxMhqwNKfvEuw' # str | User ID

    try:
        # Delete Project Member
        api_instance.v1_project_member_delete(o_id, p_id, u_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->v1_project_member_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
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

# **v1_project_member_update**
> V1ProjectMemberCreate200Response v1_project_member_update(o_id, p_id, u_id, v1_project_member_update_request=v1_project_member_update_request)

Update Project Member

Update Project Member

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_project_member_create200_response import V1ProjectMemberCreate200Response
from obslabs_client.models.v1_project_member_update_request import V1ProjectMemberUpdateRequest
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
    api_instance = obslabs_client.ProjectsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    u_id = 'iaI_KnKzSNxMhqwNKfvEuw' # str | User ID
    v1_project_member_update_request = obslabs_client.V1ProjectMemberUpdateRequest() # V1ProjectMemberUpdateRequest |  (optional)

    try:
        # Update Project Member
        api_response = api_instance.v1_project_member_update(o_id, p_id, u_id, v1_project_member_update_request=v1_project_member_update_request)
        print("The response of ProjectsApi->v1_project_member_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->v1_project_member_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **u_id** | **str**| User ID | 
 **v1_project_member_update_request** | [**V1ProjectMemberUpdateRequest**](V1ProjectMemberUpdateRequest.md)|  | [optional] 

### Return type

[**V1ProjectMemberCreate200Response**](V1ProjectMemberCreate200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Project Member Response |  -  |
**400** | Error Response |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_project**
> V1UpdateProject200Response v1_update_project(o_id, p_id, v1_update_project_request=v1_update_project_request)

Update Project

### Example

* Basic Authentication (basicAuth):

```python
import obslabs_client
from obslabs_client.models.v1_update_project200_response import V1UpdateProject200Response
from obslabs_client.models.v1_update_project_request import V1UpdateProjectRequest
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
    api_instance = obslabs_client.ProjectsApi(api_client)
    o_id = 'NTz6OnG_yqlm_0qUmjHJjg' # str | Organization ID
    p_id = '1_g7EQvDIFjREnMBuRQ30Q' # str | Project ID
    v1_update_project_request = obslabs_client.V1UpdateProjectRequest() # V1UpdateProjectRequest | Update Project (optional)

    try:
        # Update Project
        api_response = api_instance.v1_update_project(o_id, p_id, v1_update_project_request=v1_update_project_request)
        print("The response of ProjectsApi->v1_update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->v1_update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_id** | **str**| Organization ID | 
 **p_id** | **str**| Project ID | 
 **v1_update_project_request** | [**V1UpdateProjectRequest**](V1UpdateProjectRequest.md)| Update Project | [optional] 

### Return type

[**V1UpdateProject200Response**](V1UpdateProject200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Project |  -  |
**401** | Error Unauthorized  |  -  |
**403** | Error Forbidden |  -  |
**404** | Error Not Found |  -  |
**500** | Error Internal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

