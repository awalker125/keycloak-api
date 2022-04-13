# keycloak_api.ClientRegistrationPolicyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_client_registration_policy_providers_get**](ClientRegistrationPolicyApi.md#realm_client_registration_policy_providers_get) | **GET** /{realm}/client-registration-policy/providers | Base path for retrieve providers with the configProperties properly filled


# **realm_client_registration_policy_providers_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_registration_policy_providers_get(realm)

Base path for retrieve providers with the configProperties properly filled

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_registration_policy_api
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
    api_instance = client_registration_policy_api.ClientRegistrationPolicyApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Base path for retrieve providers with the configProperties properly filled
        api_response = api_instance.realm_client_registration_policy_providers_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientRegistrationPolicyApi->realm_client_registration_policy_providers_get: %s\n" % e)
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

