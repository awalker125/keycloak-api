# keycloak_api.ScopeMappingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_client_scopes_id_scope_mappings_clients_client_available_get**](ScopeMappingsApi.md#realm_client_scopes_id_scope_mappings_clients_client_available_get) | **GET** /{realm}/client-scopes/{id}/scope-mappings/clients/{client}/available | The available client-level roles   Returns the roles for the client that can be associated with the client’s scope
[**realm_client_scopes_id_scope_mappings_clients_client_composite_get**](ScopeMappingsApi.md#realm_client_scopes_id_scope_mappings_clients_client_composite_get) | **GET** /{realm}/client-scopes/{id}/scope-mappings/clients/{client}/composite | Get effective client roles   Returns the roles for the client that are associated with the client’s scope.
[**realm_client_scopes_id_scope_mappings_clients_client_delete**](ScopeMappingsApi.md#realm_client_scopes_id_scope_mappings_clients_client_delete) | **DELETE** /{realm}/client-scopes/{id}/scope-mappings/clients/{client} | Remove client-level roles from the client’s scope.
[**realm_client_scopes_id_scope_mappings_clients_client_get**](ScopeMappingsApi.md#realm_client_scopes_id_scope_mappings_clients_client_get) | **GET** /{realm}/client-scopes/{id}/scope-mappings/clients/{client} | Get the roles associated with a client’s scope   Returns roles for the client.
[**realm_client_scopes_id_scope_mappings_clients_client_post**](ScopeMappingsApi.md#realm_client_scopes_id_scope_mappings_clients_client_post) | **POST** /{realm}/client-scopes/{id}/scope-mappings/clients/{client} | Add client-level roles to the client’s scope
[**realm_client_scopes_id_scope_mappings_realm_available_get**](ScopeMappingsApi.md#realm_client_scopes_id_scope_mappings_realm_available_get) | **GET** /{realm}/client-scopes/{id}/scope-mappings/realm/available | Get realm-level roles that are available to attach to this client’s scope
[**realm_client_scopes_id_scope_mappings_realm_composite_get**](ScopeMappingsApi.md#realm_client_scopes_id_scope_mappings_realm_composite_get) | **GET** /{realm}/client-scopes/{id}/scope-mappings/realm/composite | Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.
[**realm_client_scopes_id_scope_mappings_realm_delete**](ScopeMappingsApi.md#realm_client_scopes_id_scope_mappings_realm_delete) | **DELETE** /{realm}/client-scopes/{id}/scope-mappings/realm | Remove a set of realm-level roles from the client’s scope
[**realm_client_scopes_id_scope_mappings_realm_get**](ScopeMappingsApi.md#realm_client_scopes_id_scope_mappings_realm_get) | **GET** /{realm}/client-scopes/{id}/scope-mappings/realm | Get realm-level roles associated with the client’s scope
[**realm_client_scopes_id_scope_mappings_realm_post**](ScopeMappingsApi.md#realm_client_scopes_id_scope_mappings_realm_post) | **POST** /{realm}/client-scopes/{id}/scope-mappings/realm | Add a set of realm-level roles to the client’s scope
[**realm_clients_id_scope_mappings_clients_client_available_get**](ScopeMappingsApi.md#realm_clients_id_scope_mappings_clients_client_available_get) | **GET** /{realm}/clients/{id}/scope-mappings/clients/{client}/available | The available client-level roles   Returns the roles for the client that can be associated with the client’s scope
[**realm_clients_id_scope_mappings_clients_client_composite_get**](ScopeMappingsApi.md#realm_clients_id_scope_mappings_clients_client_composite_get) | **GET** /{realm}/clients/{id}/scope-mappings/clients/{client}/composite | Get effective client roles   Returns the roles for the client that are associated with the client’s scope.
[**realm_clients_id_scope_mappings_clients_client_delete**](ScopeMappingsApi.md#realm_clients_id_scope_mappings_clients_client_delete) | **DELETE** /{realm}/clients/{id}/scope-mappings/clients/{client} | Remove client-level roles from the client’s scope.
[**realm_clients_id_scope_mappings_clients_client_get**](ScopeMappingsApi.md#realm_clients_id_scope_mappings_clients_client_get) | **GET** /{realm}/clients/{id}/scope-mappings/clients/{client} | Get the roles associated with a client’s scope   Returns roles for the client.
[**realm_clients_id_scope_mappings_clients_client_post**](ScopeMappingsApi.md#realm_clients_id_scope_mappings_clients_client_post) | **POST** /{realm}/clients/{id}/scope-mappings/clients/{client} | Add client-level roles to the client’s scope
[**realm_clients_id_scope_mappings_realm_available_get**](ScopeMappingsApi.md#realm_clients_id_scope_mappings_realm_available_get) | **GET** /{realm}/clients/{id}/scope-mappings/realm/available | Get realm-level roles that are available to attach to this client’s scope
[**realm_clients_id_scope_mappings_realm_composite_get**](ScopeMappingsApi.md#realm_clients_id_scope_mappings_realm_composite_get) | **GET** /{realm}/clients/{id}/scope-mappings/realm/composite | Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.
[**realm_clients_id_scope_mappings_realm_delete**](ScopeMappingsApi.md#realm_clients_id_scope_mappings_realm_delete) | **DELETE** /{realm}/clients/{id}/scope-mappings/realm | Remove a set of realm-level roles from the client’s scope
[**realm_clients_id_scope_mappings_realm_get**](ScopeMappingsApi.md#realm_clients_id_scope_mappings_realm_get) | **GET** /{realm}/clients/{id}/scope-mappings/realm | Get realm-level roles associated with the client’s scope
[**realm_clients_id_scope_mappings_realm_post**](ScopeMappingsApi.md#realm_clients_id_scope_mappings_realm_post) | **POST** /{realm}/clients/{id}/scope-mappings/realm | Add a set of realm-level roles to the client’s scope


# **realm_client_scopes_id_scope_mappings_clients_client_available_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_scopes_id_scope_mappings_clients_client_available_get(realm, id, client)

The available client-level roles   Returns the roles for the client that can be associated with the client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
    client = "client_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The available client-level roles   Returns the roles for the client that can be associated with the client’s scope
        api_response = api_instance.realm_client_scopes_id_scope_mappings_clients_client_available_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_clients_client_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
 **client** | **str**|  |

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

# **realm_client_scopes_id_scope_mappings_clients_client_composite_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_scopes_id_scope_mappings_clients_client_composite_get(realm, id, client)

Get effective client roles   Returns the roles for the client that are associated with the client’s scope.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
    client = "client_example" # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get effective client roles   Returns the roles for the client that are associated with the client’s scope.
        api_response = api_instance.realm_client_scopes_id_scope_mappings_clients_client_composite_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_clients_client_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective client roles   Returns the roles for the client that are associated with the client’s scope.
        api_response = api_instance.realm_client_scopes_id_scope_mappings_clients_client_composite_get(realm, id, client, brief_representation=brief_representation)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_clients_client_composite_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
 **client** | **str**|  |
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

# **realm_client_scopes_id_scope_mappings_clients_client_delete**
> realm_client_scopes_id_scope_mappings_clients_client_delete(realm, id, client, role_representation)

Remove client-level roles from the client’s scope.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
    client = "client_example" # str | 
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
        # Remove client-level roles from the client’s scope.
        api_instance.realm_client_scopes_id_scope_mappings_clients_client_delete(realm, id, client, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_clients_client_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
 **client** | **str**|  |
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

# **realm_client_scopes_id_scope_mappings_clients_client_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_scopes_id_scope_mappings_clients_client_get(realm, id, client)

Get the roles associated with a client’s scope   Returns roles for the client.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
    client = "client_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the roles associated with a client’s scope   Returns roles for the client.
        api_response = api_instance.realm_client_scopes_id_scope_mappings_clients_client_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_clients_client_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
 **client** | **str**|  |

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

# **realm_client_scopes_id_scope_mappings_clients_client_post**
> realm_client_scopes_id_scope_mappings_clients_client_post(realm, id, client, role_representation)

Add client-level roles to the client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
    client = "client_example" # str | 
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
        # Add client-level roles to the client’s scope
        api_instance.realm_client_scopes_id_scope_mappings_clients_client_post(realm, id, client, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_clients_client_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
 **client** | **str**|  |
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

# **realm_client_scopes_id_scope_mappings_realm_available_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_scopes_id_scope_mappings_realm_available_get(realm, id)

Get realm-level roles that are available to attach to this client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that are available to attach to this client’s scope
        api_response = api_instance.realm_client_scopes_id_scope_mappings_realm_available_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_realm_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |

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

# **realm_client_scopes_id_scope_mappings_realm_composite_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_scopes_id_scope_mappings_realm_composite_get(realm, id)

Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
    brief_representation = True # bool | if false, return roles with their attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.
        api_response = api_instance.realm_client_scopes_id_scope_mappings_realm_composite_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_realm_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.
        api_response = api_instance.realm_client_scopes_id_scope_mappings_realm_composite_get(realm, id, brief_representation=brief_representation)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_realm_composite_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
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

# **realm_client_scopes_id_scope_mappings_realm_delete**
> realm_client_scopes_id_scope_mappings_realm_delete(realm, id, role_representation)

Remove a set of realm-level roles from the client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
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
        # Remove a set of realm-level roles from the client’s scope
        api_instance.realm_client_scopes_id_scope_mappings_realm_delete(realm, id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_realm_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
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

# **realm_client_scopes_id_scope_mappings_realm_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_scopes_id_scope_mappings_realm_get(realm, id)

Get realm-level roles associated with the client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles associated with the client’s scope
        api_response = api_instance.realm_client_scopes_id_scope_mappings_realm_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_realm_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |

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

# **realm_client_scopes_id_scope_mappings_realm_post**
> realm_client_scopes_id_scope_mappings_realm_post(realm, id, role_representation)

Add a set of realm-level roles to the client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
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
        # Add a set of realm-level roles to the client’s scope
        api_instance.realm_client_scopes_id_scope_mappings_realm_post(realm, id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_client_scopes_id_scope_mappings_realm_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
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

# **realm_clients_id_scope_mappings_clients_client_available_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_scope_mappings_clients_client_available_get(realm, id, client)

The available client-level roles   Returns the roles for the client that can be associated with the client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    client = "client_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # The available client-level roles   Returns the roles for the client that can be associated with the client’s scope
        api_response = api_instance.realm_clients_id_scope_mappings_clients_client_available_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_clients_client_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **client** | **str**|  |

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

# **realm_clients_id_scope_mappings_clients_client_composite_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_scope_mappings_clients_client_composite_get(realm, id, client)

Get effective client roles   Returns the roles for the client that are associated with the client’s scope.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    client = "client_example" # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get effective client roles   Returns the roles for the client that are associated with the client’s scope.
        api_response = api_instance.realm_clients_id_scope_mappings_clients_client_composite_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_clients_client_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective client roles   Returns the roles for the client that are associated with the client’s scope.
        api_response = api_instance.realm_clients_id_scope_mappings_clients_client_composite_get(realm, id, client, brief_representation=brief_representation)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_clients_client_composite_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **client** | **str**|  |
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

# **realm_clients_id_scope_mappings_clients_client_delete**
> realm_clients_id_scope_mappings_clients_client_delete(realm, id, client, role_representation)

Remove client-level roles from the client’s scope.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    client = "client_example" # str | 
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
        # Remove client-level roles from the client’s scope.
        api_instance.realm_clients_id_scope_mappings_clients_client_delete(realm, id, client, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_clients_client_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **client** | **str**|  |
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

# **realm_clients_id_scope_mappings_clients_client_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_scope_mappings_clients_client_get(realm, id, client)

Get the roles associated with a client’s scope   Returns roles for the client.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    client = "client_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the roles associated with a client’s scope   Returns roles for the client.
        api_response = api_instance.realm_clients_id_scope_mappings_clients_client_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_clients_client_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **client** | **str**|  |

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

# **realm_clients_id_scope_mappings_clients_client_post**
> realm_clients_id_scope_mappings_clients_client_post(realm, id, client, role_representation)

Add client-level roles to the client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    client = "client_example" # str | 
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
        # Add client-level roles to the client’s scope
        api_instance.realm_clients_id_scope_mappings_clients_client_post(realm, id, client, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_clients_client_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **client** | **str**|  |
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

# **realm_clients_id_scope_mappings_realm_available_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_scope_mappings_realm_available_get(realm, id)

Get realm-level roles that are available to attach to this client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles that are available to attach to this client’s scope
        api_response = api_instance.realm_clients_id_scope_mappings_realm_available_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_realm_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

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

# **realm_clients_id_scope_mappings_realm_composite_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_scope_mappings_realm_composite_get(realm, id)

Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    brief_representation = True # bool | if false, return roles with their attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.
        api_response = api_instance.realm_clients_id_scope_mappings_realm_composite_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_realm_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.
        api_response = api_instance.realm_clients_id_scope_mappings_realm_composite_get(realm, id, brief_representation=brief_representation)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_realm_composite_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
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

# **realm_clients_id_scope_mappings_realm_delete**
> realm_clients_id_scope_mappings_realm_delete(realm, id, role_representation)

Remove a set of realm-level roles from the client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
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
        # Remove a set of realm-level roles from the client’s scope
        api_instance.realm_clients_id_scope_mappings_realm_delete(realm, id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_realm_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
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

# **realm_clients_id_scope_mappings_realm_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_scope_mappings_realm_get(realm, id)

Get realm-level roles associated with the client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Get realm-level roles associated with the client’s scope
        api_response = api_instance.realm_clients_id_scope_mappings_realm_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_realm_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

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

# **realm_clients_id_scope_mappings_realm_post**
> realm_clients_id_scope_mappings_realm_post(realm, id, role_representation)

Add a set of realm-level roles to the client’s scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import scope_mappings_api
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
    api_instance = scope_mappings_api.ScopeMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
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
        # Add a set of realm-level roles to the client’s scope
        api_instance.realm_clients_id_scope_mappings_realm_post(realm, id, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ScopeMappingsApi->realm_clients_id_scope_mappings_realm_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
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

