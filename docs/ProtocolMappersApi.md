# keycloak_api.ProtocolMappersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_client_scopes_id1_protocol_mappers_models_id2_delete**](ProtocolMappersApi.md#realm_client_scopes_id1_protocol_mappers_models_id2_delete) | **DELETE** /{realm}/client-scopes/{id1}/protocol-mappers/models/{id2} | Delete the mapper
[**realm_client_scopes_id1_protocol_mappers_models_id2_get**](ProtocolMappersApi.md#realm_client_scopes_id1_protocol_mappers_models_id2_get) | **GET** /{realm}/client-scopes/{id1}/protocol-mappers/models/{id2} | Get mapper by id
[**realm_client_scopes_id1_protocol_mappers_models_id2_put**](ProtocolMappersApi.md#realm_client_scopes_id1_protocol_mappers_models_id2_put) | **PUT** /{realm}/client-scopes/{id1}/protocol-mappers/models/{id2} | Update the mapper
[**realm_client_scopes_id_protocol_mappers_add_models_post**](ProtocolMappersApi.md#realm_client_scopes_id_protocol_mappers_add_models_post) | **POST** /{realm}/client-scopes/{id}/protocol-mappers/add-models | Create multiple mappers
[**realm_client_scopes_id_protocol_mappers_models_get**](ProtocolMappersApi.md#realm_client_scopes_id_protocol_mappers_models_get) | **GET** /{realm}/client-scopes/{id}/protocol-mappers/models | Get mappers
[**realm_client_scopes_id_protocol_mappers_models_post**](ProtocolMappersApi.md#realm_client_scopes_id_protocol_mappers_models_post) | **POST** /{realm}/client-scopes/{id}/protocol-mappers/models | Create a mapper
[**realm_client_scopes_id_protocol_mappers_protocol_protocol_get**](ProtocolMappersApi.md#realm_client_scopes_id_protocol_mappers_protocol_protocol_get) | **GET** /{realm}/client-scopes/{id}/protocol-mappers/protocol/{protocol} | Get mappers by name for a specific protocol
[**realm_clients_id1_protocol_mappers_models_id2_delete**](ProtocolMappersApi.md#realm_clients_id1_protocol_mappers_models_id2_delete) | **DELETE** /{realm}/clients/{id1}/protocol-mappers/models/{id2} | Delete the mapper
[**realm_clients_id1_protocol_mappers_models_id2_get**](ProtocolMappersApi.md#realm_clients_id1_protocol_mappers_models_id2_get) | **GET** /{realm}/clients/{id1}/protocol-mappers/models/{id2} | Get mapper by id
[**realm_clients_id1_protocol_mappers_models_id2_put**](ProtocolMappersApi.md#realm_clients_id1_protocol_mappers_models_id2_put) | **PUT** /{realm}/clients/{id1}/protocol-mappers/models/{id2} | Update the mapper
[**realm_clients_id_protocol_mappers_add_models_post**](ProtocolMappersApi.md#realm_clients_id_protocol_mappers_add_models_post) | **POST** /{realm}/clients/{id}/protocol-mappers/add-models | Create multiple mappers
[**realm_clients_id_protocol_mappers_models_get**](ProtocolMappersApi.md#realm_clients_id_protocol_mappers_models_get) | **GET** /{realm}/clients/{id}/protocol-mappers/models | Get mappers
[**realm_clients_id_protocol_mappers_models_post**](ProtocolMappersApi.md#realm_clients_id_protocol_mappers_models_post) | **POST** /{realm}/clients/{id}/protocol-mappers/models | Create a mapper
[**realm_clients_id_protocol_mappers_protocol_protocol_get**](ProtocolMappersApi.md#realm_clients_id_protocol_mappers_protocol_protocol_get) | **GET** /{realm}/clients/{id}/protocol-mappers/protocol/{protocol} | Get mappers by name for a specific protocol


# **realm_client_scopes_id1_protocol_mappers_models_id2_delete**
> realm_client_scopes_id1_protocol_mappers_models_id2_delete(realm, id1, id2)

Delete the mapper

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id1 = "id1_example" # str | 
    id2 = "id2_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the mapper
        api_instance.realm_client_scopes_id1_protocol_mappers_models_id2_delete(realm, id1, id2)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_client_scopes_id1_protocol_mappers_models_id2_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id1** | **str**|  |
 **id2** | **str**|  |

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

# **realm_client_scopes_id1_protocol_mappers_models_id2_get**
> ProtocolMapperRepresentation realm_client_scopes_id1_protocol_mappers_models_id2_get(realm, id1, id2)

Get mapper by id

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
from keycloak_api.model.protocol_mapper_representation import ProtocolMapperRepresentation
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id1 = "id1_example" # str | 
    id2 = "id2_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get mapper by id
        api_response = api_instance.realm_client_scopes_id1_protocol_mappers_models_id2_get(realm, id1, id2)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_client_scopes_id1_protocol_mappers_models_id2_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id1** | **str**|  |
 **id2** | **str**|  |

### Return type

[**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)

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

# **realm_client_scopes_id1_protocol_mappers_models_id2_put**
> realm_client_scopes_id1_protocol_mappers_models_id2_put(realm, id1, id2, protocol_mapper_representation)

Update the mapper

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
from keycloak_api.model.protocol_mapper_representation import ProtocolMapperRepresentation
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id1 = "id1_example" # str | 
    id2 = "id2_example" # str | 
    protocol_mapper_representation = ProtocolMapperRepresentation(
        config={},
        id="id_example",
        name="name_example",
        protocol="protocol_example",
        protocol_mapper="protocol_mapper_example",
    ) # ProtocolMapperRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update the mapper
        api_instance.realm_client_scopes_id1_protocol_mappers_models_id2_put(realm, id1, id2, protocol_mapper_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_client_scopes_id1_protocol_mappers_models_id2_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id1** | **str**|  |
 **id2** | **str**|  |
 **protocol_mapper_representation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  |

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

# **realm_client_scopes_id_protocol_mappers_add_models_post**
> realm_client_scopes_id_protocol_mappers_add_models_post(realm, id, protocol_mapper_representation)

Create multiple mappers

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
from keycloak_api.model.protocol_mapper_representation import ProtocolMapperRepresentation
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
    protocol_mapper_representation = [
        ProtocolMapperRepresentation(
            config={},
            id="id_example",
            name="name_example",
            protocol="protocol_example",
            protocol_mapper="protocol_mapper_example",
        ),
    ] # [ProtocolMapperRepresentation] | 

    # example passing only required values which don't have defaults set
    try:
        # Create multiple mappers
        api_instance.realm_client_scopes_id_protocol_mappers_add_models_post(realm, id, protocol_mapper_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_client_scopes_id_protocol_mappers_add_models_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
 **protocol_mapper_representation** | [**[ProtocolMapperRepresentation]**](ProtocolMapperRepresentation.md)|  |

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

# **realm_client_scopes_id_protocol_mappers_models_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_scopes_id_protocol_mappers_models_get(realm, id)

Get mappers

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)

    # example passing only required values which don't have defaults set
    try:
        # Get mappers
        api_response = api_instance.realm_client_scopes_id_protocol_mappers_models_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_client_scopes_id_protocol_mappers_models_get: %s\n" % e)
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

# **realm_client_scopes_id_protocol_mappers_models_post**
> realm_client_scopes_id_protocol_mappers_models_post(realm, id, protocol_mapper_representation)

Create a mapper

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
from keycloak_api.model.protocol_mapper_representation import ProtocolMapperRepresentation
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
    protocol_mapper_representation = ProtocolMapperRepresentation(
        config={},
        id="id_example",
        name="name_example",
        protocol="protocol_example",
        protocol_mapper="protocol_mapper_example",
    ) # ProtocolMapperRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Create a mapper
        api_instance.realm_client_scopes_id_protocol_mappers_models_post(realm, id, protocol_mapper_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_client_scopes_id_protocol_mappers_models_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
 **protocol_mapper_representation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  |

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

# **realm_client_scopes_id_protocol_mappers_protocol_protocol_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_scopes_id_protocol_mappers_protocol_protocol_get(realm, id, protocol)

Get mappers by name for a specific protocol

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client scope (not name)
    protocol = "protocol_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get mappers by name for a specific protocol
        api_response = api_instance.realm_client_scopes_id_protocol_mappers_protocol_protocol_get(realm, id, protocol)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_client_scopes_id_protocol_mappers_protocol_protocol_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client scope (not name) |
 **protocol** | **str**|  |

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

# **realm_clients_id1_protocol_mappers_models_id2_delete**
> realm_clients_id1_protocol_mappers_models_id2_delete(realm, id1, id2)

Delete the mapper

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id1 = "id1_example" # str | 
    id2 = "id2_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the mapper
        api_instance.realm_clients_id1_protocol_mappers_models_id2_delete(realm, id1, id2)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_clients_id1_protocol_mappers_models_id2_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id1** | **str**|  |
 **id2** | **str**|  |

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

# **realm_clients_id1_protocol_mappers_models_id2_get**
> ProtocolMapperRepresentation realm_clients_id1_protocol_mappers_models_id2_get(realm, id1, id2)

Get mapper by id

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
from keycloak_api.model.protocol_mapper_representation import ProtocolMapperRepresentation
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id1 = "id1_example" # str | 
    id2 = "id2_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get mapper by id
        api_response = api_instance.realm_clients_id1_protocol_mappers_models_id2_get(realm, id1, id2)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_clients_id1_protocol_mappers_models_id2_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id1** | **str**|  |
 **id2** | **str**|  |

### Return type

[**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)

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

# **realm_clients_id1_protocol_mappers_models_id2_put**
> realm_clients_id1_protocol_mappers_models_id2_put(realm, id1, id2, protocol_mapper_representation)

Update the mapper

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
from keycloak_api.model.protocol_mapper_representation import ProtocolMapperRepresentation
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id1 = "id1_example" # str | 
    id2 = "id2_example" # str | 
    protocol_mapper_representation = ProtocolMapperRepresentation(
        config={},
        id="id_example",
        name="name_example",
        protocol="protocol_example",
        protocol_mapper="protocol_mapper_example",
    ) # ProtocolMapperRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update the mapper
        api_instance.realm_clients_id1_protocol_mappers_models_id2_put(realm, id1, id2, protocol_mapper_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_clients_id1_protocol_mappers_models_id2_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id1** | **str**|  |
 **id2** | **str**|  |
 **protocol_mapper_representation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  |

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

# **realm_clients_id_protocol_mappers_add_models_post**
> realm_clients_id_protocol_mappers_add_models_post(realm, id, protocol_mapper_representation)

Create multiple mappers

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
from keycloak_api.model.protocol_mapper_representation import ProtocolMapperRepresentation
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    protocol_mapper_representation = [
        ProtocolMapperRepresentation(
            config={},
            id="id_example",
            name="name_example",
            protocol="protocol_example",
            protocol_mapper="protocol_mapper_example",
        ),
    ] # [ProtocolMapperRepresentation] | 

    # example passing only required values which don't have defaults set
    try:
        # Create multiple mappers
        api_instance.realm_clients_id_protocol_mappers_add_models_post(realm, id, protocol_mapper_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_clients_id_protocol_mappers_add_models_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **protocol_mapper_representation** | [**[ProtocolMapperRepresentation]**](ProtocolMapperRepresentation.md)|  |

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

# **realm_clients_id_protocol_mappers_models_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_protocol_mappers_models_get(realm, id)

Get mappers

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)

    # example passing only required values which don't have defaults set
    try:
        # Get mappers
        api_response = api_instance.realm_clients_id_protocol_mappers_models_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_clients_id_protocol_mappers_models_get: %s\n" % e)
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

# **realm_clients_id_protocol_mappers_models_post**
> realm_clients_id_protocol_mappers_models_post(realm, id, protocol_mapper_representation)

Create a mapper

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
from keycloak_api.model.protocol_mapper_representation import ProtocolMapperRepresentation
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    protocol_mapper_representation = ProtocolMapperRepresentation(
        config={},
        id="id_example",
        name="name_example",
        protocol="protocol_example",
        protocol_mapper="protocol_mapper_example",
    ) # ProtocolMapperRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Create a mapper
        api_instance.realm_clients_id_protocol_mappers_models_post(realm, id, protocol_mapper_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_clients_id_protocol_mappers_models_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **protocol_mapper_representation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  |

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

# **realm_clients_id_protocol_mappers_protocol_protocol_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_id_protocol_mappers_protocol_protocol_get(realm, id, protocol)

Get mappers by name for a specific protocol

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import protocol_mappers_api
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
    api_instance = protocol_mappers_api.ProtocolMappersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    protocol = "protocol_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get mappers by name for a specific protocol
        api_response = api_instance.realm_clients_id_protocol_mappers_protocol_protocol_get(realm, id, protocol)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ProtocolMappersApi->realm_clients_id_protocol_mappers_protocol_protocol_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **protocol** | **str**|  |

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

