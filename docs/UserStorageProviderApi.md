# keycloak_api.UserStorageProviderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_name_get**](UserStorageProviderApi.md#id_name_get) | **GET** /{id}/name | Need this for admin console to display simple name of provider when displaying client detail   KEYCLOAK-4328
[**realm_user_storage_id_name_get**](UserStorageProviderApi.md#realm_user_storage_id_name_get) | **GET** /{realm}/user-storage/{id}/name | Need this for admin console to display simple name of provider when displaying user detail   KEYCLOAK-4328
[**realm_user_storage_id_remove_imported_users_post**](UserStorageProviderApi.md#realm_user_storage_id_remove_imported_users_post) | **POST** /{realm}/user-storage/{id}/remove-imported-users | Remove imported users
[**realm_user_storage_id_sync_post**](UserStorageProviderApi.md#realm_user_storage_id_sync_post) | **POST** /{realm}/user-storage/{id}/sync | Trigger sync of users   Action can be \&quot;triggerFullSync\&quot; or \&quot;triggerChangedUsersSync\&quot;
[**realm_user_storage_id_unlink_users_post**](UserStorageProviderApi.md#realm_user_storage_id_unlink_users_post) | **POST** /{realm}/user-storage/{id}/unlink-users | Unlink imported users from a storage provider
[**realm_user_storage_parent_id_mappers_id_sync_post**](UserStorageProviderApi.md#realm_user_storage_parent_id_mappers_id_sync_post) | **POST** /{realm}/user-storage/{parentId}/mappers/{id}/sync | Trigger sync of mapper data related to ldap mapper (roles, groups, …​)   direction is \&quot;fedToKeycloak\&quot; or \&quot;keycloakToFed\&quot;


# **id_name_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} id_name_get(id)

Need this for admin console to display simple name of provider when displaying client detail   KEYCLOAK-4328

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import user_storage_provider_api
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
    api_instance = user_storage_provider_api.UserStorageProviderApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Need this for admin console to display simple name of provider when displaying client detail   KEYCLOAK-4328
        api_response = api_instance.id_name_get(id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UserStorageProviderApi->id_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **realm_user_storage_id_name_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} realm_user_storage_id_name_get(realm, id)

Need this for admin console to display simple name of provider when displaying user detail   KEYCLOAK-4328

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import user_storage_provider_api
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
    api_instance = user_storage_provider_api.UserStorageProviderApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Need this for admin console to display simple name of provider when displaying user detail   KEYCLOAK-4328
        api_response = api_instance.realm_user_storage_id_name_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UserStorageProviderApi->realm_user_storage_id_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |

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

# **realm_user_storage_id_remove_imported_users_post**
> realm_user_storage_id_remove_imported_users_post(realm, id)

Remove imported users

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import user_storage_provider_api
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
    api_instance = user_storage_provider_api.UserStorageProviderApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove imported users
        api_instance.realm_user_storage_id_remove_imported_users_post(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling UserStorageProviderApi->realm_user_storage_id_remove_imported_users_post: %s\n" % e)
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

# **realm_user_storage_id_sync_post**
> SynchronizationResult realm_user_storage_id_sync_post(realm, id)

Trigger sync of users   Action can be \"triggerFullSync\" or \"triggerChangedUsersSync\"

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import user_storage_provider_api
from keycloak_api.model.synchronization_result import SynchronizationResult
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
    api_instance = user_storage_provider_api.UserStorageProviderApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 
    action = "action_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Trigger sync of users   Action can be \"triggerFullSync\" or \"triggerChangedUsersSync\"
        api_response = api_instance.realm_user_storage_id_sync_post(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UserStorageProviderApi->realm_user_storage_id_sync_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Trigger sync of users   Action can be \"triggerFullSync\" or \"triggerChangedUsersSync\"
        api_response = api_instance.realm_user_storage_id_sync_post(realm, id, action=action)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UserStorageProviderApi->realm_user_storage_id_sync_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**|  |
 **action** | **str**|  | [optional]

### Return type

[**SynchronizationResult**](SynchronizationResult.md)

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

# **realm_user_storage_id_unlink_users_post**
> realm_user_storage_id_unlink_users_post(realm, id)

Unlink imported users from a storage provider

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import user_storage_provider_api
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
    api_instance = user_storage_provider_api.UserStorageProviderApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink imported users from a storage provider
        api_instance.realm_user_storage_id_unlink_users_post(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling UserStorageProviderApi->realm_user_storage_id_unlink_users_post: %s\n" % e)
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

# **realm_user_storage_parent_id_mappers_id_sync_post**
> SynchronizationResult realm_user_storage_parent_id_mappers_id_sync_post(realm, parent_id, id)

Trigger sync of mapper data related to ldap mapper (roles, groups, …​)   direction is \"fedToKeycloak\" or \"keycloakToFed\"

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import user_storage_provider_api
from keycloak_api.model.synchronization_result import SynchronizationResult
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
    api_instance = user_storage_provider_api.UserStorageProviderApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    parent_id = "parentId_example" # str | 
    id = "id_example" # str | 
    direction = "direction_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Trigger sync of mapper data related to ldap mapper (roles, groups, …​)   direction is \"fedToKeycloak\" or \"keycloakToFed\"
        api_response = api_instance.realm_user_storage_parent_id_mappers_id_sync_post(realm, parent_id, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UserStorageProviderApi->realm_user_storage_parent_id_mappers_id_sync_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Trigger sync of mapper data related to ldap mapper (roles, groups, …​)   direction is \"fedToKeycloak\" or \"keycloakToFed\"
        api_response = api_instance.realm_user_storage_parent_id_mappers_id_sync_post(realm, parent_id, id, direction=direction)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UserStorageProviderApi->realm_user_storage_parent_id_mappers_id_sync_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **parent_id** | **str**|  |
 **id** | **str**|  |
 **direction** | **str**|  | [optional]

### Return type

[**SynchronizationResult**](SynchronizationResult.md)

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

