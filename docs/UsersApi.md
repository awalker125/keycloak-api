# keycloak_api.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_users_count_get**](UsersApi.md#realm_users_count_get) | **GET** /{realm}/users/count | Returns the number of users that match the given criteria.
[**realm_users_get**](UsersApi.md#realm_users_get) | **GET** /{realm}/users | Get users   Returns a stream of users, filtered according to query parameters.
[**realm_users_id_configured_user_storage_credential_types_get**](UsersApi.md#realm_users_id_configured_user_storage_credential_types_get) | **GET** /{realm}/users/{id}/configured-user-storage-credential-types | Return credential types, which are provided by the user storage where user is stored.
[**realm_users_id_consents_client_delete**](UsersApi.md#realm_users_id_consents_client_delete) | **DELETE** /{realm}/users/{id}/consents/{client} | Revoke consent and offline tokens for particular client from user
[**realm_users_id_consents_get**](UsersApi.md#realm_users_id_consents_get) | **GET** /{realm}/users/{id}/consents | Get consents granted by the user
[**realm_users_id_credentials_credential_id_delete**](UsersApi.md#realm_users_id_credentials_credential_id_delete) | **DELETE** /{realm}/users/{id}/credentials/{credentialId} | Remove a credential for a user
[**realm_users_id_credentials_credential_id_move_after_new_previous_credential_id_post**](UsersApi.md#realm_users_id_credentials_credential_id_move_after_new_previous_credential_id_post) | **POST** /{realm}/users/{id}/credentials/{credentialId}/moveAfter/{newPreviousCredentialId} | Move a credential to a position behind another credential
[**realm_users_id_credentials_credential_id_move_to_first_post**](UsersApi.md#realm_users_id_credentials_credential_id_move_to_first_post) | **POST** /{realm}/users/{id}/credentials/{credentialId}/moveToFirst | Move a credential to a first position in the credentials list of the user
[**realm_users_id_credentials_credential_id_user_label_put**](UsersApi.md#realm_users_id_credentials_credential_id_user_label_put) | **PUT** /{realm}/users/{id}/credentials/{credentialId}/userLabel | Update a credential label for a user
[**realm_users_id_credentials_get**](UsersApi.md#realm_users_id_credentials_get) | **GET** /{realm}/users/{id}/credentials | 
[**realm_users_id_delete**](UsersApi.md#realm_users_id_delete) | **DELETE** /{realm}/users/{id} | Delete the user
[**realm_users_id_disable_credential_types_put**](UsersApi.md#realm_users_id_disable_credential_types_put) | **PUT** /{realm}/users/{id}/disable-credential-types | Disable all credentials for a user of a specific type
[**realm_users_id_execute_actions_email_put**](UsersApi.md#realm_users_id_execute_actions_email_put) | **PUT** /{realm}/users/{id}/execute-actions-email | Send a update account email to the user   An email contains a link the user can click to perform a set of required actions.
[**realm_users_id_federated_identity_get**](UsersApi.md#realm_users_id_federated_identity_get) | **GET** /{realm}/users/{id}/federated-identity | Get social logins associated with the user
[**realm_users_id_federated_identity_provider_delete**](UsersApi.md#realm_users_id_federated_identity_provider_delete) | **DELETE** /{realm}/users/{id}/federated-identity/{provider} | Remove a social login provider from user
[**realm_users_id_federated_identity_provider_post**](UsersApi.md#realm_users_id_federated_identity_provider_post) | **POST** /{realm}/users/{id}/federated-identity/{provider} | Add a social login provider to the user
[**realm_users_id_get**](UsersApi.md#realm_users_id_get) | **GET** /{realm}/users/{id} | Get representation of the user
[**realm_users_id_groups_count_get**](UsersApi.md#realm_users_id_groups_count_get) | **GET** /{realm}/users/{id}/groups/count | 
[**realm_users_id_groups_get**](UsersApi.md#realm_users_id_groups_get) | **GET** /{realm}/users/{id}/groups | 
[**realm_users_id_groups_group_id_delete**](UsersApi.md#realm_users_id_groups_group_id_delete) | **DELETE** /{realm}/users/{id}/groups/{groupId} | 
[**realm_users_id_groups_group_id_put**](UsersApi.md#realm_users_id_groups_group_id_put) | **PUT** /{realm}/users/{id}/groups/{groupId} | 
[**realm_users_id_impersonation_post**](UsersApi.md#realm_users_id_impersonation_post) | **POST** /{realm}/users/{id}/impersonation | Impersonate the user
[**realm_users_id_logout_post**](UsersApi.md#realm_users_id_logout_post) | **POST** /{realm}/users/{id}/logout | Remove all user sessions associated with the user   Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.
[**realm_users_id_offline_sessions_client_uuid_get**](UsersApi.md#realm_users_id_offline_sessions_client_uuid_get) | **GET** /{realm}/users/{id}/offline-sessions/{clientUuid} | Get offline sessions associated with the user and client
[**realm_users_id_put**](UsersApi.md#realm_users_id_put) | **PUT** /{realm}/users/{id} | Update the user
[**realm_users_id_reset_password_put**](UsersApi.md#realm_users_id_reset_password_put) | **PUT** /{realm}/users/{id}/reset-password | Set up a new password for the user.
[**realm_users_id_send_verify_email_put**](UsersApi.md#realm_users_id_send_verify_email_put) | **PUT** /{realm}/users/{id}/send-verify-email | Send an email-verification email to the user   An email contains a link the user can click to verify their email address.
[**realm_users_id_sessions_get**](UsersApi.md#realm_users_id_sessions_get) | **GET** /{realm}/users/{id}/sessions | Get sessions associated with the user
[**realm_users_post**](UsersApi.md#realm_users_post) | **POST** /{realm}/users | Create a new user   Username must be unique.
[**realm_users_profile_get**](UsersApi.md#realm_users_profile_get) | **GET** /{realm}/users/profile | 
[**realm_users_profile_put**](UsersApi.md#realm_users_profile_put) | **PUT** /{realm}/users/profile | 


# **realm_users_count_get**
> int realm_users_count_get(realm)

Returns the number of users that match the given criteria.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    email = "email_example" # str | email filter (optional)
    email_verified = True # bool |  (optional)
    first_name = "firstName_example" # str | first name filter (optional)
    last_name = "lastName_example" # str | last name filter (optional)
    search = "search_example" # str | arbitrary search string for all the fields below (optional)
    username = "username_example" # str | username filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns the number of users that match the given criteria.
        api_response = api_instance.realm_users_count_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the number of users that match the given criteria.
        api_response = api_instance.realm_users_count_get(realm, email=email, email_verified=email_verified, first_name=first_name, last_name=last_name, search=search, username=username)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **email** | **str**| email filter | [optional]
 **email_verified** | **bool**|  | [optional]
 **first_name** | **str**| first name filter | [optional]
 **last_name** | **str**| last name filter | [optional]
 **search** | **str**| arbitrary search string for all the fields below | [optional]
 **username** | **str**| username filter | [optional]

### Return type

**int**

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

# **realm_users_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_get(realm)

Get users   Returns a stream of users, filtered according to query parameters.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    brief_representation = True # bool | Boolean which defines whether brief representations are returned (default: false) (optional)
    email = "email_example" # str | A String contained in email, or the complete email, if param \"exact\" is true (optional)
    email_verified = True # bool | whether the email has been verified (optional)
    enabled = True # bool | Boolean representing if user is enabled or not (optional)
    exact = True # bool | Boolean which defines whether the params \"last\", \"first\", \"email\" and \"username\" must match exactly (optional)
    first = 1 # int | Pagination offset (optional)
    first_name = "firstName_example" # str | A String contained in firstName, or the complete firstName, if param \"exact\" is true (optional)
    idp_alias = "idpAlias_example" # str | The alias of an Identity Provider linked to the user (optional)
    idp_user_id = "idpUserId_example" # str | The userId at an Identity Provider linked to the user (optional)
    last_name = "lastName_example" # str | A String contained in lastName, or the complete lastName, if param \"exact\" is true (optional)
    max = 1 # int | Maximum results size (defaults to 100) (optional)
    q = "q_example" # str | A query to search for custom attributes, in the format 'key1:value2 key2:value2' (optional)
    search = "search_example" # str | A String contained in username, first or last name, or email (optional)
    username = "username_example" # str | A String contained in username, or the complete username, if param \"exact\" is true (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get users   Returns a stream of users, filtered according to query parameters.
        api_response = api_instance.realm_users_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get users   Returns a stream of users, filtered according to query parameters.
        api_response = api_instance.realm_users_get(realm, brief_representation=brief_representation, email=email, email_verified=email_verified, enabled=enabled, exact=exact, first=first, first_name=first_name, idp_alias=idp_alias, idp_user_id=idp_user_id, last_name=last_name, max=max, q=q, search=search, username=username)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **brief_representation** | **bool**| Boolean which defines whether brief representations are returned (default: false) | [optional]
 **email** | **str**| A String contained in email, or the complete email, if param \&quot;exact\&quot; is true | [optional]
 **email_verified** | **bool**| whether the email has been verified | [optional]
 **enabled** | **bool**| Boolean representing if user is enabled or not | [optional]
 **exact** | **bool**| Boolean which defines whether the params \&quot;last\&quot;, \&quot;first\&quot;, \&quot;email\&quot; and \&quot;username\&quot; must match exactly | [optional]
 **first** | **int**| Pagination offset | [optional]
 **first_name** | **str**| A String contained in firstName, or the complete firstName, if param \&quot;exact\&quot; is true | [optional]
 **idp_alias** | **str**| The alias of an Identity Provider linked to the user | [optional]
 **idp_user_id** | **str**| The userId at an Identity Provider linked to the user | [optional]
 **last_name** | **str**| A String contained in lastName, or the complete lastName, if param \&quot;exact\&quot; is true | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]
 **q** | **str**| A query to search for custom attributes, in the format &#39;key1:value2 key2:value2&#39; | [optional]
 **search** | **str**| A String contained in username, first or last name, or email | [optional]
 **username** | **str**| A String contained in username, or the complete username, if param \&quot;exact\&quot; is true | [optional]

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

# **realm_users_id_configured_user_storage_credential_types_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_configured_user_storage_credential_types_get(realm, id)

Return credential types, which are provided by the user storage where user is stored.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Return credential types, which are provided by the user storage where user is stored.
        api_response = api_instance.realm_users_id_configured_user_storage_credential_types_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_configured_user_storage_credential_types_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_id_consents_client_delete**
> realm_users_id_consents_client_delete(realm, id, client)

Revoke consent and offline tokens for particular client from user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    client = "client_example" # str | Client id

    # example passing only required values which don't have defaults set
    try:
        # Revoke consent and offline tokens for particular client from user
        api_instance.realm_users_id_consents_client_delete(realm, id, client)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_consents_client_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **client** | **str**| Client id |

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

# **realm_users_id_consents_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_consents_get(realm, id)

Get consents granted by the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Get consents granted by the user
        api_response = api_instance.realm_users_id_consents_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_consents_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_id_credentials_credential_id_delete**
> realm_users_id_credentials_credential_id_delete(realm, id, credential_id)

Remove a credential for a user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    credential_id = "credentialId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove a credential for a user
        api_instance.realm_users_id_credentials_credential_id_delete(realm, id, credential_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_credentials_credential_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **credential_id** | **str**|  |

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

# **realm_users_id_credentials_credential_id_move_after_new_previous_credential_id_post**
> realm_users_id_credentials_credential_id_move_after_new_previous_credential_id_post(realm, id, credential_id, new_previous_credential_id)

Move a credential to a position behind another credential

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    credential_id = "credentialId_example" # str | The credential to move
    new_previous_credential_id = "newPreviousCredentialId_example" # str | The credential that will be the previous element in the list. If set to null, the moved credential will be the first element in the list.

    # example passing only required values which don't have defaults set
    try:
        # Move a credential to a position behind another credential
        api_instance.realm_users_id_credentials_credential_id_move_after_new_previous_credential_id_post(realm, id, credential_id, new_previous_credential_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_credentials_credential_id_move_after_new_previous_credential_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **credential_id** | **str**| The credential to move |
 **new_previous_credential_id** | **str**| The credential that will be the previous element in the list. If set to null, the moved credential will be the first element in the list. |

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

# **realm_users_id_credentials_credential_id_move_to_first_post**
> realm_users_id_credentials_credential_id_move_to_first_post(realm, id, credential_id)

Move a credential to a first position in the credentials list of the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    credential_id = "credentialId_example" # str | The credential to move

    # example passing only required values which don't have defaults set
    try:
        # Move a credential to a first position in the credentials list of the user
        api_instance.realm_users_id_credentials_credential_id_move_to_first_post(realm, id, credential_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_credentials_credential_id_move_to_first_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **credential_id** | **str**| The credential to move |

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

# **realm_users_id_credentials_credential_id_user_label_put**
> realm_users_id_credentials_credential_id_user_label_put(realm, id, credential_id, body)

Update a credential label for a user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    credential_id = "credentialId_example" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update a credential label for a user
        api_instance.realm_users_id_credentials_credential_id_user_label_put(realm, id, credential_id, body)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_credentials_credential_id_user_label_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **credential_id** | **str**|  |
 **body** | **str**|  |

### Return type

void (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_users_id_credentials_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_credentials_get(realm, id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_users_id_credentials_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_credentials_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_id_delete**
> realm_users_id_delete(realm, id)

Delete the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Delete the user
        api_instance.realm_users_id_delete(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_id_disable_credential_types_put**
> realm_users_id_disable_credential_types_put(realm, id, request_body)

Disable all credentials for a user of a specific type

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Disable all credentials for a user of a specific type
        api_instance.realm_users_id_disable_credential_types_put(realm, id, request_body)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_disable_credential_types_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **request_body** | **[str]**|  |

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

# **realm_users_id_execute_actions_email_put**
> realm_users_id_execute_actions_email_put(realm, id, request_body)

Send a update account email to the user   An email contains a link the user can click to perform a set of required actions.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    request_body = [
        "request_body_example",
    ] # [str] | required actions the user needs to complete
    client_id = "client_id_example" # str | Client id (optional)
    lifespan = 1 # int | Number of seconds after which the generated token expires (optional)
    redirect_uri = "redirect_uri_example" # str | Redirect uri (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send a update account email to the user   An email contains a link the user can click to perform a set of required actions.
        api_instance.realm_users_id_execute_actions_email_put(realm, id, request_body)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_execute_actions_email_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send a update account email to the user   An email contains a link the user can click to perform a set of required actions.
        api_instance.realm_users_id_execute_actions_email_put(realm, id, request_body, client_id=client_id, lifespan=lifespan, redirect_uri=redirect_uri)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_execute_actions_email_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **request_body** | **[str]**| required actions the user needs to complete |
 **client_id** | **str**| Client id | [optional]
 **lifespan** | **int**| Number of seconds after which the generated token expires | [optional]
 **redirect_uri** | **str**| Redirect uri | [optional]

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

# **realm_users_id_federated_identity_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_federated_identity_get(realm, id)

Get social logins associated with the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Get social logins associated with the user
        api_response = api_instance.realm_users_id_federated_identity_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_federated_identity_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_id_federated_identity_provider_delete**
> realm_users_id_federated_identity_provider_delete(realm, id, provider)

Remove a social login provider from user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    provider = "provider_example" # str | Social login provider id

    # example passing only required values which don't have defaults set
    try:
        # Remove a social login provider from user
        api_instance.realm_users_id_federated_identity_provider_delete(realm, id, provider)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_federated_identity_provider_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **provider** | **str**| Social login provider id |

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

# **realm_users_id_federated_identity_provider_post**
> realm_users_id_federated_identity_provider_post(realm, id, provider, federated_identity_representation)

Add a social login provider to the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
from keycloak_api.model.federated_identity_representation import FederatedIdentityRepresentation
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    provider = "provider_example" # str | Social login provider id
    federated_identity_representation = FederatedIdentityRepresentation(
        identity_provider="identity_provider_example",
        user_id="user_id_example",
        user_name="user_name_example",
    ) # FederatedIdentityRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Add a social login provider to the user
        api_instance.realm_users_id_federated_identity_provider_post(realm, id, provider, federated_identity_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_federated_identity_provider_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **provider** | **str**| Social login provider id |
 **federated_identity_representation** | [**FederatedIdentityRepresentation**](FederatedIdentityRepresentation.md)|  |

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

# **realm_users_id_get**
> UserRepresentation realm_users_id_get(realm, id)

Get representation of the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Get representation of the user
        api_response = api_instance.realm_users_id_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_id_groups_count_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} realm_users_id_groups_count_get(realm, id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    search = "search_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_users_id_groups_count_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_groups_count_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.realm_users_id_groups_count_get(realm, id, search=search)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_groups_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **search** | **str**|  | [optional]

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

# **realm_users_id_groups_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_groups_get(realm, id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    brief_representation = True # bool |  (optional)
    first = 1 # int |  (optional)
    max = 1 # int |  (optional)
    search = "search_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_users_id_groups_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.realm_users_id_groups_get(realm, id, brief_representation=brief_representation, first=first, max=max, search=search)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **brief_representation** | **bool**|  | [optional]
 **first** | **int**|  | [optional]
 **max** | **int**|  | [optional]
 **search** | **str**|  | [optional]

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

# **realm_users_id_groups_group_id_delete**
> realm_users_id_groups_group_id_delete(realm, id, group_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    group_id = "groupId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_users_id_groups_group_id_delete(realm, id, group_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_groups_group_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **group_id** | **str**|  |

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

# **realm_users_id_groups_group_id_put**
> realm_users_id_groups_group_id_put(realm, id, group_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    group_id = "groupId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_users_id_groups_group_id_put(realm, id, group_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_groups_group_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **group_id** | **str**|  |

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

# **realm_users_id_impersonation_post**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} realm_users_id_impersonation_post(realm, id)

Impersonate the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Impersonate the user
        api_response = api_instance.realm_users_id_impersonation_post(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_impersonation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_id_logout_post**
> realm_users_id_logout_post(realm, id)

Remove all user sessions associated with the user   Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Remove all user sessions associated with the user   Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.
        api_instance.realm_users_id_logout_post(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_logout_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_id_offline_sessions_client_uuid_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_offline_sessions_client_uuid_get(realm, id, client_uuid)

Get offline sessions associated with the user and client

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    client_uuid = "clientUuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get offline sessions associated with the user and client
        api_response = api_instance.realm_users_id_offline_sessions_client_uuid_get(realm, id, client_uuid)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_offline_sessions_client_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **client_uuid** | **str**|  |

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

# **realm_users_id_put**
> realm_users_id_put(realm, id, user_representation)

Update the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    user_representation = UserRepresentation(
        access={},
        attributes={},
        client_consents=[
            UserConsentRepresentation(
                client_id="client_id_example",
                created_date=1,
                granted_client_scopes=[
                    "granted_client_scopes_example",
                ],
                last_updated_date=1,
            ),
        ],
        client_roles={},
        created_timestamp=1,
        credentials=[
            CredentialRepresentation(
                created_date=1,
                credential_data="credential_data_example",
                id="id_example",
                priority=1,
                secret_data="secret_data_example",
                temporary=True,
                type="type_example",
                user_label="user_label_example",
                value="value_example",
            ),
        ],
        disableable_credential_types=[
            "disableable_credential_types_example",
        ],
        email="email_example",
        email_verified=True,
        enabled=True,
        federated_identities=[
            FederatedIdentityRepresentation(
                identity_provider="identity_provider_example",
                user_id="user_id_example",
                user_name="user_name_example",
            ),
        ],
        federation_link="federation_link_example",
        first_name="first_name_example",
        groups=[
            "groups_example",
        ],
        id="id_example",
        last_name="last_name_example",
        not_before=1,
        origin="origin_example",
        realm_roles=[
            "realm_roles_example",
        ],
        required_actions=[
            "required_actions_example",
        ],
        _self="_self_example",
        service_account_client_id="service_account_client_id_example",
        username="username_example",
    ) # UserRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update the user
        api_instance.realm_users_id_put(realm, id, user_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **user_representation** | [**UserRepresentation**](UserRepresentation.md)|  |

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

# **realm_users_id_reset_password_put**
> realm_users_id_reset_password_put(realm, id, credential_representation)

Set up a new password for the user.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    credential_representation = CredentialRepresentation(
        created_date=1,
        credential_data="credential_data_example",
        id="id_example",
        priority=1,
        secret_data="secret_data_example",
        temporary=True,
        type="type_example",
        user_label="user_label_example",
        value="value_example",
    ) # CredentialRepresentation | The representation must contain a rawPassword with the plain-text password

    # example passing only required values which don't have defaults set
    try:
        # Set up a new password for the user.
        api_instance.realm_users_id_reset_password_put(realm, id, credential_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_reset_password_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **credential_representation** | [**CredentialRepresentation**](CredentialRepresentation.md)| The representation must contain a rawPassword with the plain-text password |

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

# **realm_users_id_send_verify_email_put**
> realm_users_id_send_verify_email_put(realm, id)

Send an email-verification email to the user   An email contains a link the user can click to verify their email address.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id
    client_id = "client_id_example" # str | Client id (optional)
    redirect_uri = "redirect_uri_example" # str | Redirect uri (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send an email-verification email to the user   An email contains a link the user can click to verify their email address.
        api_instance.realm_users_id_send_verify_email_put(realm, id)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_send_verify_email_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an email-verification email to the user   An email contains a link the user can click to verify their email address.
        api_instance.realm_users_id_send_verify_email_put(realm, id, client_id=client_id, redirect_uri=redirect_uri)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_send_verify_email_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |
 **client_id** | **str**| Client id | [optional]
 **redirect_uri** | **str**| Redirect uri | [optional]

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

# **realm_users_id_sessions_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_users_id_sessions_get(realm, id)

Get sessions associated with the user

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Get sessions associated with the user
        api_response = api_instance.realm_users_id_sessions_get(realm, id)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_id_sessions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| User id |

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

# **realm_users_post**
> realm_users_post(realm, user_representation)

Create a new user   Username must be unique.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    user_representation = UserRepresentation(
        access={},
        attributes={},
        client_consents=[
            UserConsentRepresentation(
                client_id="client_id_example",
                created_date=1,
                granted_client_scopes=[
                    "granted_client_scopes_example",
                ],
                last_updated_date=1,
            ),
        ],
        client_roles={},
        created_timestamp=1,
        credentials=[
            CredentialRepresentation(
                created_date=1,
                credential_data="credential_data_example",
                id="id_example",
                priority=1,
                secret_data="secret_data_example",
                temporary=True,
                type="type_example",
                user_label="user_label_example",
                value="value_example",
            ),
        ],
        disableable_credential_types=[
            "disableable_credential_types_example",
        ],
        email="email_example",
        email_verified=True,
        enabled=True,
        federated_identities=[
            FederatedIdentityRepresentation(
                identity_provider="identity_provider_example",
                user_id="user_id_example",
                user_name="user_name_example",
            ),
        ],
        federation_link="federation_link_example",
        first_name="first_name_example",
        groups=[
            "groups_example",
        ],
        id="id_example",
        last_name="last_name_example",
        not_before=1,
        origin="origin_example",
        realm_roles=[
            "realm_roles_example",
        ],
        required_actions=[
            "required_actions_example",
        ],
        _self="_self_example",
        service_account_client_id="service_account_client_id_example",
        username="username_example",
    ) # UserRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new user   Username must be unique.
        api_instance.realm_users_post(realm, user_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **user_representation** | [**UserRepresentation**](UserRepresentation.md)|  |

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

# **realm_users_profile_get**
> str realm_users_profile_get(realm)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_users_profile_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_profile_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

### Return type

**str**

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

# **realm_users_profile_put**
> realm_users_profile_put(realm, body)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_users_profile_put(realm, body)
    except keycloak_api.ApiException as e:
        print("Exception when calling UsersApi->realm_users_profile_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **body** | **str**|  |

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

