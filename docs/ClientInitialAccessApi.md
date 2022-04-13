# keycloak_api.ClientInitialAccessApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_clients_initial_access_get**](ClientInitialAccessApi.md#realm_clients_initial_access_get) | **GET** /{realm}/clients-initial-access | 
[**realm_clients_initial_access_id_delete**](ClientInitialAccessApi.md#realm_clients_initial_access_id_delete) | **DELETE** /{realm}/clients-initial-access/{id} | 
[**realm_clients_initial_access_post**](ClientInitialAccessApi.md#realm_clients_initial_access_post) | **POST** /{realm}/clients-initial-access | Create a new initial access token.


# **realm_clients_initial_access_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_clients_initial_access_get(realm)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_initial_access_api
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
    api_instance = client_initial_access_api.ClientInitialAccessApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_clients_initial_access_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientInitialAccessApi->realm_clients_initial_access_get: %s\n" % e)
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

# **realm_clients_initial_access_id_delete**
> realm_clients_initial_access_id_delete(realm, id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_initial_access_api
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
    api_instance = client_initial_access_api.ClientInitialAccessApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_clients_initial_access_id_delete(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientInitialAccessApi->realm_clients_initial_access_id_delete: %s\n" % e)
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

# **realm_clients_initial_access_post**
> ClientInitialAccessPresentation realm_clients_initial_access_post(realm, client_initial_access_create_presentation)

Create a new initial access token.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_initial_access_api
from keycloak_api.model.client_initial_access_presentation import ClientInitialAccessPresentation
from keycloak_api.model.client_initial_access_create_presentation import ClientInitialAccessCreatePresentation
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
    api_instance = client_initial_access_api.ClientInitialAccessApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client_initial_access_create_presentation = ClientInitialAccessCreatePresentation(
        count=1,
        expiration=1,
    ) # ClientInitialAccessCreatePresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new initial access token.
        api_response = api_instance.realm_clients_initial_access_post(realm, client_initial_access_create_presentation)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientInitialAccessApi->realm_clients_initial_access_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client_initial_access_create_presentation** | [**ClientInitialAccessCreatePresentation**](ClientInitialAccessCreatePresentation.md)|  |

### Return type

[**ClientInitialAccessPresentation**](ClientInitialAccessPresentation.md)

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

