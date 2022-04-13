"""
    Keycloak Admin REST API

    This is a REST API reference for the Keycloak Admin  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


import unittest

import keycloak_api
from keycloak_api.api.client_attribute_certificate_api import ClientAttributeCertificateApi  # noqa: E501


class TestClientAttributeCertificateApi(unittest.TestCase):
    """ClientAttributeCertificateApi unit test stubs"""

    def setUp(self):
        self.api = ClientAttributeCertificateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_realm_clients_id_certificates_attr_download_post(self):
        """Test case for realm_clients_id_certificates_attr_download_post

        Get a keystore file for the client, containing private key and public certificate  # noqa: E501
        """
        pass

    def test_realm_clients_id_certificates_attr_generate_and_download_post(self):
        """Test case for realm_clients_id_certificates_attr_generate_and_download_post

        Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format.  # noqa: E501
        """
        pass

    def test_realm_clients_id_certificates_attr_generate_post(self):
        """Test case for realm_clients_id_certificates_attr_generate_post

        Generate a new certificate with new key pair  # noqa: E501
        """
        pass

    def test_realm_clients_id_certificates_attr_get(self):
        """Test case for realm_clients_id_certificates_attr_get

        Get key info  # noqa: E501
        """
        pass

    def test_realm_clients_id_certificates_attr_upload_certificate_post(self):
        """Test case for realm_clients_id_certificates_attr_upload_certificate_post

        Upload only certificate, not private key  # noqa: E501
        """
        pass

    def test_realm_clients_id_certificates_attr_upload_post(self):
        """Test case for realm_clients_id_certificates_attr_upload_post

        Upload certificate and eventually private key  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()