# keycloak_api.ClientsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_clients_get**](ClientsApi.md#realm_clients_get) | **GET** /{realm}/clients | Get clients belonging to the realm   Returns a list of clients belonging to the realm
[**realm_clients_id_client_secret_get**](ClientsApi.md#realm_clients_id_client_secret_get) | **GET** /{realm}/clients/{id}/client-secret | Get the client secret
[**realm_clients_id_client_secret_post**](ClientsApi.md#realm_clients_id_client_secret_post) | **POST** /{realm}/clients/{id}/client-secret | Generate a new secret for the client
[**realm_clients_id_default_client_scopes_client_scope_id_delete**](ClientsApi.md#realm_clients_id_default_client_scopes_client_scope_id_delete) | **DELETE** /{realm}/clients/{id}/default-client-scopes/{clientScopeId} | 
[**realm_clients_id_default_client_scopes_client_scope_id_put**](ClientsApi.md#realm_clients_id_default_client_scopes_client_scope_id_put) | **PUT** /{realm}/clients/{id}/default-client-scopes/{clientScopeId} | 
[**realm_clients_id_default_client_scopes_get**](ClientsApi.md#realm_clients_id_default_client_scopes_get) | **GET** /{realm}/clients/{id}/default-client-scopes | Get default client scopes.
[**realm_clients_id_delete**](ClientsApi.md#realm_clients_id_delete) | **DELETE** /{realm}/clients/{id} | Delete the client
[**realm_clients_id_evaluate_scopes_generate_example_access_token_get**](ClientsApi.md#realm_clients_id_evaluate_scopes_generate_example_access_token_get) | **GET** /{realm}/clients/{id}/evaluate-scopes/generate-example-access-token | Create JSON with payload of example access token
[**realm_clients_id_evaluate_scopes_generate_example_id_token_get**](ClientsApi.md#realm_clients_id_evaluate_scopes_generate_example_id_token_get) | **GET** /{realm}/clients/{id}/evaluate-scopes/generate-example-id-token | Create JSON with payload of example id token
[**realm_clients_id_evaluate_scopes_generate_example_userinfo_get**](ClientsApi.md#realm_clients_id_evaluate_scopes_generate_example_userinfo_get) | **GET** /{realm}/clients/{id}/evaluate-scopes/generate-example-userinfo | Create JSON with payload of example user info
[**realm_clients_id_evaluate_scopes_protocol_mappers_get**](ClientsApi.md#realm_clients_id_evaluate_scopes_protocol_mappers_get) | **GET** /{realm}/clients/{id}/evaluate-scopes/protocol-mappers | Return list of all protocol mappers, which will be used when generating tokens issued for particular client.
[**realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get**](ClientsApi.md#realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get) | **GET** /{realm}/clients/{id}/evaluate-scopes/scope-mappings/{roleContainerId}/granted | Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.
[**realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get**](ClientsApi.md#realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get) | **GET** /{realm}/clients/{id}/evaluate-scopes/scope-mappings/{roleContainerId}/not-granted | Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him.
[**realm_clients_id_get**](ClientsApi.md#realm_clients_id_get) | **GET** /{realm}/clients/{id} | Get representation of the client
[**realm_clients_id_installation_providers_provider_id_get**](ClientsApi.md#realm_clients_id_installation_providers_provider_id_get) | **GET** /{realm}/clients/{id}/installation/providers/{providerId} | 
[**realm_clients_id_management_permissions_get**](ClientsApi.md#realm_clients_id_management_permissions_get) | **GET** /{realm}/clients/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realm_clients_id_management_permissions_put**](ClientsApi.md#realm_clients_id_management_permissions_put) | **PUT** /{realm}/clients/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realm_clients_id_nodes_node_delete**](ClientsApi.md#realm_clients_id_nodes_node_delete) | **DELETE** /{realm}/clients/{id}/nodes/{node} | Unregister a cluster node from the client
[**realm_clients_id_nodes_post**](ClientsApi.md#realm_clients_id_nodes_post) | **POST** /{realm}/clients/{id}/nodes | Register a cluster node with the client   Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle  by sending registration request to Keycloak
[**realm_clients_id_offline_session_count_get**](ClientsApi.md#realm_clients_id_offline_session_count_get) | **GET** /{realm}/clients/{id}/offline-session-count | Get application offline session count   Returns a number of offline user sessions associated with this client   {      \&quot;count\&quot;: number  }
[**realm_clients_id_offline_sessions_get**](ClientsApi.md#realm_clients_id_offline_sessions_get) | **GET** /{realm}/clients/{id}/offline-sessions | Get offline sessions for client   Returns a list of offline user sessions associated with this client
[**realm_clients_id_optional_client_scopes_client_scope_id_delete**](ClientsApi.md#realm_clients_id_optional_client_scopes_client_scope_id_delete) | **DELETE** /{realm}/clients/{id}/optional-client-scopes/{clientScopeId} | 
[**realm_clients_id_optional_client_scopes_client_scope_id_put**](ClientsApi.md#realm_clients_id_optional_client_scopes_client_scope_id_put) | **PUT** /{realm}/clients/{id}/optional-client-scopes/{clientScopeId} | 
[**realm_clients_id_optional_client_scopes_get**](ClientsApi.md#realm_clients_id_optional_client_scopes_get) | **GET** /{realm}/clients/{id}/optional-client-scopes | Get optional client scopes.
[**realm_clients_id_push_revocation_post**](ClientsApi.md#realm_clients_id_push_revocation_post) | **POST** /{realm}/clients/{id}/push-revocation | Push the client’s revocation policy to its admin URL   If the client has an admin URL, push revocation policy to it.
[**realm_clients_id_put**](ClientsApi.md#realm_clients_id_put) | **PUT** /{realm}/clients/{id} | Update the client
[**realm_clients_id_registration_access_token_post**](ClientsApi.md#realm_clients_id_registration_access_token_post) | **POST** /{realm}/clients/{id}/registration-access-token | Generate a new registration access token for the client
[**realm_clients_id_service_account_user_get**](ClientsApi.md#realm_clients_id_service_account_user_get) | **GET** /{realm}/clients/{id}/service-account-user | Get a user dedicated to the service account
[**realm_clients_id_session_count_get**](ClientsApi.md#realm_clients_id_session_count_get) | **GET** /{realm}/clients/{id}/session-count | Get application session count   Returns a number of user sessions associated with this client   {      \&quot;count\&quot;: number  }
[**realm_clients_id_test_nodes_available_get**](ClientsApi.md#realm_clients_id_test_nodes_available_get) | **GET** /{realm}/clients/{id}/test-nodes-available | Test if registered cluster nodes are available   Tests availability by sending &#39;ping&#39; request to all cluster nodes.
[**realm_clients_id_user_sessions_get**](ClientsApi.md#realm_clients_id_user_sessions_get) | **GET** /{realm}/clients/{id}/user-sessions | Get user sessions for client   Returns a list of user sessions associated with this client
[**realm_clients_post**](ClientsApi.md#realm_clients_post) | **POST** /{realm}/clients | Create a new client   Client’s client_id must be unique!


# **realm_clients_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_get(realm)

Get clients belonging to the realm   Returns a list of clients belonging to the realm

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client_id = "clientId_example" # str | filter by clientId (optional)
    first = 1 # int | the first result (optional)
    max = 1 # int | the max results to return (optional)
    q = "q_example" # str |  (optional)
    search = True # bool | whether this is a search query or a getClientById query (optional)
    viewable_only = True # bool | filter clients that cannot be viewed in full by admin (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get clients belonging to the realm   Returns a list of clients belonging to the realm
        api_response = api_instance.realm_clients_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get clients belonging to the realm   Returns a list of clients belonging to the realm
        api_response = api_instance.realm_clients_get(realm, client_id=client_id, first=first, max=max, q=q, search=search, viewable_only=viewable_only)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client_id** | **str**| filter by clientId | [optional]
 **first** | **int**| the first result | [optional]
 **max** | **int**| the max results to return | [optional]
 **q** | **str**|  | [optional]
 **search** | **bool**| whether this is a search query or a getClientById query | [optional]
 **viewable_only** | **bool**| filter clients that cannot be viewed in full by admin | [optional]

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

# **realm_clients_id_client_secret_get**
> CredentialRepresentation realm_clients_id_client_secret_get(realm, id)

Get the client secret

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.credential_representation import CredentialRepresentation
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Get the client secret
        api_response = api_instance.realm_clients_id_client_secret_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_client_secret_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

### Return type

[**CredentialRepresentation**](CredentialRepresentation.md)

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

# **realm_clients_id_client_secret_post**
> CredentialRepresentation realm_clients_id_client_secret_post(realm, id)

Generate a new secret for the client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.credential_representation import CredentialRepresentation
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Generate a new secret for the client
        api_response = api_instance.realm_clients_id_client_secret_post(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_client_secret_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

### Return type

[**CredentialRepresentation**](CredentialRepresentation.md)

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

# **realm_clients_id_default_client_scopes_client_scope_id_delete**
> realm_clients_id_default_client_scopes_client_scope_id_delete(realm, id, client_scope_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    client_scope_id = "clientScopeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_clients_id_default_client_scopes_client_scope_id_delete(realm, id, client_scope_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_default_client_scopes_client_scope_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **client_scope_id** | **str**|  |

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

# **realm_clients_id_default_client_scopes_client_scope_id_put**
> realm_clients_id_default_client_scopes_client_scope_id_put(realm, id, client_scope_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    client_scope_id = "clientScopeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_clients_id_default_client_scopes_client_scope_id_put(realm, id, client_scope_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_default_client_scopes_client_scope_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **client_scope_id** | **str**|  |

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

# **realm_clients_id_default_client_scopes_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_default_client_scopes_get(realm, id)

Get default client scopes.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Get default client scopes.
        api_response = api_instance.realm_clients_id_default_client_scopes_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_default_client_scopes_get: %s\n" % e)
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

# **realm_clients_id_delete**
> realm_clients_id_delete(realm, id)

Delete the client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Delete the client
        api_instance.realm_clients_id_delete(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

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

# **realm_clients_id_evaluate_scopes_generate_example_access_token_get**
> AccessToken realm_clients_id_evaluate_scopes_generate_example_access_token_get(realm, id)

Create JSON with payload of example access token

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.access_token import AccessToken
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    scope = "scope_example" # str |  (optional)
    user_id = "userId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create JSON with payload of example access token
        api_response = api_instance.realm_clients_id_evaluate_scopes_generate_example_access_token_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_generate_example_access_token_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create JSON with payload of example access token
        api_response = api_instance.realm_clients_id_evaluate_scopes_generate_example_access_token_get(realm, id, scope=scope, user_id=user_id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_generate_example_access_token_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **scope** | **str**|  | [optional]
 **user_id** | **str**|  | [optional]

### Return type

[**AccessToken**](AccessToken.md)

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

# **realm_clients_id_evaluate_scopes_generate_example_id_token_get**
> IDToken realm_clients_id_evaluate_scopes_generate_example_id_token_get(realm, id)

Create JSON with payload of example id token

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.id_token import IDToken
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    scope = "scope_example" # str |  (optional)
    user_id = "userId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create JSON with payload of example id token
        api_response = api_instance.realm_clients_id_evaluate_scopes_generate_example_id_token_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_generate_example_id_token_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create JSON with payload of example id token
        api_response = api_instance.realm_clients_id_evaluate_scopes_generate_example_id_token_get(realm, id, scope=scope, user_id=user_id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_generate_example_id_token_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **scope** | **str**|  | [optional]
 **user_id** | **str**|  | [optional]

### Return type

[**IDToken**](IDToken.md)

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

# **realm_clients_id_evaluate_scopes_generate_example_userinfo_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} realm_clients_id_evaluate_scopes_generate_example_userinfo_get(realm, id)

Create JSON with payload of example user info

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    scope = "scope_example" # str |  (optional)
    user_id = "userId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create JSON with payload of example user info
        api_response = api_instance.realm_clients_id_evaluate_scopes_generate_example_userinfo_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_generate_example_userinfo_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create JSON with payload of example user info
        api_response = api_instance.realm_clients_id_evaluate_scopes_generate_example_userinfo_get(realm, id, scope=scope, user_id=user_id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_generate_example_userinfo_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **scope** | **str**|  | [optional]
 **user_id** | **str**|  | [optional]

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

# **realm_clients_id_evaluate_scopes_protocol_mappers_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_evaluate_scopes_protocol_mappers_get(realm, id)

Return list of all protocol mappers, which will be used when generating tokens issued for particular client.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    scope = "scope_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return list of all protocol mappers, which will be used when generating tokens issued for particular client.
        api_response = api_instance.realm_clients_id_evaluate_scopes_protocol_mappers_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_protocol_mappers_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return list of all protocol mappers, which will be used when generating tokens issued for particular client.
        api_response = api_instance.realm_clients_id_evaluate_scopes_protocol_mappers_get(realm, id, scope=scope)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_protocol_mappers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **scope** | **str**|  | [optional]

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

# **realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get(realm, id, role_container_id)

Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_container_id = "roleContainerId_example" # str | either realm name OR client UUID
    scope = "scope_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.
        api_response = api_instance.realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get(realm, id, role_container_id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.
        api_response = api_instance.realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get(realm, id, role_container_id, scope=scope)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_container_id** | **str**| either realm name OR client UUID |
 **scope** | **str**|  | [optional]

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

# **realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get(realm, id, role_container_id)

Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    role_container_id = "roleContainerId_example" # str | either realm name OR client UUID
    scope = "scope_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him.
        api_response = api_instance.realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get(realm, id, role_container_id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him.
        api_response = api_instance.realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get(realm, id, role_container_id, scope=scope)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **role_container_id** | **str**| either realm name OR client UUID |
 **scope** | **str**|  | [optional]

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

# **realm_clients_id_get**
> ClientRepresentation realm_clients_id_get(realm, id)

Get representation of the client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.client_representation import ClientRepresentation
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Get representation of the client
        api_response = api_instance.realm_clients_id_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

### Return type

[**ClientRepresentation**](ClientRepresentation.md)

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

# **realm_clients_id_installation_providers_provider_id_get**
> realm_clients_id_installation_providers_provider_id_get(realm, id, provider_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    provider_id = "providerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_clients_id_installation_providers_provider_id_get(realm, id, provider_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_installation_providers_provider_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **provider_id** | **str**|  |

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

# **realm_clients_id_management_permissions_get**
> ManagementPermissionReference realm_clients_id_management_permissions_get(realm, id)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.realm_clients_id_management_permissions_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_management_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

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

# **realm_clients_id_management_permissions_put**
> ManagementPermissionReference realm_clients_id_management_permissions_put(realm, id, management_permission_reference)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    management_permission_reference = ManagementPermissionReference(
        enabled=True,
        resource="resource_example",
        scope_permissions={},
    ) # ManagementPermissionReference | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.realm_clients_id_management_permissions_put(realm, id, management_permission_reference)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_management_permissions_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
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

# **realm_clients_id_nodes_node_delete**
> realm_clients_id_nodes_node_delete(realm, id, node)

Unregister a cluster node from the client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    node = "node_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unregister a cluster node from the client
        api_instance.realm_clients_id_nodes_node_delete(realm, id, node)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_nodes_node_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **node** | **str**|  |

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

# **realm_clients_id_nodes_post**
> realm_clients_id_nodes_post(realm, id, request_body)

Register a cluster node with the client   Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle  by sending registration request to Keycloak

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        # Register a cluster node with the client   Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle  by sending registration request to Keycloak
        api_instance.realm_clients_id_nodes_post(realm, id, request_body)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_nodes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

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

# **realm_clients_id_offline_session_count_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} realm_clients_id_offline_session_count_get(realm, id)

Get application offline session count   Returns a number of offline user sessions associated with this client   {      \"count\": number  }

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Get application offline session count   Returns a number of offline user sessions associated with this client   {      \"count\": number  }
        api_response = api_instance.realm_clients_id_offline_session_count_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_offline_session_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

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

# **realm_clients_id_offline_sessions_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_offline_sessions_get(realm, id)

Get offline sessions for client   Returns a list of offline user sessions associated with this client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    first = 1 # int | Paging offset (optional)
    max = 1 # int | Maximum results size (defaults to 100) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get offline sessions for client   Returns a list of offline user sessions associated with this client
        api_response = api_instance.realm_clients_id_offline_sessions_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_offline_sessions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get offline sessions for client   Returns a list of offline user sessions associated with this client
        api_response = api_instance.realm_clients_id_offline_sessions_get(realm, id, first=first, max=max)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_offline_sessions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **first** | **int**| Paging offset | [optional]
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

# **realm_clients_id_optional_client_scopes_client_scope_id_delete**
> realm_clients_id_optional_client_scopes_client_scope_id_delete(realm, id, client_scope_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    client_scope_id = "clientScopeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_clients_id_optional_client_scopes_client_scope_id_delete(realm, id, client_scope_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_optional_client_scopes_client_scope_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **client_scope_id** | **str**|  |

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

# **realm_clients_id_optional_client_scopes_client_scope_id_put**
> realm_clients_id_optional_client_scopes_client_scope_id_put(realm, id, client_scope_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    client_scope_id = "clientScopeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_clients_id_optional_client_scopes_client_scope_id_put(realm, id, client_scope_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_optional_client_scopes_client_scope_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **client_scope_id** | **str**|  |

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

# **realm_clients_id_optional_client_scopes_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_optional_client_scopes_get(realm, id)

Get optional client scopes.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Get optional client scopes.
        api_response = api_instance.realm_clients_id_optional_client_scopes_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_optional_client_scopes_get: %s\n" % e)
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

# **realm_clients_id_push_revocation_post**
> GlobalRequestResult realm_clients_id_push_revocation_post(realm, id)

Push the client’s revocation policy to its admin URL   If the client has an admin URL, push revocation policy to it.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.global_request_result import GlobalRequestResult
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Push the client’s revocation policy to its admin URL   If the client has an admin URL, push revocation policy to it.
        api_response = api_instance.realm_clients_id_push_revocation_post(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_push_revocation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

### Return type

[**GlobalRequestResult**](GlobalRequestResult.md)

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

# **realm_clients_id_put**
> realm_clients_id_put(realm, id, client_representation)

Update the client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.client_representation import ClientRepresentation
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    client_representation = ClientRepresentation(
        access={},
        admin_url="admin_url_example",
        always_display_in_console=True,
        attributes={},
        authentication_flow_binding_overrides={},
        authorization_services_enabled=True,
        authorization_settings=ResourceServerRepresentation(
            allow_remote_resource_management=True,
            client_id="client_id_example",
            decision_strategy="AFFIRMATIVE",
            id="id_example",
            name="name_example",
            policies=[
                PolicyRepresentation(
                    config={},
                    decision_strategy="AFFIRMATIVE",
                    description="description_example",
                    id="id_example",
                    logic="POSITIVE",
                    name="name_example",
                    owner="owner_example",
                    policies=[
                        "policies_example",
                    ],
                    resources=[
                        "resources_example",
                    ],
                    resources_data=[
                        ResourceRepresentation(
                            id="id_example",
                            attributes={},
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            name="name_example",
                            owner_managed_access=True,
                            scopes=[
                                ScopeRepresentation(
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    id="id_example",
                                    name="name_example",
                                    policies=[],
                                    resources=[],
                                ),
                            ],
                            type="type_example",
                            uris=[
                                "uris_example",
                            ],
                        ),
                    ],
                    scopes=[
                        "scopes_example",
                    ],
                    scopes_data=[
                        ScopeRepresentation(
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            id="id_example",
                            name="name_example",
                            policies=[],
                            resources=[
                                ResourceRepresentation(
                                    id="id_example",
                                    attributes={},
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    name="name_example",
                                    owner_managed_access=True,
                                    scopes=[],
                                    type="type_example",
                                    uris=[
                                        "uris_example",
                                    ],
                                ),
                            ],
                        ),
                    ],
                    type="type_example",
                ),
            ],
            policy_enforcement_mode="ENFORCING",
            resources=[
                ResourceRepresentation(
                    id="id_example",
                    attributes={},
                    display_name="display_name_example",
                    icon_uri="icon_uri_example",
                    name="name_example",
                    owner_managed_access=True,
                    scopes=[
                        ScopeRepresentation(
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            id="id_example",
                            name="name_example",
                            policies=[
                                PolicyRepresentation(
                                    config={},
                                    decision_strategy="AFFIRMATIVE",
                                    description="description_example",
                                    id="id_example",
                                    logic="POSITIVE",
                                    name="name_example",
                                    owner="owner_example",
                                    policies=[
                                        "policies_example",
                                    ],
                                    resources=[
                                        "resources_example",
                                    ],
                                    resources_data=[],
                                    scopes=[
                                        "scopes_example",
                                    ],
                                    scopes_data=[],
                                    type="type_example",
                                ),
                            ],
                            resources=[],
                        ),
                    ],
                    type="type_example",
                    uris=[
                        "uris_example",
                    ],
                ),
            ],
            scopes=[
                ScopeRepresentation(
                    display_name="display_name_example",
                    icon_uri="icon_uri_example",
                    id="id_example",
                    name="name_example",
                    policies=[
                        PolicyRepresentation(
                            config={},
                            decision_strategy="AFFIRMATIVE",
                            description="description_example",
                            id="id_example",
                            logic="POSITIVE",
                            name="name_example",
                            owner="owner_example",
                            policies=[
                                "policies_example",
                            ],
                            resources=[
                                "resources_example",
                            ],
                            resources_data=[
                                ResourceRepresentation(
                                    id="id_example",
                                    attributes={},
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    name="name_example",
                                    owner_managed_access=True,
                                    scopes=[],
                                    type="type_example",
                                    uris=[
                                        "uris_example",
                                    ],
                                ),
                            ],
                            scopes=[
                                "scopes_example",
                            ],
                            scopes_data=[],
                            type="type_example",
                        ),
                    ],
                    resources=[
                        ResourceRepresentation(
                            id="id_example",
                            attributes={},
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            name="name_example",
                            owner_managed_access=True,
                            scopes=[],
                            type="type_example",
                            uris=[
                                "uris_example",
                            ],
                        ),
                    ],
                ),
            ],
        ),
        base_url="base_url_example",
        bearer_only=True,
        client_authenticator_type="client_authenticator_type_example",
        client_id="client_id_example",
        consent_required=True,
        default_client_scopes=[
            "default_client_scopes_example",
        ],
        description="description_example",
        direct_access_grants_enabled=True,
        enabled=True,
        frontchannel_logout=True,
        full_scope_allowed=True,
        id="id_example",
        implicit_flow_enabled=True,
        name="name_example",
        node_re_registration_timeout=1,
        not_before=1,
        oauth2_device_authorization_grant_enabled=True,
        optional_client_scopes=[
            "optional_client_scopes_example",
        ],
        origin="origin_example",
        protocol="protocol_example",
        protocol_mappers=[
            ProtocolMapperRepresentation(
                config={},
                id="id_example",
                name="name_example",
                protocol="protocol_example",
                protocol_mapper="protocol_mapper_example",
            ),
        ],
        public_client=True,
        redirect_uris=[
            "redirect_uris_example",
        ],
        registered_nodes={},
        registration_access_token="registration_access_token_example",
        root_url="root_url_example",
        secret="secret_example",
        service_accounts_enabled=True,
        standard_flow_enabled=True,
        surrogate_auth_required=True,
        web_origins=[
            "web_origins_example",
        ],
    ) # ClientRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update the client
        api_instance.realm_clients_id_put(realm, id, client_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **client_representation** | [**ClientRepresentation**](ClientRepresentation.md)|  |

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

# **realm_clients_id_registration_access_token_post**
> ClientRepresentation realm_clients_id_registration_access_token_post(realm, id)

Generate a new registration access token for the client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.client_representation import ClientRepresentation
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Generate a new registration access token for the client
        api_response = api_instance.realm_clients_id_registration_access_token_post(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_registration_access_token_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

### Return type

[**ClientRepresentation**](ClientRepresentation.md)

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

# **realm_clients_id_service_account_user_get**
> UserRepresentation realm_clients_id_service_account_user_get(realm, id)

Get a user dedicated to the service account

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.user_representation import UserRepresentation
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Get a user dedicated to the service account
        api_response = api_instance.realm_clients_id_service_account_user_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_service_account_user_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

### Return type

[**UserRepresentation**](UserRepresentation.md)

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

# **realm_clients_id_session_count_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} realm_clients_id_session_count_get(realm, id)

Get application session count   Returns a number of user sessions associated with this client   {      \"count\": number  }

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Get application session count   Returns a number of user sessions associated with this client   {      \"count\": number  }
        api_response = api_instance.realm_clients_id_session_count_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_session_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

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

# **realm_clients_id_test_nodes_available_get**
> GlobalRequestResult realm_clients_id_test_nodes_available_get(realm, id)

Test if registered cluster nodes are available   Tests availability by sending 'ping' request to all cluster nodes.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.global_request_result import GlobalRequestResult
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Test if registered cluster nodes are available   Tests availability by sending 'ping' request to all cluster nodes.
        api_response = api_instance.realm_clients_id_test_nodes_available_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_test_nodes_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |

### Return type

[**GlobalRequestResult**](GlobalRequestResult.md)

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

# **realm_clients_id_user_sessions_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_user_sessions_get(realm, id)

Get user sessions for client   Returns a list of user sessions associated with this client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    first = 1 # int | Paging offset (optional)
    max = 1 # int | Maximum results size (defaults to 100) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get user sessions for client   Returns a list of user sessions associated with this client
        api_response = api_instance.realm_clients_id_user_sessions_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_user_sessions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get user sessions for client   Returns a list of user sessions associated with this client
        api_response = api_instance.realm_clients_id_user_sessions_get(realm, id, first=first, max=max)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_id_user_sessions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **first** | **int**| Paging offset | [optional]
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

# **realm_clients_post**
> realm_clients_post(realm, client_representation)

Create a new client   Client’s client_id must be unique!

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import clients_api
from keycloak_api.model.client_representation import ClientRepresentation
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
    api_instance = clients_api.ClientsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client_representation = ClientRepresentation(
        access={},
        admin_url="admin_url_example",
        always_display_in_console=True,
        attributes={},
        authentication_flow_binding_overrides={},
        authorization_services_enabled=True,
        authorization_settings=ResourceServerRepresentation(
            allow_remote_resource_management=True,
            client_id="client_id_example",
            decision_strategy="AFFIRMATIVE",
            id="id_example",
            name="name_example",
            policies=[
                PolicyRepresentation(
                    config={},
                    decision_strategy="AFFIRMATIVE",
                    description="description_example",
                    id="id_example",
                    logic="POSITIVE",
                    name="name_example",
                    owner="owner_example",
                    policies=[
                        "policies_example",
                    ],
                    resources=[
                        "resources_example",
                    ],
                    resources_data=[
                        ResourceRepresentation(
                            id="id_example",
                            attributes={},
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            name="name_example",
                            owner_managed_access=True,
                            scopes=[
                                ScopeRepresentation(
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    id="id_example",
                                    name="name_example",
                                    policies=[],
                                    resources=[],
                                ),
                            ],
                            type="type_example",
                            uris=[
                                "uris_example",
                            ],
                        ),
                    ],
                    scopes=[
                        "scopes_example",
                    ],
                    scopes_data=[
                        ScopeRepresentation(
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            id="id_example",
                            name="name_example",
                            policies=[],
                            resources=[
                                ResourceRepresentation(
                                    id="id_example",
                                    attributes={},
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    name="name_example",
                                    owner_managed_access=True,
                                    scopes=[],
                                    type="type_example",
                                    uris=[
                                        "uris_example",
                                    ],
                                ),
                            ],
                        ),
                    ],
                    type="type_example",
                ),
            ],
            policy_enforcement_mode="ENFORCING",
            resources=[
                ResourceRepresentation(
                    id="id_example",
                    attributes={},
                    display_name="display_name_example",
                    icon_uri="icon_uri_example",
                    name="name_example",
                    owner_managed_access=True,
                    scopes=[
                        ScopeRepresentation(
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            id="id_example",
                            name="name_example",
                            policies=[
                                PolicyRepresentation(
                                    config={},
                                    decision_strategy="AFFIRMATIVE",
                                    description="description_example",
                                    id="id_example",
                                    logic="POSITIVE",
                                    name="name_example",
                                    owner="owner_example",
                                    policies=[
                                        "policies_example",
                                    ],
                                    resources=[
                                        "resources_example",
                                    ],
                                    resources_data=[],
                                    scopes=[
                                        "scopes_example",
                                    ],
                                    scopes_data=[],
                                    type="type_example",
                                ),
                            ],
                            resources=[],
                        ),
                    ],
                    type="type_example",
                    uris=[
                        "uris_example",
                    ],
                ),
            ],
            scopes=[
                ScopeRepresentation(
                    display_name="display_name_example",
                    icon_uri="icon_uri_example",
                    id="id_example",
                    name="name_example",
                    policies=[
                        PolicyRepresentation(
                            config={},
                            decision_strategy="AFFIRMATIVE",
                            description="description_example",
                            id="id_example",
                            logic="POSITIVE",
                            name="name_example",
                            owner="owner_example",
                            policies=[
                                "policies_example",
                            ],
                            resources=[
                                "resources_example",
                            ],
                            resources_data=[
                                ResourceRepresentation(
                                    id="id_example",
                                    attributes={},
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    name="name_example",
                                    owner_managed_access=True,
                                    scopes=[],
                                    type="type_example",
                                    uris=[
                                        "uris_example",
                                    ],
                                ),
                            ],
                            scopes=[
                                "scopes_example",
                            ],
                            scopes_data=[],
                            type="type_example",
                        ),
                    ],
                    resources=[
                        ResourceRepresentation(
                            id="id_example",
                            attributes={},
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            name="name_example",
                            owner_managed_access=True,
                            scopes=[],
                            type="type_example",
                            uris=[
                                "uris_example",
                            ],
                        ),
                    ],
                ),
            ],
        ),
        base_url="base_url_example",
        bearer_only=True,
        client_authenticator_type="client_authenticator_type_example",
        client_id="client_id_example",
        consent_required=True,
        default_client_scopes=[
            "default_client_scopes_example",
        ],
        description="description_example",
        direct_access_grants_enabled=True,
        enabled=True,
        frontchannel_logout=True,
        full_scope_allowed=True,
        id="id_example",
        implicit_flow_enabled=True,
        name="name_example",
        node_re_registration_timeout=1,
        not_before=1,
        oauth2_device_authorization_grant_enabled=True,
        optional_client_scopes=[
            "optional_client_scopes_example",
        ],
        origin="origin_example",
        protocol="protocol_example",
        protocol_mappers=[
            ProtocolMapperRepresentation(
                config={},
                id="id_example",
                name="name_example",
                protocol="protocol_example",
                protocol_mapper="protocol_mapper_example",
            ),
        ],
        public_client=True,
        redirect_uris=[
            "redirect_uris_example",
        ],
        registered_nodes={},
        registration_access_token="registration_access_token_example",
        root_url="root_url_example",
        secret="secret_example",
        service_accounts_enabled=True,
        standard_flow_enabled=True,
        surrogate_auth_required=True,
        web_origins=[
            "web_origins_example",
        ],
    ) # ClientRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new client   Client’s client_id must be unique!
        api_instance.realm_clients_post(realm, client_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientsApi->realm_clients_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client_representation** | [**ClientRepresentation**](ClientRepresentation.md)|  |

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

