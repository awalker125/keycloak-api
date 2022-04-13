# keycloak_api.GroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_groups_count_get**](GroupsApi.md#realm_groups_count_get) | **GET** /{realm}/groups/count | Returns the groups counts.
[**realm_groups_get**](GroupsApi.md#realm_groups_get) | **GET** /{realm}/groups | Get group hierarchy.
[**realm_groups_id_children_post**](GroupsApi.md#realm_groups_id_children_post) | **POST** /{realm}/groups/{id}/children | Set or create child.
[**realm_groups_id_delete**](GroupsApi.md#realm_groups_id_delete) | **DELETE** /{realm}/groups/{id} | 
[**realm_groups_id_get**](GroupsApi.md#realm_groups_id_get) | **GET** /{realm}/groups/{id} | 
[**realm_groups_id_management_permissions_get**](GroupsApi.md#realm_groups_id_management_permissions_get) | **GET** /{realm}/groups/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realm_groups_id_management_permissions_put**](GroupsApi.md#realm_groups_id_management_permissions_put) | **PUT** /{realm}/groups/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realm_groups_id_members_get**](GroupsApi.md#realm_groups_id_members_get) | **GET** /{realm}/groups/{id}/members | Get users   Returns a stream of users, filtered according to query parameters
[**realm_groups_id_put**](GroupsApi.md#realm_groups_id_put) | **PUT** /{realm}/groups/{id} | Update group, ignores subgroups.
[**realm_groups_post**](GroupsApi.md#realm_groups_post) | **POST** /{realm}/groups | create or add a top level realm groupSet or create child.


# **realm_groups_count_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} realm_groups_count_get(realm)

Returns the groups counts.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import groups_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = keycloak_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = keycloak_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with keycloak_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    search = "search_example" # str |  (optional)
    top = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns the groups counts.
        api_response = api_instance.realm_groups_count_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the groups counts.
        api_response = api_instance.realm_groups_count_get(realm, search=search, top=top)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **search** | **str**|  | [optional]
 **top** | **bool**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_groups_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_groups_get(realm)

Get group hierarchy.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import groups_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = keycloak_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = keycloak_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with keycloak_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    brief_representation = True # bool |  (optional)
    first = 1 # int |  (optional)
    max = 1 # int |  (optional)
    search = "search_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get group hierarchy.
        api_response = api_instance.realm_groups_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get group hierarchy.
        api_response = api_instance.realm_groups_get(realm, brief_representation=brief_representation, first=first, max=max, search=search)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **brief_representation** | **bool**|  | [optional]
 **first** | **int**|  | [optional]
 **max** | **int**|  | [optional]
 **search** | **str**|  | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_groups_id_children_post**
> realm_groups_id_children_post(realm, id, group_representation)

Set or create child.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import groups_api
from keycloak_api.model.group_representation import GroupRepresentation
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = keycloak_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = keycloak_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with keycloak_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    group_representation = GroupRepresentation(
        access={},
        attributes={},
        client_roles={},
        id="id_example",
        name="name_example",
        path="path_example",
        realm_roles=[
            "realm_roles_example",
        ],
        sub_groups=[
            GroupRepresentation(),
        ],
    ) # GroupRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Set or create child.
        api_instance.realm_groups_id_children_post(realm, id, group_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_id_children_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
 **group_representation** | [**GroupRepresentation**](GroupRepresentation.md)|  |

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_groups_id_delete**
> realm_groups_id_delete(realm, id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import groups_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = keycloak_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = keycloak_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with keycloak_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_groups_id_delete(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_groups_id_get**
> GroupRepresentation realm_groups_id_get(realm, id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import groups_api
from keycloak_api.model.group_representation import GroupRepresentation
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = keycloak_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = keycloak_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with keycloak_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_groups_id_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |

### Return type

[**GroupRepresentation**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_groups_id_management_permissions_get**
> ManagementPermissionReference realm_groups_id_management_permissions_get(realm, id)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import groups_api
from keycloak_api.model.management_permission_reference import ManagementPermissionReference
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = keycloak_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = keycloak_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with keycloak_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.realm_groups_id_management_permissions_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_id_management_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_groups_id_management_permissions_put**
> ManagementPermissionReference realm_groups_id_management_permissions_put(realm, id, management_permission_reference)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import groups_api
from keycloak_api.model.management_permission_reference import ManagementPermissionReference
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = keycloak_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = keycloak_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with keycloak_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    management_permission_reference = ManagementPermissionReference(
        enabled=True,
        resource="resource_example",
        scope_permissions={},
    ) # ManagementPermissionReference | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.realm_groups_id_management_permissions_put(realm, id, management_permission_reference)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_id_management_permissions_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
 **management_permission_reference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  |

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_groups_id_members_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_groups_id_members_get(realm, id)

Get users   Returns a stream of users, filtered according to query parameters

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import groups_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = keycloak_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = keycloak_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with keycloak_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    brief_representation = True # bool | Only return basic information (only guaranteed to return id, username, created, first and last name,  email, enabled state, email verification state, federation link, and access.  Note that it means that namely user attributes, required actions, and not before are not returned.) (optional)
    first = 1 # int | Pagination offset (optional)
    max = 1 # int | Maximum results size (defaults to 100) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get users   Returns a stream of users, filtered according to query parameters
        api_response = api_instance.realm_groups_id_members_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_id_members_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get users   Returns a stream of users, filtered according to query parameters
        api_response = api_instance.realm_groups_id_members_get(realm, id, brief_representation=brief_representation, first=first, max=max)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_id_members_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
 **brief_representation** | **bool**| Only return basic information (only guaranteed to return id, username, created, first and last name,  email, enabled state, email verification state, federation link, and access.  Note that it means that namely user attributes, required actions, and not before are not returned.) | [optional]
 **first** | **int**| Pagination offset | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_groups_id_put**
> realm_groups_id_put(realm, id, group_representation)

Update group, ignores subgroups.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import groups_api
from keycloak_api.model.group_representation import GroupRepresentation
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = keycloak_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = keycloak_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with keycloak_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    group_representation = GroupRepresentation(
        access={},
        attributes={},
        client_roles={},
        id="id_example",
        name="name_example",
        path="path_example",
        realm_roles=[
            "realm_roles_example",
        ],
        sub_groups=[
            GroupRepresentation(),
        ],
    ) # GroupRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update group, ignores subgroups.
        api_instance.realm_groups_id_put(realm, id, group_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
 **group_representation** | [**GroupRepresentation**](GroupRepresentation.md)|  |

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_groups_post**
> realm_groups_post(realm, group_representation)

create or add a top level realm groupSet or create child.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import groups_api
from keycloak_api.model.group_representation import GroupRepresentation
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = keycloak_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = keycloak_api.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with keycloak_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groups_api.GroupsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    group_representation = GroupRepresentation(
        access={},
        attributes={},
        client_roles={},
        id="id_example",
        name="name_example",
        path="path_example",
        realm_roles=[
            "realm_roles_example",
        ],
        sub_groups=[
            GroupRepresentation(),
        ],
    ) # GroupRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # create or add a top level realm groupSet or create child.
        api_instance.realm_groups_post(realm, group_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling GroupsApi->realm_groups_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **group_representation** | [**GroupRepresentation**](GroupRepresentation.md)|  |

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

