# keycloak_api.RoleMapperApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_groups_id_role_mappings_get**](RoleMapperApi.md#realm_groups_id_role_mappings_get) | **GET** /{realm}/groups/{id}/role-mappings | Get role mappings
[**realm_groups_id_role_mappings_realm_available_get**](RoleMapperApi.md#realm_groups_id_role_mappings_realm_available_get) | **GET** /{realm}/groups/{id}/role-mappings/realm/available | Get realm-level roles that can be mapped
[**realm_groups_id_role_mappings_realm_composite_get**](RoleMapperApi.md#realm_groups_id_role_mappings_realm_composite_get) | **GET** /{realm}/groups/{id}/role-mappings/realm/composite | Get effective realm-level role mappings   This will recurse all composite roles to get the result.
[**realm_groups_id_role_mappings_realm_delete**](RoleMapperApi.md#realm_groups_id_role_mappings_realm_delete) | **DELETE** /{realm}/groups/{id}/role-mappings/realm | Delete realm-level role mappings
[**realm_groups_id_role_mappings_realm_get**](RoleMapperApi.md#realm_groups_id_role_mappings_realm_get) | **GET** /{realm}/groups/{id}/role-mappings/realm | Get realm-level role mappings
[**realm_groups_id_role_mappings_realm_post**](RoleMapperApi.md#realm_groups_id_role_mappings_realm_post) | **POST** /{realm}/groups/{id}/role-mappings/realm | Add realm-level role mappings to the user
[**realm_users_id_role_mappings_get**](RoleMapperApi.md#realm_users_id_role_mappings_get) | **GET** /{realm}/users/{id}/role-mappings | Get role mappings
[**realm_users_id_role_mappings_realm_available_get**](RoleMapperApi.md#realm_users_id_role_mappings_realm_available_get) | **GET** /{realm}/users/{id}/role-mappings/realm/available | Get realm-level roles that can be mapped
[**realm_users_id_role_mappings_realm_composite_get**](RoleMapperApi.md#realm_users_id_role_mappings_realm_composite_get) | **GET** /{realm}/users/{id}/role-mappings/realm/composite | Get effective realm-level role mappings   This will recurse all composite roles to get the result.
[**realm_users_id_role_mappings_realm_delete**](RoleMapperApi.md#realm_users_id_role_mappings_realm_delete) | **DELETE** /{realm}/users/{id}/role-mappings/realm | Delete realm-level role mappings
[**realm_users_id_role_mappings_realm_get**](RoleMapperApi.md#realm_users_id_role_mappings_realm_get) | **GET** /{realm}/users/{id}/role-mappings/realm | Get realm-level role mappings
[**realm_users_id_role_mappings_realm_post**](RoleMapperApi.md#realm_users_id_role_mappings_realm_post) | **POST** /{realm}/users/{id}/role-mappings/realm | Add realm-level role mappings to the user


# **realm_groups_id_role_mappings_get**
> MappingsRepresentation realm_groups_id_role_mappings_get(realm, id)

Get role mappings

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
from keycloak_api.model.mappings_representation import MappingsRepresentation
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get role mappings
        api_response = api_instance.realm_groups_id_role_mappings_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_groups_id_role_mappings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |

### Return type

[**MappingsRepresentation**](MappingsRepresentation.md)

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

# **realm_groups_id_role_mappings_realm_available_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_groups_id_role_mappings_realm_available_get(realm, id)

Get realm-level roles that can be mapped

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that can be mapped
        api_response = api_instance.realm_groups_id_role_mappings_realm_available_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_groups_id_role_mappings_realm_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |

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

# **realm_groups_id_role_mappings_realm_composite_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_groups_id_role_mappings_realm_composite_get(realm, id)

Get effective realm-level role mappings   This will recurse all composite roles to get the result.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get effective realm-level role mappings   This will recurse all composite roles to get the result.
        api_response = api_instance.realm_groups_id_role_mappings_realm_composite_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_groups_id_role_mappings_realm_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective realm-level role mappings   This will recurse all composite roles to get the result.
        api_response = api_instance.realm_groups_id_role_mappings_realm_composite_get(realm, id, brief_representation=brief_representation)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_groups_id_role_mappings_realm_composite_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
 **brief_representation** | **bool**| if false, return roles with their attributes | [optional]

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

# **realm_groups_id_role_mappings_realm_delete**
> realm_groups_id_role_mappings_realm_delete(realm, id, role_representation)

Delete realm-level role mappings

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
from keycloak_api.model.role_representation import RoleRepresentation
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    role_representation = [
        RoleRepresentation(
            attributes={},
            client_role=True,
            composite=True,
            composites=RoleRepresentationComposites(
                client={},
                realm=[
                    "realm_example",
                ],
            ),
            container_id="container_id_example",
            description="description_example",
            id="id_example",
            name="name_example",
        ),
    ] # [RoleRepresentation] | 

    # example passing only required values which don't have defaults set
    try:
        # Delete realm-level role mappings
        api_instance.realm_groups_id_role_mappings_realm_delete(realm, id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_groups_id_role_mappings_realm_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
 **role_representation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  |

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

# **realm_groups_id_role_mappings_realm_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_groups_id_role_mappings_realm_get(realm, id)

Get realm-level role mappings

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level role mappings
        api_response = api_instance.realm_groups_id_role_mappings_realm_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_groups_id_role_mappings_realm_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |

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

# **realm_groups_id_role_mappings_realm_post**
> realm_groups_id_role_mappings_realm_post(realm, id, role_representation)

Add realm-level role mappings to the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
from keycloak_api.model.role_representation import RoleRepresentation
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    role_representation = [
        RoleRepresentation(
            attributes={},
            client_role=True,
            composite=True,
            composites=RoleRepresentationComposites(
                client={},
                realm=[
                    "realm_example",
                ],
            ),
            container_id="container_id_example",
            description="description_example",
            id="id_example",
            name="name_example",
        ),
    ] # [RoleRepresentation] | Roles to add

    # example passing only required values which don't have defaults set
    try:
        # Add realm-level role mappings to the user
        api_instance.realm_groups_id_role_mappings_realm_post(realm, id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_groups_id_role_mappings_realm_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
 **role_representation** | [**[RoleRepresentation]**](RoleRepresentation.md)| Roles to add |

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

# **realm_users_id_role_mappings_get**
> MappingsRepresentation realm_users_id_role_mappings_get(realm, id)

Get role mappings

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
from keycloak_api.model.mappings_representation import MappingsRepresentation
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Get role mappings
        api_response = api_instance.realm_users_id_role_mappings_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_users_id_role_mappings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

### Return type

[**MappingsRepresentation**](MappingsRepresentation.md)

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

# **realm_users_id_role_mappings_realm_available_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_role_mappings_realm_available_get(realm, id)

Get realm-level roles that can be mapped

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that can be mapped
        api_response = api_instance.realm_users_id_role_mappings_realm_available_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_users_id_role_mappings_realm_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_id_role_mappings_realm_composite_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_role_mappings_realm_composite_get(realm, id)

Get effective realm-level role mappings   This will recurse all composite roles to get the result.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    brief_representation = True # bool | if false, return roles with their attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get effective realm-level role mappings   This will recurse all composite roles to get the result.
        api_response = api_instance.realm_users_id_role_mappings_realm_composite_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_users_id_role_mappings_realm_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective realm-level role mappings   This will recurse all composite roles to get the result.
        api_response = api_instance.realm_users_id_role_mappings_realm_composite_get(realm, id, brief_representation=brief_representation)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_users_id_role_mappings_realm_composite_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **brief_representation** | **bool**| if false, return roles with their attributes | [optional]

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

# **realm_users_id_role_mappings_realm_delete**
> realm_users_id_role_mappings_realm_delete(realm, id, role_representation)

Delete realm-level role mappings

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
from keycloak_api.model.role_representation import RoleRepresentation
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    role_representation = [
        RoleRepresentation(
            attributes={},
            client_role=True,
            composite=True,
            composites=RoleRepresentationComposites(
                client={},
                realm=[
                    "realm_example",
                ],
            ),
            container_id="container_id_example",
            description="description_example",
            id="id_example",
            name="name_example",
        ),
    ] # [RoleRepresentation] | 

    # example passing only required values which don't have defaults set
    try:
        # Delete realm-level role mappings
        api_instance.realm_users_id_role_mappings_realm_delete(realm, id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_users_id_role_mappings_realm_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **role_representation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  |

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

# **realm_users_id_role_mappings_realm_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_role_mappings_realm_get(realm, id)

Get realm-level role mappings

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level role mappings
        api_response = api_instance.realm_users_id_role_mappings_realm_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_users_id_role_mappings_realm_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_id_role_mappings_realm_post**
> realm_users_id_role_mappings_realm_post(realm, id, role_representation)

Add realm-level role mappings to the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import role_mapper_api
from keycloak_api.model.role_representation import RoleRepresentation
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
    api_instance = role_mapper_api.RoleMapperApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    role_representation = [
        RoleRepresentation(
            attributes={},
            client_role=True,
            composite=True,
            composites=RoleRepresentationComposites(
                client={},
                realm=[
                    "realm_example",
                ],
            ),
            container_id="container_id_example",
            description="description_example",
            id="id_example",
            name="name_example",
        ),
    ] # [RoleRepresentation] | Roles to add

    # example passing only required values which don't have defaults set
    try:
        # Add realm-level role mappings to the user
        api_instance.realm_users_id_role_mappings_realm_post(realm, id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RoleMapperApi->realm_users_id_role_mappings_realm_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **role_representation** | [**[RoleRepresentation]**](RoleRepresentation.md)| Roles to add |

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

