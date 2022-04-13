# keycloak_api.ClientAttributeCertificateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realm_clients_id_certificates_attr_download_post**](ClientAttributeCertificateApi.md#realm_clients_id_certificates_attr_download_post) | **POST** /{realm}/clients/{id}/certificates/{attr}/download | Get a keystore file for the client, containing private key and public certificate
[**realm_clients_id_certificates_attr_generate_and_download_post**](ClientAttributeCertificateApi.md#realm_clients_id_certificates_attr_generate_and_download_post) | **POST** /{realm}/clients/{id}/certificates/{attr}/generate-and-download | Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format.
[**realm_clients_id_certificates_attr_generate_post**](ClientAttributeCertificateApi.md#realm_clients_id_certificates_attr_generate_post) | **POST** /{realm}/clients/{id}/certificates/{attr}/generate | Generate a new certificate with new key pair
[**realm_clients_id_certificates_attr_get**](ClientAttributeCertificateApi.md#realm_clients_id_certificates_attr_get) | **GET** /{realm}/clients/{id}/certificates/{attr} | Get key info
[**realm_clients_id_certificates_attr_upload_certificate_post**](ClientAttributeCertificateApi.md#realm_clients_id_certificates_attr_upload_certificate_post) | **POST** /{realm}/clients/{id}/certificates/{attr}/upload-certificate | Upload only certificate, not private key
[**realm_clients_id_certificates_attr_upload_post**](ClientAttributeCertificateApi.md#realm_clients_id_certificates_attr_upload_post) | **POST** /{realm}/clients/{id}/certificates/{attr}/upload | Upload certificate and eventually private key


# **realm_clients_id_certificates_attr_download_post**
> str realm_clients_id_certificates_attr_download_post(realm, id, attr, key_store_config)

Get a keystore file for the client, containing private key and public certificate

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_attribute_certificate_api
from keycloak_api.model.key_store_config import KeyStoreConfig
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
    api_instance = client_attribute_certificate_api.ClientAttributeCertificateApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    attr = "attr_example" # str | 
    key_store_config = KeyStoreConfig(
        format="format_example",
        key_alias="key_alias_example",
        key_password="key_password_example",
        realm_alias="realm_alias_example",
        realm_certificate=True,
        store_password="store_password_example",
    ) # KeyStoreConfig | Keystore configuration as JSON

    # example passing only required values which don't have defaults set
    try:
        # Get a keystore file for the client, containing private key and public certificate
        api_response = api_instance.realm_clients_id_certificates_attr_download_post(realm, id, attr, key_store_config)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->realm_clients_id_certificates_attr_download_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **attr** | **str**|  |
 **key_store_config** | [**KeyStoreConfig**](KeyStoreConfig.md)| Keystore configuration as JSON |

### Return type

**str**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_clients_id_certificates_attr_generate_and_download_post**
> str realm_clients_id_certificates_attr_generate_and_download_post(realm, id, attr, key_store_config)

Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_attribute_certificate_api
from keycloak_api.model.key_store_config import KeyStoreConfig
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
    api_instance = client_attribute_certificate_api.ClientAttributeCertificateApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    attr = "attr_example" # str | 
    key_store_config = KeyStoreConfig(
        format="format_example",
        key_alias="key_alias_example",
        key_password="key_password_example",
        realm_alias="realm_alias_example",
        realm_certificate=True,
        store_password="store_password_example",
    ) # KeyStoreConfig | Keystore configuration as JSON

    # example passing only required values which don't have defaults set
    try:
        # Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format.
        api_response = api_instance.realm_clients_id_certificates_attr_generate_and_download_post(realm, id, attr, key_store_config)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->realm_clients_id_certificates_attr_generate_and_download_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **attr** | **str**|  |
 **key_store_config** | [**KeyStoreConfig**](KeyStoreConfig.md)| Keystore configuration as JSON |

### Return type

**str**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_clients_id_certificates_attr_generate_post**
> CertificateRepresentation realm_clients_id_certificates_attr_generate_post(realm, id, attr)

Generate a new certificate with new key pair

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_attribute_certificate_api
from keycloak_api.model.certificate_representation import CertificateRepresentation
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
    api_instance = client_attribute_certificate_api.ClientAttributeCertificateApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    attr = "attr_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Generate a new certificate with new key pair
        api_response = api_instance.realm_clients_id_certificates_attr_generate_post(realm, id, attr)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->realm_clients_id_certificates_attr_generate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **attr** | **str**|  |

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

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

# **realm_clients_id_certificates_attr_get**
> CertificateRepresentation realm_clients_id_certificates_attr_get(realm, id, attr)

Get key info

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_attribute_certificate_api
from keycloak_api.model.certificate_representation import CertificateRepresentation
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
    api_instance = client_attribute_certificate_api.ClientAttributeCertificateApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    attr = "attr_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get key info
        api_response = api_instance.realm_clients_id_certificates_attr_get(realm, id, attr)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->realm_clients_id_certificates_attr_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **attr** | **str**|  |

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

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

# **realm_clients_id_certificates_attr_upload_certificate_post**
> CertificateRepresentation realm_clients_id_certificates_attr_upload_certificate_post(realm, id, attr)

Upload only certificate, not private key

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_attribute_certificate_api
from keycloak_api.model.certificate_representation import CertificateRepresentation
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
    api_instance = client_attribute_certificate_api.ClientAttributeCertificateApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    attr = "attr_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Upload only certificate, not private key
        api_response = api_instance.realm_clients_id_certificates_attr_upload_certificate_post(realm, id, attr)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->realm_clients_id_certificates_attr_upload_certificate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **attr** | **str**|  |

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

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

# **realm_clients_id_certificates_attr_upload_post**
> CertificateRepresentation realm_clients_id_certificates_attr_upload_post(realm, id, attr)

Upload certificate and eventually private key

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import client_attribute_certificate_api
from keycloak_api.model.certificate_representation import CertificateRepresentation
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
    api_instance = client_attribute_certificate_api.ClientAttributeCertificateApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    id = "id_example" # str | id of client (not client-id)
    attr = "attr_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Upload certificate and eventually private key
        api_response = api_instance.realm_clients_id_certificates_attr_upload_post(realm, id, attr)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling ClientAttributeCertificateApi->realm_clients_id_certificates_attr_upload_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **id** | **str**| id of client (not client-id) |
 **attr** | **str**|  |

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

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

