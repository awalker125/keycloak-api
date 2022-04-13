# keycloak_api.ComponentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_components_get**](ComponentApi.md#realm_components_get) | **GET** /{realm}/components | 
[**realm_components_id_delete**](ComponentApi.md#realm_components_id_delete) | **DELETE** /{realm}/components/{id} | 
[**realm_components_id_get**](ComponentApi.md#realm_components_id_get) | **GET** /{realm}/components/{id} | 
[**realm_components_id_put**](ComponentApi.md#realm_components_id_put) | **PUT** /{realm}/components/{id} | 
[**realm_components_id_sub_component_types_get**](ComponentApi.md#realm_components_id_sub_component_types_get) | **GET** /{realm}/components/{id}/sub-component-types | List of subcomponent types that are available to configure for a particular parent component.
[**realm_components_post**](ComponentApi.md#realm_components_post) | **POST** /{realm}/components | 


# **realm_components_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_components_get(realm)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import component_api
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
    api_instance = component_api.ComponentApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    name = "name_example" # str |  (optional)
    parent = "parent_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_components_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ComponentApi->realm_components_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.realm_components_get(realm, name=name, parent=parent, type=type)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ComponentApi->realm_components_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **name** | **str**|  | [optional]
 **parent** | **str**|  | [optional]
 **type** | **str**|  | [optional]

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

# **realm_components_id_delete**
> realm_components_id_delete(realm, id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import component_api
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
    api_instance = component_api.ComponentApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_components_id_delete(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling ComponentApi->realm_components_id_delete: %s\n" % e)
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

# **realm_components_id_get**
> ComponentRepresentation realm_components_id_get(realm, id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import component_api
from keycloak_api.model.component_representation import ComponentRepresentation
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
    api_instance = component_api.ComponentApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_components_id_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ComponentApi->realm_components_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |

### Return type

[**ComponentRepresentation**](ComponentRepresentation.md)

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

# **realm_components_id_put**
> realm_components_id_put(realm, id, component_representation)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import component_api
from keycloak_api.model.component_representation import ComponentRepresentation
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
    api_instance = component_api.ComponentApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    component_representation = ComponentRepresentation(
        config=MultivaluedHashMap(
            empty=True,
            load_factor=3.14,
            threshold=1,
        ),
        id="id_example",
        name="name_example",
        parent_id="parent_id_example",
        provider_id="provider_id_example",
        provider_type="provider_type_example",
        sub_type="sub_type_example",
    ) # ComponentRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_components_id_put(realm, id, component_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ComponentApi->realm_components_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
 **component_representation** | [**ComponentRepresentation**](ComponentRepresentation.md)|  |

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

# **realm_components_id_sub_component_types_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_components_id_sub_component_types_get(realm, id)

List of subcomponent types that are available to configure for a particular parent component.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import component_api
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
    api_instance = component_api.ComponentApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List of subcomponent types that are available to configure for a particular parent component.
        api_response = api_instance.realm_components_id_sub_component_types_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ComponentApi->realm_components_id_sub_component_types_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of subcomponent types that are available to configure for a particular parent component.
        api_response = api_instance.realm_components_id_sub_component_types_get(realm, id, type=type)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ComponentApi->realm_components_id_sub_component_types_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
 **type** | **str**|  | [optional]

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

# **realm_components_post**
> realm_components_post(realm, component_representation)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import component_api
from keycloak_api.model.component_representation import ComponentRepresentation
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
    api_instance = component_api.ComponentApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    component_representation = ComponentRepresentation(
        config=MultivaluedHashMap(
            empty=True,
            load_factor=3.14,
            threshold=1,
        ),
        id="id_example",
        name="name_example",
        parent_id="parent_id_example",
        provider_id="provider_id_example",
        provider_type="provider_type_example",
        sub_type="sub_type_example",
    ) # ComponentRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_components_post(realm, component_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling ComponentApi->realm_components_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **component_representation** | [**ComponentRepresentation**](ComponentRepresentation.md)|  |

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

