"""
    Keycloak Admin REST API

    This is a REST API reference for the Keycloak Admin  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


import unittest

import keycloak_api
from keycloak_api.api.client_registration_policy_api import ClientRegistrationPolicyApi  # noqa: E501


class TestClientRegistrationPolicyApi(unittest.TestCase):
    """ClientRegistrationPolicyApi unit test stubs"""

    def setUp(self):
        self.api = ClientRegistrationPolicyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_realm_client_registration_policy_providers_get(self):
        """Test case for realm_client_registration_policy_providers_get

        Base path for retrieve providers with the configProperties properly filled  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
