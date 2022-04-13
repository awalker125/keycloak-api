# keycloak_api.RolesByIDApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_roles_by_id_role_id_composites_clients_client_uuid_get**](RolesByIDApi.md#realm_roles_by_id_role_id_composites_clients_client_uuid_get) | **GET** /{realm}/roles-by-id/{role-id}/composites/clients/{clientUuid} | Get client-level roles for the client that are in the role’s composite
[**realm_roles_by_id_role_id_composites_delete**](RolesByIDApi.md#realm_roles_by_id_role_id_composites_delete) | **DELETE** /{realm}/roles-by-id/{role-id}/composites | Remove a set of roles from the role’s composite
[**realm_roles_by_id_role_id_composites_get**](RolesByIDApi.md#realm_roles_by_id_role_id_composites_get) | **GET** /{realm}/roles-by-id/{role-id}/composites | Get role’s children   Returns a set of role’s children provided the role is a composite.
[**realm_roles_by_id_role_id_composites_post**](RolesByIDApi.md#realm_roles_by_id_role_id_composites_post) | **POST** /{realm}/roles-by-id/{role-id}/composites | Make the role a composite role by associating some child roles
[**realm_roles_by_id_role_id_composites_realm_get**](RolesByIDApi.md#realm_roles_by_id_role_id_composites_realm_get) | **GET** /{realm}/roles-by-id/{role-id}/composites/realm | Get realm-level roles that are in the role’s composite
[**realm_roles_by_id_role_id_delete**](RolesByIDApi.md#realm_roles_by_id_role_id_delete) | **DELETE** /{realm}/roles-by-id/{role-id} | Delete the role
[**realm_roles_by_id_role_id_get**](RolesByIDApi.md#realm_roles_by_id_role_id_get) | **GET** /{realm}/roles-by-id/{role-id} | Get a specific role’s representation
[**realm_roles_by_id_role_id_management_permissions_get**](RolesByIDApi.md#realm_roles_by_id_role_id_management_permissions_get) | **GET** /{realm}/roles-by-id/{role-id}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference
[**realm_roles_by_id_role_id_management_permissions_put**](RolesByIDApi.md#realm_roles_by_id_role_id_management_permissions_put) | **PUT** /{realm}/roles-by-id/{role-id}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference
[**realm_roles_by_id_role_id_put**](RolesByIDApi.md#realm_roles_by_id_role_id_put) | **PUT** /{realm}/roles-by-id/{role-id} | Update the role


# **realm_roles_by_id_role_id_composites_clients_client_uuid_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_roles_by_id_role_id_composites_clients_client_uuid_get(realm, role_id, client_uuid)

Get client-level roles for the client that are in the role’s composite

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_by_id_api
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
    api_instance = roles_by_id_api.RolesByIDApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_id = "role-id_example" # str | 
    client_uuid = "clientUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get client-level roles for the client that are in the role’s composite
        api_response = api_instance.realm_roles_by_id_role_id_composites_clients_client_uuid_get(realm, role_id, client_uuid)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_composites_clients_client_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_id** | **str**|  |
 **client_uuid** | **str**|  |

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

# **realm_roles_by_id_role_id_composites_delete**
> realm_roles_by_id_role_id_composites_delete(realm, role_id, role_representation)

Remove a set of roles from the role’s composite

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_by_id_api
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
    api_instance = roles_by_id_api.RolesByIDApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_id = "role-id_example" # str | Role id
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
    ] # [RoleRepresentation] | A set of roles to be removed

    # example passing only required values which don't have defaults set
    try:
        # Remove a set of roles from the role’s composite
        api_instance.realm_roles_by_id_role_id_composites_delete(realm, role_id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_composites_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_id** | **str**| Role id |
 **role_representation** | [**[RoleRepresentation]**](RoleRepresentation.md)| A set of roles to be removed |

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

# **realm_roles_by_id_role_id_composites_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_roles_by_id_role_id_composites_get(realm, role_id)

Get role’s children   Returns a set of role’s children provided the role is a composite.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_by_id_api
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
    api_instance = roles_by_id_api.RolesByIDApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_id = "role-id_example" # str | Role id
    first = 1 # int |  (optional)
    max = 1 # int |  (optional)
    search = "search_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get role’s children   Returns a set of role’s children provided the role is a composite.
        api_response = api_instance.realm_roles_by_id_role_id_composites_get(realm, role_id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_composites_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get role’s children   Returns a set of role’s children provided the role is a composite.
        api_response = api_instance.realm_roles_by_id_role_id_composites_get(realm, role_id, first=first, max=max, search=search)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_composites_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_id** | **str**| Role id |
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

# **realm_roles_by_id_role_id_composites_post**
> realm_roles_by_id_role_id_composites_post(realm, role_id, role_representation)

Make the role a composite role by associating some child roles

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_by_id_api
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
    api_instance = roles_by_id_api.RolesByIDApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_id = "role-id_example" # str | Role id
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
        # Make the role a composite role by associating some child roles
        api_instance.realm_roles_by_id_role_id_composites_post(realm, role_id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_composites_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_id** | **str**| Role id |
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

# **realm_roles_by_id_role_id_composites_realm_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_roles_by_id_role_id_composites_realm_get(realm, role_id)

Get realm-level roles that are in the role’s composite

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_by_id_api
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
    api_instance = roles_by_id_api.RolesByIDApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_id = "role-id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that are in the role’s composite
        api_response = api_instance.realm_roles_by_id_role_id_composites_realm_get(realm, role_id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_composites_realm_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_id** | **str**|  |

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

# **realm_roles_by_id_role_id_delete**
> realm_roles_by_id_role_id_delete(realm, role_id)

Delete the role

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_by_id_api
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
    api_instance = roles_by_id_api.RolesByIDApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_id = "role-id_example" # str | id of role

    # example passing only required values which don't have defaults set
    try:
        # Delete the role
        api_instance.realm_roles_by_id_role_id_delete(realm, role_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_id** | **str**| id of role |

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

# **realm_roles_by_id_role_id_get**
> RoleRepresentation realm_roles_by_id_role_id_get(realm, role_id)

Get a specific role’s representation

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_by_id_api
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
    api_instance = roles_by_id_api.RolesByIDApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_id = "role-id_example" # str | id of role

    # example passing only required values which don't have defaults set
    try:
        # Get a specific role’s representation
        api_response = api_instance.realm_roles_by_id_role_id_get(realm, role_id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_id** | **str**| id of role |

### Return type

[**RoleRepresentation**](RoleRepresentation.md)

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

# **realm_roles_by_id_role_id_management_permissions_get**
> ManagementPermissionReference realm_roles_by_id_role_id_management_permissions_get(realm, role_id)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_by_id_api
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
    api_instance = roles_by_id_api.RolesByIDApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_id = "role-id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authoirzation permissions have been initialized or not and a reference
        api_response = api_instance.realm_roles_by_id_role_id_management_permissions_get(realm, role_id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_management_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_id** | **str**|  |

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

# **realm_roles_by_id_role_id_management_permissions_put**
> ManagementPermissionReference realm_roles_by_id_role_id_management_permissions_put(realm, role_id, management_permission_reference)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_by_id_api
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
    api_instance = roles_by_id_api.RolesByIDApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_id = "role-id_example" # str | 
    management_permission_reference = ManagementPermissionReference(
        enabled=True,
        resource="resource_example",
        scope_permissions={},
    ) # ManagementPermissionReference | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authoirzation permissions have been initialized or not and a reference
        api_response = api_instance.realm_roles_by_id_role_id_management_permissions_put(realm, role_id, management_permission_reference)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_management_permissions_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_id** | **str**|  |
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

# **realm_roles_by_id_role_id_put**
> realm_roles_by_id_role_id_put(realm, role_id, role_representation)

Update the role

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_by_id_api
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
    api_instance = roles_by_id_api.RolesByIDApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_id = "role-id_example" # str | id of role
    role_representation = RoleRepresentation(
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
    ) # RoleRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update the role
        api_instance.realm_roles_by_id_role_id_put(realm, role_id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesByIDApi->realm_roles_by_id_role_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_id** | **str**| id of role |
 **role_representation** | [**RoleRepresentation**](RoleRepresentation.md)|  |

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

