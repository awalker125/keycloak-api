# keycloak_api.ClientScopesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_client_scopes_get**](ClientScopesApi.md#realm_client_scopes_get) | **GET** /{realm}/client-scopes | Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm
[**realm_client_scopes_id_delete**](ClientScopesApi.md#realm_client_scopes_id_delete) | **DELETE** /{realm}/client-scopes/{id} | Delete the client scope
[**realm_client_scopes_id_get**](ClientScopesApi.md#realm_client_scopes_id_get) | **GET** /{realm}/client-scopes/{id} | Get representation of the client scope
[**realm_client_scopes_id_put**](ClientScopesApi.md#realm_client_scopes_id_put) | **PUT** /{realm}/client-scopes/{id} | Update the client scope
[**realm_client_scopes_post**](ClientScopesApi.md#realm_client_scopes_post) | **POST** /{realm}/client-scopes | Create a new client scope   Client Scope’s name must be unique!


# **realm_client_scopes_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_scopes_get(realm)

Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_scopes_api
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
    api_instance = client_scopes_api.ClientScopesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm
        api_response = api_instance.realm_client_scopes_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientScopesApi->realm_client_scopes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

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

# **realm_client_scopes_id_delete**
> realm_client_scopes_id_delete(realm, id)

Delete the client scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_scopes_api
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
    api_instance = client_scopes_api.ClientScopesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)

    # example passing only required values which don't have defaults set
    try:
        # Delete the client scope
        api_instance.realm_client_scopes_id_delete(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientScopesApi->realm_client_scopes_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |

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

# **realm_client_scopes_id_get**
> ClientScopeRepresentation realm_client_scopes_id_get(realm, id)

Get representation of the client scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_scopes_api
from keycloak_api.model.client_scope_representation import ClientScopeRepresentation
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
    api_instance = client_scopes_api.ClientScopesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)

    # example passing only required values which don't have defaults set
    try:
        # Get representation of the client scope
        api_response = api_instance.realm_client_scopes_id_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientScopesApi->realm_client_scopes_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |

### Return type

[**ClientScopeRepresentation**](ClientScopeRepresentation.md)

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

# **realm_client_scopes_id_put**
> realm_client_scopes_id_put(realm, id, client_scope_representation)

Update the client scope

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_scopes_api
from keycloak_api.model.client_scope_representation import ClientScopeRepresentation
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
    api_instance = client_scopes_api.ClientScopesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
    client_scope_representation = ClientScopeRepresentation(
        attributes={},
        description="description_example",
        id="id_example",
        name="name_example",
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
    ) # ClientScopeRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update the client scope
        api_instance.realm_client_scopes_id_put(realm, id, client_scope_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientScopesApi->realm_client_scopes_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
 **client_scope_representation** | [**ClientScopeRepresentation**](ClientScopeRepresentation.md)|  |

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

# **realm_client_scopes_post**
> realm_client_scopes_post(realm, client_scope_representation)

Create a new client scope   Client Scope’s name must be unique!

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_scopes_api
from keycloak_api.model.client_scope_representation import ClientScopeRepresentation
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
    api_instance = client_scopes_api.ClientScopesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client_scope_representation = ClientScopeRepresentation(
        attributes={},
        description="description_example",
        id="id_example",
        name="name_example",
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
    ) # ClientScopeRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new client scope   Client Scope’s name must be unique!
        api_instance.realm_client_scopes_post(realm, client_scope_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientScopesApi->realm_client_scopes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client_scope_representation** | [**ClientScopeRepresentation**](ClientScopeRepresentation.md)|  |

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

