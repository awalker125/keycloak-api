"""
    Keycloak Admin REST API

    This is a REST API reference for the Keycloak Admin  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


import unittest

import keycloak_api
from keycloak_api.api.key_api import KeyApi  # noqa: E501


class TestKeyApi(unittest.TestCase):
    """KeyApi unit test stubs"""

    def setUp(self):
        self.api = KeyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_realm_keys_get(self):
        """Test case for realm_keys_get

        """
        pass


if __name__ == '__main__':
    unittest.main()