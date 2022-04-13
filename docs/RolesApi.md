# keycloak_api.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_clients_id_roles_get**](RolesApi.md#realm_clients_id_roles_get) | **GET** /{realm}/clients/{id}/roles | Get all roles for the realm or client
[**realm_clients_id_roles_post**](RolesApi.md#realm_clients_id_roles_post) | **POST** /{realm}/clients/{id}/roles | Create a new role for the realm or client
[**realm_clients_id_roles_role_name_composites_clients_client_uuid_get**](RolesApi.md#realm_clients_id_roles_role_name_composites_clients_client_uuid_get) | **GET** /{realm}/clients/{id}/roles/{role-name}/composites/clients/{clientUuid} | Get client-level roles for the client that are in the role’s composite
[**realm_clients_id_roles_role_name_composites_delete**](RolesApi.md#realm_clients_id_roles_role_name_composites_delete) | **DELETE** /{realm}/clients/{id}/roles/{role-name}/composites | Remove roles from the role’s composite
[**realm_clients_id_roles_role_name_composites_get**](RolesApi.md#realm_clients_id_roles_role_name_composites_get) | **GET** /{realm}/clients/{id}/roles/{role-name}/composites | Get composites of the role
[**realm_clients_id_roles_role_name_composites_post**](RolesApi.md#realm_clients_id_roles_role_name_composites_post) | **POST** /{realm}/clients/{id}/roles/{role-name}/composites | Add a composite to the role
[**realm_clients_id_roles_role_name_composites_realm_get**](RolesApi.md#realm_clients_id_roles_role_name_composites_realm_get) | **GET** /{realm}/clients/{id}/roles/{role-name}/composites/realm | Get realm-level roles of the role’s composite
[**realm_clients_id_roles_role_name_delete**](RolesApi.md#realm_clients_id_roles_role_name_delete) | **DELETE** /{realm}/clients/{id}/roles/{role-name} | Delete a role by name
[**realm_clients_id_roles_role_name_get**](RolesApi.md#realm_clients_id_roles_role_name_get) | **GET** /{realm}/clients/{id}/roles/{role-name} | Get a role by name
[**realm_clients_id_roles_role_name_groups_get**](RolesApi.md#realm_clients_id_roles_role_name_groups_get) | **GET** /{realm}/clients/{id}/roles/{role-name}/groups | Returns a stream of groups that have the specified role name
[**realm_clients_id_roles_role_name_management_permissions_get**](RolesApi.md#realm_clients_id_roles_role_name_management_permissions_get) | **GET** /{realm}/clients/{id}/roles/{role-name}/management/permissions | Return object stating whether role Authorization permissions have been initialized or not and a reference
[**realm_clients_id_roles_role_name_management_permissions_put**](RolesApi.md#realm_clients_id_roles_role_name_management_permissions_put) | **PUT** /{realm}/clients/{id}/roles/{role-name}/management/permissions | Return object stating whether role Authorization permissions have been initialized or not and a reference
[**realm_clients_id_roles_role_name_put**](RolesApi.md#realm_clients_id_roles_role_name_put) | **PUT** /{realm}/clients/{id}/roles/{role-name} | Update a role by name
[**realm_clients_id_roles_role_name_users_get**](RolesApi.md#realm_clients_id_roles_role_name_users_get) | **GET** /{realm}/clients/{id}/roles/{role-name}/users | Returns a stream of users that have the specified role name.
[**realm_roles_get**](RolesApi.md#realm_roles_get) | **GET** /{realm}/roles | Get all roles for the realm or client
[**realm_roles_post**](RolesApi.md#realm_roles_post) | **POST** /{realm}/roles | Create a new role for the realm or client
[**realm_roles_role_name_composites_clients_client_uuid_get**](RolesApi.md#realm_roles_role_name_composites_clients_client_uuid_get) | **GET** /{realm}/roles/{role-name}/composites/clients/{clientUuid} | Get client-level roles for the client that are in the role’s composite
[**realm_roles_role_name_composites_delete**](RolesApi.md#realm_roles_role_name_composites_delete) | **DELETE** /{realm}/roles/{role-name}/composites | Remove roles from the role’s composite
[**realm_roles_role_name_composites_get**](RolesApi.md#realm_roles_role_name_composites_get) | **GET** /{realm}/roles/{role-name}/composites | Get composites of the role
[**realm_roles_role_name_composites_post**](RolesApi.md#realm_roles_role_name_composites_post) | **POST** /{realm}/roles/{role-name}/composites | Add a composite to the role
[**realm_roles_role_name_composites_realm_get**](RolesApi.md#realm_roles_role_name_composites_realm_get) | **GET** /{realm}/roles/{role-name}/composites/realm | Get realm-level roles of the role’s composite
[**realm_roles_role_name_delete**](RolesApi.md#realm_roles_role_name_delete) | **DELETE** /{realm}/roles/{role-name} | Delete a role by name
[**realm_roles_role_name_get**](RolesApi.md#realm_roles_role_name_get) | **GET** /{realm}/roles/{role-name} | Get a role by name
[**realm_roles_role_name_groups_get**](RolesApi.md#realm_roles_role_name_groups_get) | **GET** /{realm}/roles/{role-name}/groups | Returns a stream of groups that have the specified role name
[**realm_roles_role_name_management_permissions_get**](RolesApi.md#realm_roles_role_name_management_permissions_get) | **GET** /{realm}/roles/{role-name}/management/permissions | Return object stating whether role Authorization permissions have been initialized or not and a reference
[**realm_roles_role_name_management_permissions_put**](RolesApi.md#realm_roles_role_name_management_permissions_put) | **PUT** /{realm}/roles/{role-name}/management/permissions | Return object stating whether role Authorization permissions have been initialized or not and a reference
[**realm_roles_role_name_put**](RolesApi.md#realm_roles_role_name_put) | **PUT** /{realm}/roles/{role-name} | Update a role by name
[**realm_roles_role_name_users_get**](RolesApi.md#realm_roles_role_name_users_get) | **GET** /{realm}/roles/{role-name}/users | Returns a stream of users that have the specified role name.


# **realm_clients_id_roles_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_roles_get(realm, id)

Get all roles for the realm or client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    brief_representation = True # bool |  (optional)
    first = 1 # int |  (optional)
    max = 1 # int |  (optional)
    search = "search_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all roles for the realm or client
        api_response = api_instance.realm_clients_id_roles_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all roles for the realm or client
        api_response = api_instance.realm_clients_id_roles_get(realm, id, brief_representation=brief_representation, first=first, max=max, search=search)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
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

# **realm_clients_id_roles_post**
> realm_clients_id_roles_post(realm, id, role_representation)

Create a new role for the realm or client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
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
        # Create a new role for the realm or client
        api_instance.realm_clients_id_roles_post(realm, id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
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

# **realm_clients_id_roles_role_name_composites_clients_client_uuid_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_roles_role_name_composites_clients_client_uuid_get(realm, id, role_name, client_uuid)

Get client-level roles for the client that are in the role’s composite

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | role’s name (not id!)
    client_uuid = "clientUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get client-level roles for the client that are in the role’s composite
        api_response = api_instance.realm_clients_id_roles_role_name_composites_clients_client_uuid_get(realm, id, role_name, client_uuid)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_composites_clients_client_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**| role’s name (not id!) |
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

# **realm_clients_id_roles_role_name_composites_delete**
> realm_clients_id_roles_role_name_composites_delete(realm, id, role_name, role_representation)

Remove roles from the role’s composite

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | role’s name (not id!)
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
    ] # [RoleRepresentation] | roles to remove

    # example passing only required values which don't have defaults set
    try:
        # Remove roles from the role’s composite
        api_instance.realm_clients_id_roles_role_name_composites_delete(realm, id, role_name, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_composites_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**| role’s name (not id!) |
 **role_representation** | [**[RoleRepresentation]**](RoleRepresentation.md)| roles to remove |

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

# **realm_clients_id_roles_role_name_composites_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_roles_role_name_composites_get(realm, id, role_name)

Get composites of the role

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | role’s name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get composites of the role
        api_response = api_instance.realm_clients_id_roles_role_name_composites_get(realm, id, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_composites_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**| role’s name (not id!) |

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

# **realm_clients_id_roles_role_name_composites_post**
> realm_clients_id_roles_role_name_composites_post(realm, id, role_name, role_representation)

Add a composite to the role

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | role’s name (not id!)
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
        # Add a composite to the role
        api_instance.realm_clients_id_roles_role_name_composites_post(realm, id, role_name, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_composites_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**| role’s name (not id!) |
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

# **realm_clients_id_roles_role_name_composites_realm_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_roles_role_name_composites_realm_get(realm, id, role_name)

Get realm-level roles of the role’s composite

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | role’s name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles of the role’s composite
        api_response = api_instance.realm_clients_id_roles_role_name_composites_realm_get(realm, id, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_composites_realm_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**| role’s name (not id!) |

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

# **realm_clients_id_roles_role_name_delete**
> realm_clients_id_roles_role_name_delete(realm, id, role_name)

Delete a role by name

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | role’s name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Delete a role by name
        api_instance.realm_clients_id_roles_role_name_delete(realm, id, role_name)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**| role’s name (not id!) |

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

# **realm_clients_id_roles_role_name_get**
> RoleRepresentation realm_clients_id_roles_role_name_get(realm, id, role_name)

Get a role by name

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | role’s name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get a role by name
        api_response = api_instance.realm_clients_id_roles_role_name_get(realm, id, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**| role’s name (not id!) |

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

# **realm_clients_id_roles_role_name_groups_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_roles_role_name_groups_get(realm, id, role_name)

Returns a stream of groups that have the specified role name

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | the role name.
    brief_representation = True # bool | if false, return a full representation of the {@code GroupRepresentation} objects. (optional)
    first = 1 # int | first result to return. Ignored if negative or {@code null}. (optional)
    max = 1 # int | maximum number of results to return. Ignored if negative or {@code null}. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a stream of groups that have the specified role name
        api_response = api_instance.realm_clients_id_roles_role_name_groups_get(realm, id, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a stream of groups that have the specified role name
        api_response = api_instance.realm_clients_id_roles_role_name_groups_get(realm, id, role_name, brief_representation=brief_representation, first=first, max=max)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**| the role name. |
 **brief_representation** | **bool**| if false, return a full representation of the {@code GroupRepresentation} objects. | [optional]
 **first** | **int**| first result to return. Ignored if negative or {@code null}. | [optional]
 **max** | **int**| maximum number of results to return. Ignored if negative or {@code null}. | [optional]

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

# **realm_clients_id_roles_role_name_management_permissions_get**
> ManagementPermissionReference realm_clients_id_roles_role_name_management_permissions_get(realm, id, role_name)

Return object stating whether role Authorization permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.realm_clients_id_roles_role_name_management_permissions_get(realm, id, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_management_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**|  |

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

# **realm_clients_id_roles_role_name_management_permissions_put**
> ManagementPermissionReference realm_clients_id_roles_role_name_management_permissions_put(realm, id, role_name, management_permission_reference)

Return object stating whether role Authorization permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | 
    management_permission_reference = ManagementPermissionReference(
        enabled=True,
        resource="resource_example",
        scope_permissions={},
    ) # ManagementPermissionReference | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.realm_clients_id_roles_role_name_management_permissions_put(realm, id, role_name, management_permission_reference)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_management_permissions_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**|  |
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

# **realm_clients_id_roles_role_name_put**
> realm_clients_id_roles_role_name_put(realm, id, role_name, role_representation)

Update a role by name

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | role’s name (not id!)
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
        # Update a role by name
        api_instance.realm_clients_id_roles_role_name_put(realm, id, role_name, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**| role’s name (not id!) |
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

# **realm_clients_id_roles_role_name_users_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_roles_role_name_users_get(realm, id, role_name)

Returns a stream of users that have the specified role name.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_name = "role-name_example" # str | the role name.
    first = 1 # int | first result to return. Ignored if negative or {@code null}. (optional)
    max = 1 # int | maximum number of results to return. Ignored if negative or {@code null}. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a stream of users that have the specified role name.
        api_response = api_instance.realm_clients_id_roles_role_name_users_get(realm, id, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_users_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a stream of users that have the specified role name.
        api_response = api_instance.realm_clients_id_roles_role_name_users_get(realm, id, role_name, first=first, max=max)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_clients_id_roles_role_name_users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_name** | **str**| the role name. |
 **first** | **int**| first result to return. Ignored if negative or {@code null}. | [optional]
 **max** | **int**| maximum number of results to return. Ignored if negative or {@code null}. | [optional]

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

# **realm_roles_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_roles_get(realm)

Get all roles for the realm or client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    brief_representation = True # bool |  (optional)
    first = 1 # int |  (optional)
    max = 1 # int |  (optional)
    search = "search_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all roles for the realm or client
        api_response = api_instance.realm_roles_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all roles for the realm or client
        api_response = api_instance.realm_roles_get(realm, brief_representation=brief_representation, first=first, max=max, search=search)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_get: %s\n" % e)
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

# **realm_roles_post**
> realm_roles_post(realm, role_representation)

Create a new role for the realm or client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
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
        # Create a new role for the realm or client
        api_instance.realm_roles_post(realm, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
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

# **realm_roles_role_name_composites_clients_client_uuid_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_roles_role_name_composites_clients_client_uuid_get(realm, role_name, client_uuid)

Get client-level roles for the client that are in the role’s composite

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | role’s name (not id!)
    client_uuid = "clientUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get client-level roles for the client that are in the role’s composite
        api_response = api_instance.realm_roles_role_name_composites_clients_client_uuid_get(realm, role_name, client_uuid)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_composites_clients_client_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**| role’s name (not id!) |
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

# **realm_roles_role_name_composites_delete**
> realm_roles_role_name_composites_delete(realm, role_name, role_representation)

Remove roles from the role’s composite

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | role’s name (not id!)
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
    ] # [RoleRepresentation] | roles to remove

    # example passing only required values which don't have defaults set
    try:
        # Remove roles from the role’s composite
        api_instance.realm_roles_role_name_composites_delete(realm, role_name, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_composites_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**| role’s name (not id!) |
 **role_representation** | [**[RoleRepresentation]**](RoleRepresentation.md)| roles to remove |

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

# **realm_roles_role_name_composites_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_roles_role_name_composites_get(realm, role_name)

Get composites of the role

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | role’s name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get composites of the role
        api_response = api_instance.realm_roles_role_name_composites_get(realm, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_composites_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**| role’s name (not id!) |

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

# **realm_roles_role_name_composites_post**
> realm_roles_role_name_composites_post(realm, role_name, role_representation)

Add a composite to the role

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | role’s name (not id!)
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
        # Add a composite to the role
        api_instance.realm_roles_role_name_composites_post(realm, role_name, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_composites_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**| role’s name (not id!) |
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

# **realm_roles_role_name_composites_realm_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_roles_role_name_composites_realm_get(realm, role_name)

Get realm-level roles of the role’s composite

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | role’s name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles of the role’s composite
        api_response = api_instance.realm_roles_role_name_composites_realm_get(realm, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_composites_realm_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**| role’s name (not id!) |

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

# **realm_roles_role_name_delete**
> realm_roles_role_name_delete(realm, role_name)

Delete a role by name

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | role’s name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Delete a role by name
        api_instance.realm_roles_role_name_delete(realm, role_name)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**| role’s name (not id!) |

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

# **realm_roles_role_name_get**
> RoleRepresentation realm_roles_role_name_get(realm, role_name)

Get a role by name

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | role’s name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get a role by name
        api_response = api_instance.realm_roles_role_name_get(realm, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**| role’s name (not id!) |

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

# **realm_roles_role_name_groups_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_roles_role_name_groups_get(realm, role_name)

Returns a stream of groups that have the specified role name

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | the role name.
    brief_representation = True # bool | if false, return a full representation of the {@code GroupRepresentation} objects. (optional)
    first = 1 # int | first result to return. Ignored if negative or {@code null}. (optional)
    max = 1 # int | maximum number of results to return. Ignored if negative or {@code null}. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a stream of groups that have the specified role name
        api_response = api_instance.realm_roles_role_name_groups_get(realm, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a stream of groups that have the specified role name
        api_response = api_instance.realm_roles_role_name_groups_get(realm, role_name, brief_representation=brief_representation, first=first, max=max)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**| the role name. |
 **brief_representation** | **bool**| if false, return a full representation of the {@code GroupRepresentation} objects. | [optional]
 **first** | **int**| first result to return. Ignored if negative or {@code null}. | [optional]
 **max** | **int**| maximum number of results to return. Ignored if negative or {@code null}. | [optional]

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

# **realm_roles_role_name_management_permissions_get**
> ManagementPermissionReference realm_roles_role_name_management_permissions_get(realm, role_name)

Return object stating whether role Authorization permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.realm_roles_role_name_management_permissions_get(realm, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_management_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**|  |

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

# **realm_roles_role_name_management_permissions_put**
> ManagementPermissionReference realm_roles_role_name_management_permissions_put(realm, role_name, management_permission_reference)

Return object stating whether role Authorization permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | 
    management_permission_reference = ManagementPermissionReference(
        enabled=True,
        resource="resource_example",
        scope_permissions={},
    ) # ManagementPermissionReference | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether role Authorization permissions have been initialized or not and a reference
        api_response = api_instance.realm_roles_role_name_management_permissions_put(realm, role_name, management_permission_reference)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_management_permissions_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**|  |
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

# **realm_roles_role_name_put**
> realm_roles_role_name_put(realm, role_name, role_representation)

Update a role by name

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | role’s name (not id!)
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
        # Update a role by name
        api_instance.realm_roles_role_name_put(realm, role_name, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**| role’s name (not id!) |
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

# **realm_roles_role_name_users_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_roles_role_name_users_get(realm, role_name)

Returns a stream of users that have the specified role name.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import roles_api
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
    api_instance = roles_api.RolesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    role_name = "role-name_example" # str | the role name.
    first = 1 # int | first result to return. Ignored if negative or {@code null}. (optional)
    max = 1 # int | maximum number of results to return. Ignored if negative or {@code null}. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a stream of users that have the specified role name.
        api_response = api_instance.realm_roles_role_name_users_get(realm, role_name)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_users_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a stream of users that have the specified role name.
        api_response = api_instance.realm_roles_role_name_users_get(realm, role_name, first=first, max=max)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RolesApi->realm_roles_role_name_users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **role_name** | **str**| the role name. |
 **first** | **int**| first result to return. Ignored if negative or {@code null}. | [optional]
 **max** | **int**| maximum number of results to return. Ignored if negative or {@code null}. | [optional]

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

