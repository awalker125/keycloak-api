"""
    Keycloak Admin REST API

    This is a REST API reference for the Keycloak Admin  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


import unittest

import keycloak_api
from keycloak_api.api.clients_api import ClientsApi  # noqa: E501


class TestClientsApi(unittest.TestCase):
    """ClientsApi unit test stubs"""

    def setUp(self):
        self.api = ClientsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_realm_clients_get(self):
        """Test case for realm_clients_get

        Get clients belonging to the realm   Returns a list of clients belonging to the realm  # noqa: E501
        """
        pass

    def test_realm_clients_id_client_secret_get(self):
        """Test case for realm_clients_id_client_secret_get

        Get the client secret  # noqa: E501
        """
        pass

    def test_realm_clients_id_client_secret_post(self):
        """Test case for realm_clients_id_client_secret_post

        Generate a new secret for the client  # noqa: E501
        """
        pass

    def test_realm_clients_id_default_client_scopes_client_scope_id_delete(self):
        """Test case for realm_clients_id_default_client_scopes_client_scope_id_delete

        """
        pass

    def test_realm_clients_id_default_client_scopes_client_scope_id_put(self):
        """Test case for realm_clients_id_default_client_scopes_client_scope_id_put

        """
        pass

    def test_realm_clients_id_default_client_scopes_get(self):
        """Test case for realm_clients_id_default_client_scopes_get

        Get default client scopes.  # noqa: E501
        """
        pass

    def test_realm_clients_id_delete(self):
        """Test case for realm_clients_id_delete

        Delete the client  # noqa: E501
        """
        pass

    def test_realm_clients_id_evaluate_scopes_generate_example_access_token_get(self):
        """Test case for realm_clients_id_evaluate_scopes_generate_example_access_token_get

        Create JSON with payload of example access token  # noqa: E501
        """
        pass

    def test_realm_clients_id_evaluate_scopes_generate_example_id_token_get(self):
        """Test case for realm_clients_id_evaluate_scopes_generate_example_id_token_get

        Create JSON with payload of example id token  # noqa: E501
        """
        pass

    def test_realm_clients_id_evaluate_scopes_generate_example_userinfo_get(self):
        """Test case for realm_clients_id_evaluate_scopes_generate_example_userinfo_get

        Create JSON with payload of example user info  # noqa: E501
        """
        pass

    def test_realm_clients_id_evaluate_scopes_protocol_mappers_get(self):
        """Test case for realm_clients_id_evaluate_scopes_protocol_mappers_get

        Return list of all protocol mappers, which will be used when generating tokens issued for particular client.  # noqa: E501
        """
        pass

    def test_realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get(self):
        """Test case for realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get

        Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.  # noqa: E501
        """
        pass

    def test_realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get(self):
        """Test case for realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get

        Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him.  # noqa: E501
        """
        pass

    def test_realm_clients_id_get(self):
        """Test case for realm_clients_id_get

        Get representation of the client  # noqa: E501
        """
        pass

    def test_realm_clients_id_installation_providers_provider_id_get(self):
        """Test case for realm_clients_id_installation_providers_provider_id_get

        """
        pass

    def test_realm_clients_id_management_permissions_get(self):
        """Test case for realm_clients_id_management_permissions_get

        Return object stating whether client Authorization permissions have been initialized or not and a reference  # noqa: E501
        """
        pass

    def test_realm_clients_id_management_permissions_put(self):
        """Test case for realm_clients_id_management_permissions_put

        Return object stating whether client Authorization permissions have been initialized or not and a reference  # noqa: E501
        """
        pass

    def test_realm_clients_id_nodes_node_delete(self):
        """Test case for realm_clients_id_nodes_node_delete

        Unregister a cluster node from the client  # noqa: E501
        """
        pass

    def test_realm_clients_id_nodes_post(self):
        """Test case for realm_clients_id_nodes_post

        Register a cluster node with the client   Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle  by sending registration request to Keycloak  # noqa: E501
        """
        pass

    def test_realm_clients_id_offline_session_count_get(self):
        """Test case for realm_clients_id_offline_session_count_get

        Get application offline session count   Returns a number of offline user sessions associated with this client   {      \"count\": number  }  # noqa: E501
        """
        pass

    def test_realm_clients_id_offline_sessions_get(self):
        """Test case for realm_clients_id_offline_sessions_get

        Get offline sessions for client   Returns a list of offline user sessions associated with this client  # noqa: E501
        """
        pass

    def test_realm_clients_id_optional_client_scopes_client_scope_id_delete(self):
        """Test case for realm_clients_id_optional_client_scopes_client_scope_id_delete

        """
        pass

    def test_realm_clients_id_optional_client_scopes_client_scope_id_put(self):
        """Test case for realm_clients_id_optional_client_scopes_client_scope_id_put

        """
        pass

    def test_realm_clients_id_optional_client_scopes_get(self):
        """Test case for realm_clients_id_optional_client_scopes_get

        Get optional client scopes.  # noqa: E501
        """
        pass

    def test_realm_clients_id_push_revocation_post(self):
        """Test case for realm_clients_id_push_revocation_post

        Push the client’s revocation policy to its admin URL   If the client has an admin URL, push revocation policy to it.  # noqa: E501
        """
        pass

    def test_realm_clients_id_put(self):
        """Test case for realm_clients_id_put

        Update the client  # noqa: E501
        """
        pass

    def test_realm_clients_id_registration_access_token_post(self):
        """Test case for realm_clients_id_registration_access_token_post

        Generate a new registration access token for the client  # noqa: E501
        """
        pass

    def test_realm_clients_id_service_account_user_get(self):
        """Test case for realm_clients_id_service_account_user_get

        Get a user dedicated to the service account  # noqa: E501
        """
        pass

    def test_realm_clients_id_session_count_get(self):
        """Test case for realm_clients_id_session_count_get

        Get application session count   Returns a number of user sessions associated with this client   {      \"count\": number  }  # noqa: E501
        """
        pass

    def test_realm_clients_id_test_nodes_available_get(self):
        """Test case for realm_clients_id_test_nodes_available_get

        Test if registered cluster nodes are available   Tests availability by sending 'ping' request to all cluster nodes.  # noqa: E501
        """
        pass

    def test_realm_clients_id_user_sessions_get(self):
        """Test case for realm_clients_id_user_sessions_get

        Get user sessions for client   Returns a list of user sessions associated with this client  # noqa: E501
        """
        pass

    def test_realm_clients_post(self):
        """Test case for realm_clients_post

        Create a new client   Client’s client_id must be unique!  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
