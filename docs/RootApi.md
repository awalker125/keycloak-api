# keycloak_api.RootApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_get**](RootApi.md#admin_realms_get) | **GET** /admin/realms | Get themes, social providers, auth providers, and event listeners available on this server


# **admin_realms_get**
> ServerInfoRepresentation admin_realms_get()

Get themes, social providers, auth providers, and event listeners available on this server

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import root_api
from keycloak_api.model.server_info_representation import ServerInfoRepresentation
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
    api_instance = root_api.RootApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get themes, social providers, auth providers, and event listeners available on this server
        api_response = api_instance.admin_realms_get()
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RootApi->admin_realms_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerInfoRepresentation**](ServerInfoRepresentation.md)

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

