# keycloak_api.IdentityProvidersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_identity_provider_import_config_post**](IdentityProvidersApi.md#realm_identity_provider_import_config_post) | **POST** /{realm}/identity-provider/import-config | Import identity provider from uploaded JSON file
[**realm_identity_provider_instances_alias_delete**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_delete) | **DELETE** /{realm}/identity-provider/instances/{alias} | Delete the identity provider
[**realm_identity_provider_instances_alias_export_get**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_export_get) | **GET** /{realm}/identity-provider/instances/{alias}/export | Export public broker configuration for identity provider
[**realm_identity_provider_instances_alias_get**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_get) | **GET** /{realm}/identity-provider/instances/{alias} | Get the identity provider
[**realm_identity_provider_instances_alias_management_permissions_get**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_management_permissions_get) | **GET** /{realm}/identity-provider/instances/{alias}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realm_identity_provider_instances_alias_management_permissions_put**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_management_permissions_put) | **PUT** /{realm}/identity-provider/instances/{alias}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realm_identity_provider_instances_alias_mapper_types_get**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_mapper_types_get) | **GET** /{realm}/identity-provider/instances/{alias}/mapper-types | Get mapper types for identity provider
[**realm_identity_provider_instances_alias_mappers_get**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_mappers_get) | **GET** /{realm}/identity-provider/instances/{alias}/mappers | Get mappers for identity provider
[**realm_identity_provider_instances_alias_mappers_id_delete**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_mappers_id_delete) | **DELETE** /{realm}/identity-provider/instances/{alias}/mappers/{id} | Delete a mapper for the identity provider
[**realm_identity_provider_instances_alias_mappers_id_get**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_mappers_id_get) | **GET** /{realm}/identity-provider/instances/{alias}/mappers/{id} | Get mapper by id for the identity provider
[**realm_identity_provider_instances_alias_mappers_id_put**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_mappers_id_put) | **PUT** /{realm}/identity-provider/instances/{alias}/mappers/{id} | Update a mapper for the identity provider
[**realm_identity_provider_instances_alias_mappers_post**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_mappers_post) | **POST** /{realm}/identity-provider/instances/{alias}/mappers | Add a mapper to identity provider
[**realm_identity_provider_instances_alias_put**](IdentityProvidersApi.md#realm_identity_provider_instances_alias_put) | **PUT** /{realm}/identity-provider/instances/{alias} | Update the identity provider
[**realm_identity_provider_instances_get**](IdentityProvidersApi.md#realm_identity_provider_instances_get) | **GET** /{realm}/identity-provider/instances | Get identity providers
[**realm_identity_provider_instances_post**](IdentityProvidersApi.md#realm_identity_provider_instances_post) | **POST** /{realm}/identity-provider/instances | Create a new identity provider
[**realm_identity_provider_providers_provider_id_get**](IdentityProvidersApi.md#realm_identity_provider_providers_provider_id_get) | **GET** /{realm}/identity-provider/providers/{provider_id} | Get identity providers


# **realm_identity_provider_import_config_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} realm_identity_provider_import_config_post(realm)

Import identity provider from uploaded JSON file

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Import identity provider from uploaded JSON file
        api_response = api_instance.realm_identity_provider_import_config_post(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_import_config_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

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

# **realm_identity_provider_instances_alias_delete**
> realm_identity_provider_instances_alias_delete(realm, alias)

Delete the identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the identity provider
        api_instance.realm_identity_provider_instances_alias_delete(realm, alias)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |

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

# **realm_identity_provider_instances_alias_export_get**
> realm_identity_provider_instances_alias_export_get(realm, alias)

Export public broker configuration for identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 
    format = "format_example" # str | Format to use (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export public broker configuration for identity provider
        api_instance.realm_identity_provider_instances_alias_export_get(realm, alias)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_export_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export public broker configuration for identity provider
        api_instance.realm_identity_provider_instances_alias_export_get(realm, alias, format=format)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_export_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |
 **format** | **str**| Format to use | [optional]

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

# **realm_identity_provider_instances_alias_get**
> IdentityProviderRepresentation realm_identity_provider_instances_alias_get(realm, alias)

Get the identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
from keycloak_api.model.identity_provider_representation import IdentityProviderRepresentation
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the identity provider
        api_response = api_instance.realm_identity_provider_instances_alias_get(realm, alias)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |

### Return type

[**IdentityProviderRepresentation**](IdentityProviderRepresentation.md)

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

# **realm_identity_provider_instances_alias_management_permissions_get**
> ManagementPermissionReference realm_identity_provider_instances_alias_management_permissions_get(realm, alias)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.realm_identity_provider_instances_alias_management_permissions_get(realm, alias)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_management_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |

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

# **realm_identity_provider_instances_alias_management_permissions_put**
> ManagementPermissionReference realm_identity_provider_instances_alias_management_permissions_put(realm, alias, management_permission_reference)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 
    management_permission_reference = ManagementPermissionReference(
        enabled=True,
        resource="resource_example",
        scope_permissions={},
    ) # ManagementPermissionReference | 

    # example passing only required values which don't have defaults set
    try:
        # Return object stating whether client Authorization permissions have been initialized or not and a reference
        api_response = api_instance.realm_identity_provider_instances_alias_management_permissions_put(realm, alias, management_permission_reference)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_management_permissions_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |
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

# **realm_identity_provider_instances_alias_mapper_types_get**
> realm_identity_provider_instances_alias_mapper_types_get(realm, alias)

Get mapper types for identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get mapper types for identity provider
        api_instance.realm_identity_provider_instances_alias_mapper_types_get(realm, alias)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_mapper_types_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |

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

# **realm_identity_provider_instances_alias_mappers_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_identity_provider_instances_alias_mappers_get(realm, alias)

Get mappers for identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get mappers for identity provider
        api_response = api_instance.realm_identity_provider_instances_alias_mappers_get(realm, alias)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_mappers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |

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

# **realm_identity_provider_instances_alias_mappers_id_delete**
> realm_identity_provider_instances_alias_mappers_id_delete(realm, alias, id)

Delete a mapper for the identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 
    id = "id_example" # str | Mapper id

    # example passing only required values which don't have defaults set
    try:
        # Delete a mapper for the identity provider
        api_instance.realm_identity_provider_instances_alias_mappers_id_delete(realm, alias, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_mappers_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |
 **id** | **str**| Mapper id |

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

# **realm_identity_provider_instances_alias_mappers_id_get**
> IdentityProviderMapperRepresentation realm_identity_provider_instances_alias_mappers_id_get(realm, alias, id)

Get mapper by id for the identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
from keycloak_api.model.identity_provider_mapper_representation import IdentityProviderMapperRepresentation
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 
    id = "id_example" # str | Mapper id

    # example passing only required values which don't have defaults set
    try:
        # Get mapper by id for the identity provider
        api_response = api_instance.realm_identity_provider_instances_alias_mappers_id_get(realm, alias, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_mappers_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |
 **id** | **str**| Mapper id |

### Return type

[**IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)

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

# **realm_identity_provider_instances_alias_mappers_id_put**
> realm_identity_provider_instances_alias_mappers_id_put(realm, alias, id, identity_provider_mapper_representation)

Update a mapper for the identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
from keycloak_api.model.identity_provider_mapper_representation import IdentityProviderMapperRepresentation
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 
    id = "id_example" # str | Mapper id
    identity_provider_mapper_representation = IdentityProviderMapperRepresentation(
        config={},
        id="id_example",
        identity_provider_alias="identity_provider_alias_example",
        identity_provider_mapper="identity_provider_mapper_example",
        name="name_example",
    ) # IdentityProviderMapperRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update a mapper for the identity provider
        api_instance.realm_identity_provider_instances_alias_mappers_id_put(realm, alias, id, identity_provider_mapper_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_mappers_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |
 **id** | **str**| Mapper id |
 **identity_provider_mapper_representation** | [**IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)|  |

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

# **realm_identity_provider_instances_alias_mappers_post**
> realm_identity_provider_instances_alias_mappers_post(realm, alias, identity_provider_mapper_representation)

Add a mapper to identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
from keycloak_api.model.identity_provider_mapper_representation import IdentityProviderMapperRepresentation
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 
    identity_provider_mapper_representation = IdentityProviderMapperRepresentation(
        config={},
        id="id_example",
        identity_provider_alias="identity_provider_alias_example",
        identity_provider_mapper="identity_provider_mapper_example",
        name="name_example",
    ) # IdentityProviderMapperRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Add a mapper to identity provider
        api_instance.realm_identity_provider_instances_alias_mappers_post(realm, alias, identity_provider_mapper_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_mappers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |
 **identity_provider_mapper_representation** | [**IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)|  |

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

# **realm_identity_provider_instances_alias_put**
> realm_identity_provider_instances_alias_put(realm, alias, identity_provider_representation)

Update the identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
from keycloak_api.model.identity_provider_representation import IdentityProviderRepresentation
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | 
    identity_provider_representation = IdentityProviderRepresentation(
        add_read_token_role_on_create=True,
        alias="alias_example",
        config={},
        display_name="display_name_example",
        enabled=True,
        first_broker_login_flow_alias="first_broker_login_flow_alias_example",
        internal_id="internal_id_example",
        link_only=True,
        post_broker_login_flow_alias="post_broker_login_flow_alias_example",
        provider_id="provider_id_example",
        store_token=True,
        trust_email=True,
    ) # IdentityProviderRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update the identity provider
        api_instance.realm_identity_provider_instances_alias_put(realm, alias, identity_provider_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_alias_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**|  |
 **identity_provider_representation** | [**IdentityProviderRepresentation**](IdentityProviderRepresentation.md)|  |

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

# **realm_identity_provider_instances_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_identity_provider_instances_get(realm)

Get identity providers

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get identity providers
        api_response = api_instance.realm_identity_provider_instances_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_get: %s\n" % e)
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

# **realm_identity_provider_instances_post**
> realm_identity_provider_instances_post(realm, identity_provider_representation)

Create a new identity provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
from keycloak_api.model.identity_provider_representation import IdentityProviderRepresentation
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    identity_provider_representation = IdentityProviderRepresentation(
        add_read_token_role_on_create=True,
        alias="alias_example",
        config={},
        display_name="display_name_example",
        enabled=True,
        first_broker_login_flow_alias="first_broker_login_flow_alias_example",
        internal_id="internal_id_example",
        link_only=True,
        post_broker_login_flow_alias="post_broker_login_flow_alias_example",
        provider_id="provider_id_example",
        store_token=True,
        trust_email=True,
    ) # IdentityProviderRepresentation | JSON body

    # example passing only required values which don't have defaults set
    try:
        # Create a new identity provider
        api_instance.realm_identity_provider_instances_post(realm, identity_provider_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_instances_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **identity_provider_representation** | [**IdentityProviderRepresentation**](IdentityProviderRepresentation.md)| JSON body |

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

# **realm_identity_provider_providers_provider_id_get**
> realm_identity_provider_providers_provider_id_get(realm, provider_id)

Get identity providers

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import identity_providers_api
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
    api_instance = identity_providers_api.IdentityProvidersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    provider_id = "provider_id_example" # str | Provider id

    # example passing only required values which don't have defaults set
    try:
        # Get identity providers
        api_instance.realm_identity_provider_providers_provider_id_get(realm, provider_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling IdentityProvidersApi->realm_identity_provider_providers_provider_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **provider_id** | **str**| Provider id |

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

