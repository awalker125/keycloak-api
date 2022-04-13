# keycloak_api.ClientRoleMappingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_groups_id_role_mappings_clients_client_available_get**](ClientRoleMappingsApi.md#realm_groups_id_role_mappings_clients_client_available_get) | **GET** /{realm}/groups/{id}/role-mappings/clients/{client}/available | Get available client-level roles that can be mapped to the user
[**realm_groups_id_role_mappings_clients_client_composite_get**](ClientRoleMappingsApi.md#realm_groups_id_role_mappings_clients_client_composite_get) | **GET** /{realm}/groups/{id}/role-mappings/clients/{client}/composite | Get effective client-level role mappings   This recurses any composite roles
[**realm_groups_id_role_mappings_clients_client_delete**](ClientRoleMappingsApi.md#realm_groups_id_role_mappings_clients_client_delete) | **DELETE** /{realm}/groups/{id}/role-mappings/clients/{client} | Delete client-level roles from user role mapping
[**realm_groups_id_role_mappings_clients_client_get**](ClientRoleMappingsApi.md#realm_groups_id_role_mappings_clients_client_get) | **GET** /{realm}/groups/{id}/role-mappings/clients/{client} | Get client-level role mappings for the user, and the app
[**realm_groups_id_role_mappings_clients_client_post**](ClientRoleMappingsApi.md#realm_groups_id_role_mappings_clients_client_post) | **POST** /{realm}/groups/{id}/role-mappings/clients/{client} | Add client-level roles to the user role mapping
[**realm_users_id_role_mappings_clients_client_available_get**](ClientRoleMappingsApi.md#realm_users_id_role_mappings_clients_client_available_get) | **GET** /{realm}/users/{id}/role-mappings/clients/{client}/available | Get available client-level roles that can be mapped to the user
[**realm_users_id_role_mappings_clients_client_composite_get**](ClientRoleMappingsApi.md#realm_users_id_role_mappings_clients_client_composite_get) | **GET** /{realm}/users/{id}/role-mappings/clients/{client}/composite | Get effective client-level role mappings   This recurses any composite roles
[**realm_users_id_role_mappings_clients_client_delete**](ClientRoleMappingsApi.md#realm_users_id_role_mappings_clients_client_delete) | **DELETE** /{realm}/users/{id}/role-mappings/clients/{client} | Delete client-level roles from user role mapping
[**realm_users_id_role_mappings_clients_client_get**](ClientRoleMappingsApi.md#realm_users_id_role_mappings_clients_client_get) | **GET** /{realm}/users/{id}/role-mappings/clients/{client} | Get client-level role mappings for the user, and the app
[**realm_users_id_role_mappings_clients_client_post**](ClientRoleMappingsApi.md#realm_users_id_role_mappings_clients_client_post) | **POST** /{realm}/users/{id}/role-mappings/clients/{client} | Add client-level roles to the user role mapping


# **realm_groups_id_role_mappings_clients_client_available_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_groups_id_role_mappings_clients_client_available_get(realm, id, client)

Get available client-level roles that can be mapped to the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_role_mappings_api
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
    api_instance = client_role_mappings_api.ClientRoleMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    client = "client_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get available client-level roles that can be mapped to the user
        api_response = api_instance.realm_groups_id_role_mappings_clients_client_available_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_groups_id_role_mappings_clients_client_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
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

# **realm_groups_id_role_mappings_clients_client_composite_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_groups_id_role_mappings_clients_client_composite_get(realm, id, client)

Get effective client-level role mappings   This recurses any composite roles

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_role_mappings_api
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
    api_instance = client_role_mappings_api.ClientRoleMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    client = "client_example" # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get effective client-level role mappings   This recurses any composite roles
        api_response = api_instance.realm_groups_id_role_mappings_clients_client_composite_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_groups_id_role_mappings_clients_client_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective client-level role mappings   This recurses any composite roles
        api_response = api_instance.realm_groups_id_role_mappings_clients_client_composite_get(realm, id, client, brief_representation=brief_representation)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_groups_id_role_mappings_clients_client_composite_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
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

# **realm_groups_id_role_mappings_clients_client_delete**
> realm_groups_id_role_mappings_clients_client_delete(realm, id, client, role_representation)

Delete client-level roles from user role mapping

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_role_mappings_api
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
    api_instance = client_role_mappings_api.ClientRoleMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
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
        # Delete client-level roles from user role mapping
        api_instance.realm_groups_id_role_mappings_clients_client_delete(realm, id, client, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_groups_id_role_mappings_clients_client_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
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

# **realm_groups_id_role_mappings_clients_client_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_groups_id_role_mappings_clients_client_get(realm, id, client)

Get client-level role mappings for the user, and the app

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_role_mappings_api
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
    api_instance = client_role_mappings_api.ClientRoleMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    client = "client_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get client-level role mappings for the user, and the app
        api_response = api_instance.realm_groups_id_role_mappings_clients_client_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_groups_id_role_mappings_clients_client_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
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

# **realm_groups_id_role_mappings_clients_client_post**
> realm_groups_id_role_mappings_clients_client_post(realm, id, client, role_representation)

Add client-level roles to the user role mapping

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_role_mappings_api
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
    api_instance = client_role_mappings_api.ClientRoleMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
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
        # Add client-level roles to the user role mapping
        api_instance.realm_groups_id_role_mappings_clients_client_post(realm, id, client, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_groups_id_role_mappings_clients_client_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
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

# **realm_users_id_role_mappings_clients_client_available_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_role_mappings_clients_client_available_get(realm, id, client)

Get available client-level roles that can be mapped to the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_role_mappings_api
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
    api_instance = client_role_mappings_api.ClientRoleMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    client = "client_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get available client-level roles that can be mapped to the user
        api_response = api_instance.realm_users_id_role_mappings_clients_client_available_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_users_id_role_mappings_clients_client_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
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

# **realm_users_id_role_mappings_clients_client_composite_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_role_mappings_clients_client_composite_get(realm, id, client)

Get effective client-level role mappings   This recurses any composite roles

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_role_mappings_api
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
    api_instance = client_role_mappings_api.ClientRoleMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    client = "client_example" # str | 
    brief_representation = True # bool | if false, return roles with their attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get effective client-level role mappings   This recurses any composite roles
        api_response = api_instance.realm_users_id_role_mappings_clients_client_composite_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_users_id_role_mappings_clients_client_composite_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get effective client-level role mappings   This recurses any composite roles
        api_response = api_instance.realm_users_id_role_mappings_clients_client_composite_get(realm, id, client, brief_representation=brief_representation)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_users_id_role_mappings_clients_client_composite_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
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

# **realm_users_id_role_mappings_clients_client_delete**
> realm_users_id_role_mappings_clients_client_delete(realm, id, client, role_representation)

Delete client-level roles from user role mapping

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_role_mappings_api
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
    api_instance = client_role_mappings_api.ClientRoleMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
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
        # Delete client-level roles from user role mapping
        api_instance.realm_users_id_role_mappings_clients_client_delete(realm, id, client, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_users_id_role_mappings_clients_client_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
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

# **realm_users_id_role_mappings_clients_client_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_role_mappings_clients_client_get(realm, id, client)

Get client-level role mappings for the user, and the app

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_role_mappings_api
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
    api_instance = client_role_mappings_api.ClientRoleMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    client = "client_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get client-level role mappings for the user, and the app
        api_response = api_instance.realm_users_id_role_mappings_clients_client_get(realm, id, client)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_users_id_role_mappings_clients_client_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
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

# **realm_users_id_role_mappings_clients_client_post**
> realm_users_id_role_mappings_clients_client_post(realm, id, client, role_representation)

Add client-level roles to the user role mapping

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_role_mappings_api
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
    api_instance = client_role_mappings_api.ClientRoleMappingsApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
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
        # Add client-level roles to the user role mapping
        api_instance.realm_users_id_role_mappings_clients_client_post(realm, id, client, role_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRoleMappingsApi->realm_users_id_role_mappings_clients_client_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
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

