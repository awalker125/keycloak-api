"""
    Keycloak Admin REST API

    This is a REST API reference for the Keycloak Admin  # noqa: E501

    The version of the OpenAPI document: 17.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from keycloak_api.api_client import ApiClient, Endpoint as _Endpoint
from keycloak_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from keycloak_api.model.certificate_representation import CertificateRepresentation
from keycloak_api.model.key_store_config import KeyStoreConfig


class ClientAttributeCertificateApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.realm_clients_id_certificates_attr_download_post_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'access_token'
                ],
                'endpoint_path': '/{realm}/clients/{id}/certificates/{attr}/download',
                'operation_id': 'realm_clients_id_certificates_attr_download_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'realm',
                    'id',
                    'attr',
                    'key_store_config',
                ],
                'required': [
                    'realm',
                    'id',
                    'attr',
                    'key_store_config',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'realm':
                        (str,),
                    'id':
                        (str,),
                    'attr':
                        (str,),
                    'key_store_config':
                        (KeyStoreConfig,),
                },
                'attribute_map': {
                    'realm': 'realm',
                    'id': 'id',
                    'attr': 'attr',
                },
                'location_map': {
                    'realm': 'path',
                    'id': 'path',
                    'attr': 'path',
                    'key_store_config': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.realm_clients_id_certificates_attr_generate_and_download_post_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'access_token'
                ],
                'endpoint_path': '/{realm}/clients/{id}/certificates/{attr}/generate-and-download',
                'operation_id': 'realm_clients_id_certificates_attr_generate_and_download_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'realm',
                    'id',
                    'attr',
                    'key_store_config',
                ],
                'required': [
                    'realm',
                    'id',
                    'attr',
                    'key_store_config',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'realm':
                        (str,),
                    'id':
                        (str,),
                    'attr':
                        (str,),
                    'key_store_config':
                        (KeyStoreConfig,),
                },
                'attribute_map': {
                    'realm': 'realm',
                    'id': 'id',
                    'attr': 'attr',
                },
                'location_map': {
                    'realm': 'path',
                    'id': 'path',
                    'attr': 'path',
                    'key_store_config': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.realm_clients_id_certificates_attr_generate_post_endpoint = _Endpoint(
            settings={
                'response_type': (CertificateRepresentation,),
                'auth': [
                    'access_token'
                ],
                'endpoint_path': '/{realm}/clients/{id}/certificates/{attr}/generate',
                'operation_id': 'realm_clients_id_certificates_attr_generate_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'realm',
                    'id',
                    'attr',
                ],
                'required': [
                    'realm',
                    'id',
                    'attr',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'realm':
                        (str,),
                    'id':
                        (str,),
                    'attr':
                        (str,),
                },
                'attribute_map': {
                    'realm': 'realm',
                    'id': 'id',
                    'attr': 'attr',
                },
                'location_map': {
                    'realm': 'path',
                    'id': 'path',
                    'attr': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.realm_clients_id_certificates_attr_get_endpoint = _Endpoint(
            settings={
                'response_type': (CertificateRepresentation,),
                'auth': [
                    'access_token'
                ],
                'endpoint_path': '/{realm}/clients/{id}/certificates/{attr}',
                'operation_id': 'realm_clients_id_certificates_attr_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'realm',
                    'id',
                    'attr',
                ],
                'required': [
                    'realm',
                    'id',
                    'attr',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'realm':
                        (str,),
                    'id':
                        (str,),
                    'attr':
                        (str,),
                },
                'attribute_map': {
                    'realm': 'realm',
                    'id': 'id',
                    'attr': 'attr',
                },
                'location_map': {
                    'realm': 'path',
                    'id': 'path',
                    'attr': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.realm_clients_id_certificates_attr_upload_certificate_post_endpoint = _Endpoint(
            settings={
                'response_type': (CertificateRepresentation,),
                'auth': [
                    'access_token'
                ],
                'endpoint_path': '/{realm}/clients/{id}/certificates/{attr}/upload-certificate',
                'operation_id': 'realm_clients_id_certificates_attr_upload_certificate_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'realm',
                    'id',
                    'attr',
                ],
                'required': [
                    'realm',
                    'id',
                    'attr',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'realm':
                        (str,),
                    'id':
                        (str,),
                    'attr':
                        (str,),
                },
                'attribute_map': {
                    'realm': 'realm',
                    'id': 'id',
                    'attr': 'attr',
                },
                'location_map': {
                    'realm': 'path',
                    'id': 'path',
                    'attr': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.realm_clients_id_certificates_attr_upload_post_endpoint = _Endpoint(
            settings={
                'response_type': (CertificateRepresentation,),
                'auth': [
                    'access_token'
                ],
                'endpoint_path': '/{realm}/clients/{id}/certificates/{attr}/upload',
                'operation_id': 'realm_clients_id_certificates_attr_upload_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'realm',
                    'id',
                    'attr',
                ],
                'required': [
                    'realm',
                    'id',
                    'attr',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'realm':
                        (str,),
                    'id':
                        (str,),
                    'attr':
                        (str,),
                },
                'attribute_map': {
                    'realm': 'realm',
                    'id': 'id',
                    'attr': 'attr',
                },
                'location_map': {
                    'realm': 'path',
                    'id': 'path',
                    'attr': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def realm_clients_id_certificates_attr_download_post(
        self,
        realm,
        id,
        attr,
        key_store_config,
        **kwargs
    ):
        """Get a keystore file for the client, containing private key and public certificate  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.realm_clients_id_certificates_attr_download_post(realm, id, attr, key_store_config, async_req=True)
        >>> result = thread.get()

        Args:
            realm (str): realm name (not id!)
            id (str): id of client (not client-id)
            attr (str):
            key_store_config (KeyStoreConfig): Keystore configuration as JSON

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['realm'] = \
            realm
        kwargs['id'] = \
            id
        kwargs['attr'] = \
            attr
        kwargs['key_store_config'] = \
            key_store_config
        return self.realm_clients_id_certificates_attr_download_post_endpoint.call_with_http_info(**kwargs)

    def realm_clients_id_certificates_attr_generate_and_download_post(
        self,
        realm,
        id,
        attr,
        key_store_config,
        **kwargs
    ):
        """Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.realm_clients_id_certificates_attr_generate_and_download_post(realm, id, attr, key_store_config, async_req=True)
        >>> result = thread.get()

        Args:
            realm (str): realm name (not id!)
            id (str): id of client (not client-id)
            attr (str):
            key_store_config (KeyStoreConfig): Keystore configuration as JSON

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['realm'] = \
            realm
        kwargs['id'] = \
            id
        kwargs['attr'] = \
            attr
        kwargs['key_store_config'] = \
            key_store_config
        return self.realm_clients_id_certificates_attr_generate_and_download_post_endpoint.call_with_http_info(**kwargs)

    def realm_clients_id_certificates_attr_generate_post(
        self,
        realm,
        id,
        attr,
        **kwargs
    ):
        """Generate a new certificate with new key pair  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.realm_clients_id_certificates_attr_generate_post(realm, id, attr, async_req=True)
        >>> result = thread.get()

        Args:
            realm (str): realm name (not id!)
            id (str): id of client (not client-id)
            attr (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CertificateRepresentation
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['realm'] = \
            realm
        kwargs['id'] = \
            id
        kwargs['attr'] = \
            attr
        return self.realm_clients_id_certificates_attr_generate_post_endpoint.call_with_http_info(**kwargs)

    def realm_clients_id_certificates_attr_get(
        self,
        realm,
        id,
        attr,
        **kwargs
    ):
        """Get key info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.realm_clients_id_certificates_attr_get(realm, id, attr, async_req=True)
        >>> result = thread.get()

        Args:
            realm (str): realm name (not id!)
            id (str): id of client (not client-id)
            attr (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CertificateRepresentation
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['realm'] = \
            realm
        kwargs['id'] = \
            id
        kwargs['attr'] = \
            attr
        return self.realm_clients_id_certificates_attr_get_endpoint.call_with_http_info(**kwargs)

    def realm_clients_id_certificates_attr_upload_certificate_post(
        self,
        realm,
        id,
        attr,
        **kwargs
    ):
        """Upload only certificate, not private key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.realm_clients_id_certificates_attr_upload_certificate_post(realm, id, attr, async_req=True)
        >>> result = thread.get()

        Args:
            realm (str): realm name (not id!)
            id (str): id of client (not client-id)
            attr (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CertificateRepresentation
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['realm'] = \
            realm
        kwargs['id'] = \
            id
        kwargs['attr'] = \
            attr
        return self.realm_clients_id_certificates_attr_upload_certificate_post_endpoint.call_with_http_info(**kwargs)

    def realm_clients_id_certificates_attr_upload_post(
        self,
        realm,
        id,
        attr,
        **kwargs
    ):
        """Upload certificate and eventually private key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.realm_clients_id_certificates_attr_upload_post(realm, id, attr, async_req=True)
        >>> result = thread.get()

        Args:
            realm (str): realm name (not id!)
            id (str): id of client (not client-id)
            attr (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CertificateRepresentation
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['realm'] = \
            realm
        kwargs['id'] = \
            id
        kwargs['attr'] = \
            attr
        return self.realm_clients_id_certificates_attr_upload_post_endpoint.call_with_http_info(**kwargs)

