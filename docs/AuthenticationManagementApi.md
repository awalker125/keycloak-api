# keycloak_api.AuthenticationManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_authentication_authenticator_providers_get**](AuthenticationManagementApi.md#realm_authentication_authenticator_providers_get) | **GET** /{realm}/authentication/authenticator-providers | Get authenticator providers   Returns a stream of authenticator providers.
[**realm_authentication_client_authenticator_providers_get**](AuthenticationManagementApi.md#realm_authentication_client_authenticator_providers_get) | **GET** /{realm}/authentication/client-authenticator-providers | Get client authenticator providers   Returns a stream of client authenticator providers.
[**realm_authentication_config_description_provider_id_get**](AuthenticationManagementApi.md#realm_authentication_config_description_provider_id_get) | **GET** /{realm}/authentication/config-description/{providerId} | Get authenticator provider’s configuration description
[**realm_authentication_config_id_delete**](AuthenticationManagementApi.md#realm_authentication_config_id_delete) | **DELETE** /{realm}/authentication/config/{id} | Delete authenticator configuration
[**realm_authentication_config_id_get**](AuthenticationManagementApi.md#realm_authentication_config_id_get) | **GET** /{realm}/authentication/config/{id} | Get authenticator configuration
[**realm_authentication_config_id_put**](AuthenticationManagementApi.md#realm_authentication_config_id_put) | **PUT** /{realm}/authentication/config/{id} | Update authenticator configuration
[**realm_authentication_executions_execution_id_config_post**](AuthenticationManagementApi.md#realm_authentication_executions_execution_id_config_post) | **POST** /{realm}/authentication/executions/{executionId}/config | Update execution with new configuration
[**realm_authentication_executions_execution_id_delete**](AuthenticationManagementApi.md#realm_authentication_executions_execution_id_delete) | **DELETE** /{realm}/authentication/executions/{executionId} | Delete execution
[**realm_authentication_executions_execution_id_get**](AuthenticationManagementApi.md#realm_authentication_executions_execution_id_get) | **GET** /{realm}/authentication/executions/{executionId} | Get Single Execution
[**realm_authentication_executions_execution_id_lower_priority_post**](AuthenticationManagementApi.md#realm_authentication_executions_execution_id_lower_priority_post) | **POST** /{realm}/authentication/executions/{executionId}/lower-priority | Lower execution’s priority
[**realm_authentication_executions_execution_id_raise_priority_post**](AuthenticationManagementApi.md#realm_authentication_executions_execution_id_raise_priority_post) | **POST** /{realm}/authentication/executions/{executionId}/raise-priority | Raise execution’s priority
[**realm_authentication_executions_post**](AuthenticationManagementApi.md#realm_authentication_executions_post) | **POST** /{realm}/authentication/executions | Add new authentication execution
[**realm_authentication_flows_flow_alias_copy_post**](AuthenticationManagementApi.md#realm_authentication_flows_flow_alias_copy_post) | **POST** /{realm}/authentication/flows/{flowAlias}/copy | Copy existing authentication flow under a new name   The new name is given as &#39;newName&#39; attribute of the passed JSON object
[**realm_authentication_flows_flow_alias_executions_execution_post**](AuthenticationManagementApi.md#realm_authentication_flows_flow_alias_executions_execution_post) | **POST** /{realm}/authentication/flows/{flowAlias}/executions/execution | Add new authentication execution to a flow
[**realm_authentication_flows_flow_alias_executions_flow_post**](AuthenticationManagementApi.md#realm_authentication_flows_flow_alias_executions_flow_post) | **POST** /{realm}/authentication/flows/{flowAlias}/executions/flow | Add new flow with new execution to existing flow
[**realm_authentication_flows_flow_alias_executions_get**](AuthenticationManagementApi.md#realm_authentication_flows_flow_alias_executions_get) | **GET** /{realm}/authentication/flows/{flowAlias}/executions | Get authentication executions for a flow
[**realm_authentication_flows_flow_alias_executions_put**](AuthenticationManagementApi.md#realm_authentication_flows_flow_alias_executions_put) | **PUT** /{realm}/authentication/flows/{flowAlias}/executions | Update authentication executions of a Flow
[**realm_authentication_flows_get**](AuthenticationManagementApi.md#realm_authentication_flows_get) | **GET** /{realm}/authentication/flows | Get authentication flows   Returns a stream of authentication flows.
[**realm_authentication_flows_id_delete**](AuthenticationManagementApi.md#realm_authentication_flows_id_delete) | **DELETE** /{realm}/authentication/flows/{id} | Delete an authentication flow
[**realm_authentication_flows_id_get**](AuthenticationManagementApi.md#realm_authentication_flows_id_get) | **GET** /{realm}/authentication/flows/{id} | Get authentication flow for id
[**realm_authentication_flows_id_put**](AuthenticationManagementApi.md#realm_authentication_flows_id_put) | **PUT** /{realm}/authentication/flows/{id} | Update an authentication flow
[**realm_authentication_flows_post**](AuthenticationManagementApi.md#realm_authentication_flows_post) | **POST** /{realm}/authentication/flows | Create a new authentication flow
[**realm_authentication_form_action_providers_get**](AuthenticationManagementApi.md#realm_authentication_form_action_providers_get) | **GET** /{realm}/authentication/form-action-providers | Get form action providers   Returns a stream of form action providers.
[**realm_authentication_form_providers_get**](AuthenticationManagementApi.md#realm_authentication_form_providers_get) | **GET** /{realm}/authentication/form-providers | Get form providers   Returns a stream of form providers.
[**realm_authentication_per_client_config_description_get**](AuthenticationManagementApi.md#realm_authentication_per_client_config_description_get) | **GET** /{realm}/authentication/per-client-config-description | Get configuration descriptions for all clients
[**realm_authentication_register_required_action_post**](AuthenticationManagementApi.md#realm_authentication_register_required_action_post) | **POST** /{realm}/authentication/register-required-action | Register a new required actions
[**realm_authentication_required_actions_alias_delete**](AuthenticationManagementApi.md#realm_authentication_required_actions_alias_delete) | **DELETE** /{realm}/authentication/required-actions/{alias} | Delete required action
[**realm_authentication_required_actions_alias_get**](AuthenticationManagementApi.md#realm_authentication_required_actions_alias_get) | **GET** /{realm}/authentication/required-actions/{alias} | Get required action for alias
[**realm_authentication_required_actions_alias_lower_priority_post**](AuthenticationManagementApi.md#realm_authentication_required_actions_alias_lower_priority_post) | **POST** /{realm}/authentication/required-actions/{alias}/lower-priority | Lower required action’s priority
[**realm_authentication_required_actions_alias_put**](AuthenticationManagementApi.md#realm_authentication_required_actions_alias_put) | **PUT** /{realm}/authentication/required-actions/{alias} | Update required action
[**realm_authentication_required_actions_alias_raise_priority_post**](AuthenticationManagementApi.md#realm_authentication_required_actions_alias_raise_priority_post) | **POST** /{realm}/authentication/required-actions/{alias}/raise-priority | Raise required action’s priority
[**realm_authentication_required_actions_get**](AuthenticationManagementApi.md#realm_authentication_required_actions_get) | **GET** /{realm}/authentication/required-actions | Get required actions   Returns a stream of required actions.
[**realm_authentication_unregistered_required_actions_get**](AuthenticationManagementApi.md#realm_authentication_unregistered_required_actions_get) | **GET** /{realm}/authentication/unregistered-required-actions | Get unregistered required actions   Returns a stream of unregistered required actions.


# **realm_authentication_authenticator_providers_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_authentication_authenticator_providers_get(realm)

Get authenticator providers   Returns a stream of authenticator providers.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get authenticator providers   Returns a stream of authenticator providers.
        api_response = api_instance.realm_authentication_authenticator_providers_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_authenticator_providers_get: %s\n" % e)
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

# **realm_authentication_client_authenticator_providers_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_authentication_client_authenticator_providers_get(realm)

Get client authenticator providers   Returns a stream of client authenticator providers.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get client authenticator providers   Returns a stream of client authenticator providers.
        api_response = api_instance.realm_authentication_client_authenticator_providers_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_client_authenticator_providers_get: %s\n" % e)
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

# **realm_authentication_config_description_provider_id_get**
> AuthenticatorConfigInfoRepresentation realm_authentication_config_description_provider_id_get(realm, provider_id)

Get authenticator provider’s configuration description

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.authenticator_config_info_representation import AuthenticatorConfigInfoRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    provider_id = "providerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get authenticator provider’s configuration description
        api_response = api_instance.realm_authentication_config_description_provider_id_get(realm, provider_id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_config_description_provider_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **provider_id** | **str**|  |

### Return type

[**AuthenticatorConfigInfoRepresentation**](AuthenticatorConfigInfoRepresentation.md)

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

# **realm_authentication_config_id_delete**
> realm_authentication_config_id_delete(realm, id)

Delete authenticator configuration

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | Configuration id

    # example passing only required values which don't have defaults set
    try:
        # Delete authenticator configuration
        api_instance.realm_authentication_config_id_delete(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_config_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| Configuration id |

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

# **realm_authentication_config_id_get**
> AuthenticatorConfigRepresentation realm_authentication_config_id_get(realm, id)

Get authenticator configuration

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.authenticator_config_representation import AuthenticatorConfigRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | Configuration id

    # example passing only required values which don't have defaults set
    try:
        # Get authenticator configuration
        api_response = api_instance.realm_authentication_config_id_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_config_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| Configuration id |

### Return type

[**AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)

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

# **realm_authentication_config_id_put**
> realm_authentication_config_id_put(realm, id, authenticator_config_representation)

Update authenticator configuration

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.authenticator_config_representation import AuthenticatorConfigRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | Configuration id
    authenticator_config_representation = AuthenticatorConfigRepresentation(
        alias="alias_example",
        config={},
        id="id_example",
    ) # AuthenticatorConfigRepresentation | JSON describing new state of authenticator configuration

    # example passing only required values which don't have defaults set
    try:
        # Update authenticator configuration
        api_instance.realm_authentication_config_id_put(realm, id, authenticator_config_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_config_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| Configuration id |
 **authenticator_config_representation** | [**AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)| JSON describing new state of authenticator configuration |

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

# **realm_authentication_executions_execution_id_config_post**
> realm_authentication_executions_execution_id_config_post(realm, execution_id, authenticator_config_representation)

Update execution with new configuration

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.authenticator_config_representation import AuthenticatorConfigRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    execution_id = "executionId_example" # str | Execution id
    authenticator_config_representation = AuthenticatorConfigRepresentation(
        alias="alias_example",
        config={},
        id="id_example",
    ) # AuthenticatorConfigRepresentation | JSON with new configuration

    # example passing only required values which don't have defaults set
    try:
        # Update execution with new configuration
        api_instance.realm_authentication_executions_execution_id_config_post(realm, execution_id, authenticator_config_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_executions_execution_id_config_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **execution_id** | **str**| Execution id |
 **authenticator_config_representation** | [**AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)| JSON with new configuration |

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

# **realm_authentication_executions_execution_id_delete**
> realm_authentication_executions_execution_id_delete(realm, execution_id)

Delete execution

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    execution_id = "executionId_example" # str | Execution id

    # example passing only required values which don't have defaults set
    try:
        # Delete execution
        api_instance.realm_authentication_executions_execution_id_delete(realm, execution_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_executions_execution_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **execution_id** | **str**| Execution id |

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

# **realm_authentication_executions_execution_id_get**
> realm_authentication_executions_execution_id_get(realm, execution_id)

Get Single Execution

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    execution_id = "executionId_example" # str | Execution id

    # example passing only required values which don't have defaults set
    try:
        # Get Single Execution
        api_instance.realm_authentication_executions_execution_id_get(realm, execution_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_executions_execution_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **execution_id** | **str**| Execution id |

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

# **realm_authentication_executions_execution_id_lower_priority_post**
> realm_authentication_executions_execution_id_lower_priority_post(realm, execution_id)

Lower execution’s priority

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    execution_id = "executionId_example" # str | Execution id

    # example passing only required values which don't have defaults set
    try:
        # Lower execution’s priority
        api_instance.realm_authentication_executions_execution_id_lower_priority_post(realm, execution_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_executions_execution_id_lower_priority_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **execution_id** | **str**| Execution id |

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

# **realm_authentication_executions_execution_id_raise_priority_post**
> realm_authentication_executions_execution_id_raise_priority_post(realm, execution_id)

Raise execution’s priority

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    execution_id = "executionId_example" # str | Execution id

    # example passing only required values which don't have defaults set
    try:
        # Raise execution’s priority
        api_instance.realm_authentication_executions_execution_id_raise_priority_post(realm, execution_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_executions_execution_id_raise_priority_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **execution_id** | **str**| Execution id |

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

# **realm_authentication_executions_post**
> realm_authentication_executions_post(realm, authentication_execution_representation)

Add new authentication execution

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.authentication_execution_representation import AuthenticationExecutionRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    authentication_execution_representation = AuthenticationExecutionRepresentation(
        authenticator="authenticator_example",
        authenticator_config="authenticator_config_example",
        authenticator_flow=True,
        flow_id="flow_id_example",
        id="id_example",
        parent_flow="parent_flow_example",
        priority=1,
        requirement="requirement_example",
    ) # AuthenticationExecutionRepresentation | JSON model describing authentication execution

    # example passing only required values which don't have defaults set
    try:
        # Add new authentication execution
        api_instance.realm_authentication_executions_post(realm, authentication_execution_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_executions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **authentication_execution_representation** | [**AuthenticationExecutionRepresentation**](AuthenticationExecutionRepresentation.md)| JSON model describing authentication execution |

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

# **realm_authentication_flows_flow_alias_copy_post**
> realm_authentication_flows_flow_alias_copy_post(realm, flow_alias, request_body)

Copy existing authentication flow under a new name   The new name is given as 'newName' attribute of the passed JSON object

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    flow_alias = "flowAlias_example" # str | Name of the existing authentication flow
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | JSON containing 'newName' attribute

    # example passing only required values which don't have defaults set
    try:
        # Copy existing authentication flow under a new name   The new name is given as 'newName' attribute of the passed JSON object
        api_instance.realm_authentication_flows_flow_alias_copy_post(realm, flow_alias, request_body)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_flows_flow_alias_copy_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **flow_alias** | **str**| Name of the existing authentication flow |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| JSON containing &#39;newName&#39; attribute |

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

# **realm_authentication_flows_flow_alias_executions_execution_post**
> realm_authentication_flows_flow_alias_executions_execution_post(realm, flow_alias, request_body)

Add new authentication execution to a flow

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    flow_alias = "flowAlias_example" # str | Alias of parent flow
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | New execution JSON data containing 'provider' attribute

    # example passing only required values which don't have defaults set
    try:
        # Add new authentication execution to a flow
        api_instance.realm_authentication_flows_flow_alias_executions_execution_post(realm, flow_alias, request_body)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_flows_flow_alias_executions_execution_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **flow_alias** | **str**| Alias of parent flow |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| New execution JSON data containing &#39;provider&#39; attribute |

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

# **realm_authentication_flows_flow_alias_executions_flow_post**
> realm_authentication_flows_flow_alias_executions_flow_post(realm, flow_alias, request_body)

Add new flow with new execution to existing flow

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    flow_alias = "flowAlias_example" # str | Alias of parent authentication flow
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | New authentication flow / execution JSON data containing 'alias', 'type', 'provider', and 'description' attributes

    # example passing only required values which don't have defaults set
    try:
        # Add new flow with new execution to existing flow
        api_instance.realm_authentication_flows_flow_alias_executions_flow_post(realm, flow_alias, request_body)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_flows_flow_alias_executions_flow_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **flow_alias** | **str**| Alias of parent authentication flow |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| New authentication flow / execution JSON data containing &#39;alias&#39;, &#39;type&#39;, &#39;provider&#39;, and &#39;description&#39; attributes |

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

# **realm_authentication_flows_flow_alias_executions_get**
> realm_authentication_flows_flow_alias_executions_get(realm, flow_alias)

Get authentication executions for a flow

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    flow_alias = "flowAlias_example" # str | Flow alias

    # example passing only required values which don't have defaults set
    try:
        # Get authentication executions for a flow
        api_instance.realm_authentication_flows_flow_alias_executions_get(realm, flow_alias)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_flows_flow_alias_executions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **flow_alias** | **str**| Flow alias |

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

# **realm_authentication_flows_flow_alias_executions_put**
> realm_authentication_flows_flow_alias_executions_put(realm, flow_alias, authentication_execution_info_representation)

Update authentication executions of a Flow

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.authentication_execution_info_representation import AuthenticationExecutionInfoRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    flow_alias = "flowAlias_example" # str | Flow alias
    authentication_execution_info_representation = AuthenticationExecutionInfoRepresentation(
        alias="alias_example",
        authentication_config="authentication_config_example",
        authentication_flow=True,
        configurable=True,
        description="description_example",
        display_name="display_name_example",
        flow_id="flow_id_example",
        id="id_example",
        index=1,
        level=1,
        provider_id="provider_id_example",
        requirement="requirement_example",
        requirement_choices=[
            "requirement_choices_example",
        ],
    ) # AuthenticationExecutionInfoRepresentation | AuthenticationExecutionInfoRepresentation

    # example passing only required values which don't have defaults set
    try:
        # Update authentication executions of a Flow
        api_instance.realm_authentication_flows_flow_alias_executions_put(realm, flow_alias, authentication_execution_info_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_flows_flow_alias_executions_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **flow_alias** | **str**| Flow alias |
 **authentication_execution_info_representation** | [**AuthenticationExecutionInfoRepresentation**](AuthenticationExecutionInfoRepresentation.md)| AuthenticationExecutionInfoRepresentation |

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

# **realm_authentication_flows_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_authentication_flows_get(realm)

Get authentication flows   Returns a stream of authentication flows.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get authentication flows   Returns a stream of authentication flows.
        api_response = api_instance.realm_authentication_flows_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_flows_get: %s\n" % e)
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

# **realm_authentication_flows_id_delete**
> realm_authentication_flows_id_delete(realm, id)

Delete an authentication flow

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | Flow id

    # example passing only required values which don't have defaults set
    try:
        # Delete an authentication flow
        api_instance.realm_authentication_flows_id_delete(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_flows_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| Flow id |

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

# **realm_authentication_flows_id_get**
> AuthenticationFlowRepresentation realm_authentication_flows_id_get(realm, id)

Get authentication flow for id

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.authentication_flow_representation import AuthenticationFlowRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | Flow id

    # example passing only required values which don't have defaults set
    try:
        # Get authentication flow for id
        api_response = api_instance.realm_authentication_flows_id_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_flows_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| Flow id |

### Return type

[**AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)

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

# **realm_authentication_flows_id_put**
> realm_authentication_flows_id_put(realm, id, authentication_flow_representation)

Update an authentication flow

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.authentication_flow_representation import AuthenticationFlowRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | Flow id
    authentication_flow_representation = AuthenticationFlowRepresentation(
        alias="alias_example",
        authentication_executions=[
            AuthenticationExecutionExportRepresentation(
                authenticator="authenticator_example",
                authenticator_config="authenticator_config_example",
                authenticator_flow=True,
                flow_alias="flow_alias_example",
                priority=1,
                requirement="requirement_example",
                user_setup_allowed=True,
            ),
        ],
        built_in=True,
        description="description_example",
        id="id_example",
        provider_id="provider_id_example",
        top_level=True,
    ) # AuthenticationFlowRepresentation | Authentication flow representation

    # example passing only required values which don't have defaults set
    try:
        # Update an authentication flow
        api_instance.realm_authentication_flows_id_put(realm, id, authentication_flow_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_flows_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| Flow id |
 **authentication_flow_representation** | [**AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)| Authentication flow representation |

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

# **realm_authentication_flows_post**
> realm_authentication_flows_post(realm, authentication_flow_representation)

Create a new authentication flow

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.authentication_flow_representation import AuthenticationFlowRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    authentication_flow_representation = AuthenticationFlowRepresentation(
        alias="alias_example",
        authentication_executions=[
            AuthenticationExecutionExportRepresentation(
                authenticator="authenticator_example",
                authenticator_config="authenticator_config_example",
                authenticator_flow=True,
                flow_alias="flow_alias_example",
                priority=1,
                requirement="requirement_example",
                user_setup_allowed=True,
            ),
        ],
        built_in=True,
        description="description_example",
        id="id_example",
        provider_id="provider_id_example",
        top_level=True,
    ) # AuthenticationFlowRepresentation | Authentication flow representation

    # example passing only required values which don't have defaults set
    try:
        # Create a new authentication flow
        api_instance.realm_authentication_flows_post(realm, authentication_flow_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_flows_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **authentication_flow_representation** | [**AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)| Authentication flow representation |

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

# **realm_authentication_form_action_providers_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_authentication_form_action_providers_get(realm)

Get form action providers   Returns a stream of form action providers.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get form action providers   Returns a stream of form action providers.
        api_response = api_instance.realm_authentication_form_action_providers_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_form_action_providers_get: %s\n" % e)
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

# **realm_authentication_form_providers_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_authentication_form_providers_get(realm)

Get form providers   Returns a stream of form providers.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get form providers   Returns a stream of form providers.
        api_response = api_instance.realm_authentication_form_providers_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_form_providers_get: %s\n" % e)
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

# **realm_authentication_per_client_config_description_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} realm_authentication_per_client_config_description_get(realm)

Get configuration descriptions for all clients

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get configuration descriptions for all clients
        api_response = api_instance.realm_authentication_per_client_config_description_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_per_client_config_description_get: %s\n" % e)
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

# **realm_authentication_register_required_action_post**
> realm_authentication_register_required_action_post(realm, request_body)

Register a new required actions

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | JSON containing 'providerId', and 'name' attributes.

    # example passing only required values which don't have defaults set
    try:
        # Register a new required actions
        api_instance.realm_authentication_register_required_action_post(realm, request_body)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_register_required_action_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| JSON containing &#39;providerId&#39;, and &#39;name&#39; attributes. |

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

# **realm_authentication_required_actions_alias_delete**
> realm_authentication_required_actions_alias_delete(realm, alias)

Delete required action

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | Alias of required action

    # example passing only required values which don't have defaults set
    try:
        # Delete required action
        api_instance.realm_authentication_required_actions_alias_delete(realm, alias)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_required_actions_alias_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**| Alias of required action |

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

# **realm_authentication_required_actions_alias_get**
> RequiredActionProviderRepresentation realm_authentication_required_actions_alias_get(realm, alias)

Get required action for alias

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.required_action_provider_representation import RequiredActionProviderRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | Alias of required action

    # example passing only required values which don't have defaults set
    try:
        # Get required action for alias
        api_response = api_instance.realm_authentication_required_actions_alias_get(realm, alias)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_required_actions_alias_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**| Alias of required action |

### Return type

[**RequiredActionProviderRepresentation**](RequiredActionProviderRepresentation.md)

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

# **realm_authentication_required_actions_alias_lower_priority_post**
> realm_authentication_required_actions_alias_lower_priority_post(realm, alias)

Lower required action’s priority

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | Alias of required action

    # example passing only required values which don't have defaults set
    try:
        # Lower required action’s priority
        api_instance.realm_authentication_required_actions_alias_lower_priority_post(realm, alias)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_required_actions_alias_lower_priority_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**| Alias of required action |

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

# **realm_authentication_required_actions_alias_put**
> realm_authentication_required_actions_alias_put(realm, alias, required_action_provider_representation)

Update required action

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
from keycloak_api.model.required_action_provider_representation import RequiredActionProviderRepresentation
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | Alias of required action
    required_action_provider_representation = RequiredActionProviderRepresentation(
        alias="alias_example",
        config={},
        default_action=True,
        enabled=True,
        name="name_example",
        priority=1,
        provider_id="provider_id_example",
    ) # RequiredActionProviderRepresentation | JSON describing new state of required action

    # example passing only required values which don't have defaults set
    try:
        # Update required action
        api_instance.realm_authentication_required_actions_alias_put(realm, alias, required_action_provider_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_required_actions_alias_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**| Alias of required action |
 **required_action_provider_representation** | [**RequiredActionProviderRepresentation**](RequiredActionProviderRepresentation.md)| JSON describing new state of required action |

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

# **realm_authentication_required_actions_alias_raise_priority_post**
> realm_authentication_required_actions_alias_raise_priority_post(realm, alias)

Raise required action’s priority

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    alias = "alias_example" # str | Alias of required action

    # example passing only required values which don't have defaults set
    try:
        # Raise required action’s priority
        api_instance.realm_authentication_required_actions_alias_raise_priority_post(realm, alias)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_required_actions_alias_raise_priority_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **alias** | **str**| Alias of required action |

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

# **realm_authentication_required_actions_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_authentication_required_actions_get(realm)

Get required actions   Returns a stream of required actions.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get required actions   Returns a stream of required actions.
        api_response = api_instance.realm_authentication_required_actions_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_required_actions_get: %s\n" % e)
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

# **realm_authentication_unregistered_required_actions_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_authentication_unregistered_required_actions_get(realm)

Get unregistered required actions   Returns a stream of unregistered required actions.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import authentication_management_api
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
    api_instance = authentication_management_api.AuthenticationManagementApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get unregistered required actions   Returns a stream of unregistered required actions.
        api_response = api_instance.realm_authentication_unregistered_required_actions_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling AuthenticationManagementApi->realm_authentication_unregistered_required_actions_get: %s\n" % e)
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

