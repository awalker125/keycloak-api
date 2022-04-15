# keycloak_api.RealmsAdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_realms_post**](RealmsAdminApi.md#admin_realms_post) | **POST** /admin/realms | Import a realm   Imports a realm from a full representation of that realm.
[**realm_admin_events_delete**](RealmsAdminApi.md#realm_admin_events_delete) | **DELETE** /{realm}/admin-events | Delete all admin events
[**realm_admin_events_get**](RealmsAdminApi.md#realm_admin_events_get) | **GET** /{realm}/admin-events | Get admin events   Returns all admin events, or filters events based on URL query parameters listed here
[**realm_clear_keys_cache_post**](RealmsAdminApi.md#realm_clear_keys_cache_post) | **POST** /{realm}/clear-keys-cache | Clear cache of external public keys (Public keys of clients or Identity providers)
[**realm_clear_realm_cache_post**](RealmsAdminApi.md#realm_clear_realm_cache_post) | **POST** /{realm}/clear-realm-cache | Clear realm cache
[**realm_clear_user_cache_post**](RealmsAdminApi.md#realm_clear_user_cache_post) | **POST** /{realm}/clear-user-cache | Clear user cache
[**realm_client_description_converter_post**](RealmsAdminApi.md#realm_client_description_converter_post) | **POST** /{realm}/client-description-converter | Base path for importing clients under this realm.
[**realm_client_policies_policies_get**](RealmsAdminApi.md#realm_client_policies_policies_get) | **GET** /{realm}/client-policies/policies | 
[**realm_client_policies_policies_put**](RealmsAdminApi.md#realm_client_policies_policies_put) | **PUT** /{realm}/client-policies/policies | 
[**realm_client_policies_profiles_get**](RealmsAdminApi.md#realm_client_policies_profiles_get) | **GET** /{realm}/client-policies/profiles | 
[**realm_client_policies_profiles_put**](RealmsAdminApi.md#realm_client_policies_profiles_put) | **PUT** /{realm}/client-policies/profiles | 
[**realm_client_session_stats_get**](RealmsAdminApi.md#realm_client_session_stats_get) | **GET** /{realm}/client-session-stats | Get client session stats   Returns a JSON map.
[**realm_credential_registrators_get**](RealmsAdminApi.md#realm_credential_registrators_get) | **GET** /{realm}/credential-registrators | 
[**realm_default_default_client_scopes_client_scope_id_delete**](RealmsAdminApi.md#realm_default_default_client_scopes_client_scope_id_delete) | **DELETE** /{realm}/default-default-client-scopes/{clientScopeId} | 
[**realm_default_default_client_scopes_client_scope_id_put**](RealmsAdminApi.md#realm_default_default_client_scopes_client_scope_id_put) | **PUT** /{realm}/default-default-client-scopes/{clientScopeId} | 
[**realm_default_default_client_scopes_get**](RealmsAdminApi.md#realm_default_default_client_scopes_get) | **GET** /{realm}/default-default-client-scopes | Get realm default client scopes.
[**realm_default_groups_get**](RealmsAdminApi.md#realm_default_groups_get) | **GET** /{realm}/default-groups | Get group hierarchy.
[**realm_default_groups_group_id_delete**](RealmsAdminApi.md#realm_default_groups_group_id_delete) | **DELETE** /{realm}/default-groups/{groupId} | 
[**realm_default_groups_group_id_put**](RealmsAdminApi.md#realm_default_groups_group_id_put) | **PUT** /{realm}/default-groups/{groupId} | 
[**realm_default_optional_client_scopes_client_scope_id_delete**](RealmsAdminApi.md#realm_default_optional_client_scopes_client_scope_id_delete) | **DELETE** /{realm}/default-optional-client-scopes/{clientScopeId} | 
[**realm_default_optional_client_scopes_client_scope_id_put**](RealmsAdminApi.md#realm_default_optional_client_scopes_client_scope_id_put) | **PUT** /{realm}/default-optional-client-scopes/{clientScopeId} | 
[**realm_default_optional_client_scopes_get**](RealmsAdminApi.md#realm_default_optional_client_scopes_get) | **GET** /{realm}/default-optional-client-scopes | Get realm optional client scopes.
[**realm_delete**](RealmsAdminApi.md#realm_delete) | **DELETE** /{realm} | Delete the realm
[**realm_events_config_get**](RealmsAdminApi.md#realm_events_config_get) | **GET** /{realm}/events/config | Get the events provider configuration   Returns JSON object with events provider configuration
[**realm_events_config_put**](RealmsAdminApi.md#realm_events_config_put) | **PUT** /{realm}/events/config | Update the events provider   Change the events provider and/or its configuration
[**realm_events_delete**](RealmsAdminApi.md#realm_events_delete) | **DELETE** /{realm}/events | Delete all events
[**realm_events_get**](RealmsAdminApi.md#realm_events_get) | **GET** /{realm}/events | Get events   Returns all events, or filters them based on URL query parameters listed here
[**realm_get**](RealmsAdminApi.md#realm_get) | **GET** /{realm} | Get the top-level representation of the realm   It will not include nested information like User and Client representations.
[**realm_group_by_path_path_get**](RealmsAdminApi.md#realm_group_by_path_path_get) | **GET** /{realm}/group-by-path/{path} | 
[**realm_ldap_server_capabilities_post**](RealmsAdminApi.md#realm_ldap_server_capabilities_post) | **POST** /{realm}/ldap-server-capabilities | Get LDAP supported extensions.
[**realm_localization_get**](RealmsAdminApi.md#realm_localization_get) | **GET** /{realm}/localization | 
[**realm_localization_locale_delete**](RealmsAdminApi.md#realm_localization_locale_delete) | **DELETE** /{realm}/localization/{locale} | 
[**realm_localization_locale_get**](RealmsAdminApi.md#realm_localization_locale_get) | **GET** /{realm}/localization/{locale} | 
[**realm_localization_locale_key_delete**](RealmsAdminApi.md#realm_localization_locale_key_delete) | **DELETE** /{realm}/localization/{locale}/{key} | 
[**realm_localization_locale_key_get**](RealmsAdminApi.md#realm_localization_locale_key_get) | **GET** /{realm}/localization/{locale}/{key} | 
[**realm_localization_locale_key_put**](RealmsAdminApi.md#realm_localization_locale_key_put) | **PUT** /{realm}/localization/{locale}/{key} | 
[**realm_localization_locale_post**](RealmsAdminApi.md#realm_localization_locale_post) | **POST** /{realm}/localization/{locale} | 
[**realm_logout_all_post**](RealmsAdminApi.md#realm_logout_all_post) | **POST** /{realm}/logout-all | Removes all user sessions.
[**realm_partial_export_post**](RealmsAdminApi.md#realm_partial_export_post) | **POST** /{realm}/partial-export | Partial export of existing realm into a JSON file.
[**realm_partial_import_post**](RealmsAdminApi.md#realm_partial_import_post) | **POST** /{realm}/partialImport | Partial import from a JSON file to an existing realm.
[**realm_push_revocation_post**](RealmsAdminApi.md#realm_push_revocation_post) | **POST** /{realm}/push-revocation | Push the realm’s revocation policy to any client that has an admin url associated with it.
[**realm_put**](RealmsAdminApi.md#realm_put) | **PUT** /{realm} | Update the top-level information of the realm   Any user, roles or client information in the representation  will be ignored.
[**realm_sessions_session_delete**](RealmsAdminApi.md#realm_sessions_session_delete) | **DELETE** /{realm}/sessions/{session} | Remove a specific user session.
[**realm_test_ldap_connection_post**](RealmsAdminApi.md#realm_test_ldap_connection_post) | **POST** /{realm}/testLDAPConnection | Test LDAP connection
[**realm_test_smtp_connection_post**](RealmsAdminApi.md#realm_test_smtp_connection_post) | **POST** /{realm}/testSMTPConnection | 
[**realm_users_management_permissions_get**](RealmsAdminApi.md#realm_users_management_permissions_get) | **GET** /{realm}/users-management-permissions | 
[**realm_users_management_permissions_put**](RealmsAdminApi.md#realm_users_management_permissions_put) | **PUT** /{realm}/users-management-permissions | 


# **admin_realms_post**
> admin_realms_post(realm_representation)

Import a realm   Imports a realm from a full representation of that realm.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.realm_representation import RealmRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm_representation = RealmRepresentation(
        access_code_lifespan=1,
        access_code_lifespan_login=1,
        access_code_lifespan_user_action=1,
        access_token_lifespan=1,
        access_token_lifespan_for_implicit_flow=1,
        account_theme="account_theme_example",
        action_token_generated_by_admin_lifespan=1,
        action_token_generated_by_user_lifespan=1,
        admin_events_details_enabled=True,
        admin_events_enabled=True,
        admin_theme="admin_theme_example",
        attributes={},
        authentication_flows=[
            AuthenticationFlowRepresentation(
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
            ),
        ],
        authenticator_config=[
            AuthenticatorConfigRepresentation(
                alias="alias_example",
                config={},
                id="id_example",
            ),
        ],
        browser_flow="browser_flow_example",
        browser_security_headers={},
        brute_force_protected=True,
        client_authentication_flow="client_authentication_flow_example",
        client_offline_session_idle_timeout=1,
        client_offline_session_max_lifespan=1,
        client_policies=JsonNode(
            array=True,
            big_decimal=True,
            big_integer=True,
            binary=True,
            boolean=True,
            container_node=True,
            double=True,
            empty=True,
            float=True,
            floating_point_number=True,
            int=True,
            integral_number=True,
            long=True,
            missing_node=True,
            node_type="ARRAY",
            null=True,
            number=True,
            object=True,
            pojo=True,
            short=True,
            textual=True,
            value_node=True,
        ),
        client_profiles=JsonNode(
            array=True,
            big_decimal=True,
            big_integer=True,
            binary=True,
            boolean=True,
            container_node=True,
            double=True,
            empty=True,
            float=True,
            floating_point_number=True,
            int=True,
            integral_number=True,
            long=True,
            missing_node=True,
            node_type="ARRAY",
            null=True,
            number=True,
            object=True,
            pojo=True,
            short=True,
            textual=True,
            value_node=True,
        ),
        client_scope_mappings={},
        client_scopes=[
            ClientScopeRepresentation(
                attributes={},
                description="description_example",
                id="id_example",
                name="name_example",
                protocol="protocol_example",
                protocol_mappers=[
                    ProtocolMapperRepresentation(
                        config={},
                        id="id_example",
                        name="name_example",
                        protocol="protocol_example",
                        protocol_mapper="protocol_mapper_example",
                    ),
                ],
            ),
        ],
        client_session_idle_timeout=1,
        client_session_max_lifespan=1,
        clients=[
            ClientRepresentation(
                access={},
                admin_url="admin_url_example",
                always_display_in_console=True,
                attributes={},
                authentication_flow_binding_overrides={},
                authorization_services_enabled=True,
                authorization_settings=ResourceServerRepresentation(
                    allow_remote_resource_management=True,
                    client_id="client_id_example",
                    decision_strategy="AFFIRMATIVE",
                    id="id_example",
                    name="name_example",
                    policies=[
                        PolicyRepresentation(
                            config={},
                            decision_strategy="AFFIRMATIVE",
                            description="description_example",
                            id="id_example",
                            logic="POSITIVE",
                            name="name_example",
                            owner="owner_example",
                            policies=[
                                "policies_example",
                            ],
                            resources=[
                                "resources_example",
                            ],
                            resources_data=[
                                ResourceRepresentation(
                                    id="id_example",
                                    attributes={},
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    name="name_example",
                                    owner_managed_access=True,
                                    scopes=[
                                        ScopeRepresentation(
                                            display_name="display_name_example",
                                            icon_uri="icon_uri_example",
                                            id="id_example",
                                            name="name_example",
                                            policies=[],
                                            resources=[],
                                        ),
                                    ],
                                    type="type_example",
                                    uris=[
                                        "uris_example",
                                    ],
                                ),
                            ],
                            scopes=[
                                "scopes_example",
                            ],
                            scopes_data=[
                                ScopeRepresentation(
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    id="id_example",
                                    name="name_example",
                                    policies=[],
                                    resources=[
                                        ResourceRepresentation(
                                            id="id_example",
                                            attributes={},
                                            display_name="display_name_example",
                                            icon_uri="icon_uri_example",
                                            name="name_example",
                                            owner_managed_access=True,
                                            scopes=[],
                                            type="type_example",
                                            uris=[
                                                "uris_example",
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            type="type_example",
                        ),
                    ],
                    policy_enforcement_mode="ENFORCING",
                    resources=[
                        ResourceRepresentation(
                            id="id_example",
                            attributes={},
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            name="name_example",
                            owner_managed_access=True,
                            scopes=[
                                ScopeRepresentation(
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    id="id_example",
                                    name="name_example",
                                    policies=[
                                        PolicyRepresentation(
                                            config={},
                                            decision_strategy="AFFIRMATIVE",
                                            description="description_example",
                                            id="id_example",
                                            logic="POSITIVE",
                                            name="name_example",
                                            owner="owner_example",
                                            policies=[
                                                "policies_example",
                                            ],
                                            resources=[
                                                "resources_example",
                                            ],
                                            resources_data=[],
                                            scopes=[
                                                "scopes_example",
                                            ],
                                            scopes_data=[],
                                            type="type_example",
                                        ),
                                    ],
                                    resources=[],
                                ),
                            ],
                            type="type_example",
                            uris=[
                                "uris_example",
                            ],
                        ),
                    ],
                    scopes=[
                        ScopeRepresentation(
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            id="id_example",
                            name="name_example",
                            policies=[
                                PolicyRepresentation(
                                    config={},
                                    decision_strategy="AFFIRMATIVE",
                                    description="description_example",
                                    id="id_example",
                                    logic="POSITIVE",
                                    name="name_example",
                                    owner="owner_example",
                                    policies=[
                                        "policies_example",
                                    ],
                                    resources=[
                                        "resources_example",
                                    ],
                                    resources_data=[
                                        ResourceRepresentation(
                                            id="id_example",
                                            attributes={},
                                            display_name="display_name_example",
                                            icon_uri="icon_uri_example",
                                            name="name_example",
                                            owner_managed_access=True,
                                            scopes=[],
                                            type="type_example",
                                            uris=[
                                                "uris_example",
                                            ],
                                        ),
                                    ],
                                    scopes=[
                                        "scopes_example",
                                    ],
                                    scopes_data=[],
                                    type="type_example",
                                ),
                            ],
                            resources=[
                                ResourceRepresentation(
                                    id="id_example",
                                    attributes={},
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    name="name_example",
                                    owner_managed_access=True,
                                    scopes=[],
                                    type="type_example",
                                    uris=[
                                        "uris_example",
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                base_url="base_url_example",
                bearer_only=True,
                client_authenticator_type="client_authenticator_type_example",
                client_id="client_id_example",
                consent_required=True,
                default_client_scopes=[
                    "default_client_scopes_example",
                ],
                description="description_example",
                direct_access_grants_enabled=True,
                enabled=True,
                frontchannel_logout=True,
                full_scope_allowed=True,
                id="id_example",
                implicit_flow_enabled=True,
                name="name_example",
                node_re_registration_timeout=1,
                not_before=1,
                oauth2_device_authorization_grant_enabled=True,
                optional_client_scopes=[
                    "optional_client_scopes_example",
                ],
                origin="origin_example",
                protocol="protocol_example",
                protocol_mappers=[
                    ProtocolMapperRepresentation(
                        config={},
                        id="id_example",
                        name="name_example",
                        protocol="protocol_example",
                        protocol_mapper="protocol_mapper_example",
                    ),
                ],
                public_client=True,
                redirect_uris=[
                    "redirect_uris_example",
                ],
                registered_nodes={},
                registration_access_token="registration_access_token_example",
                root_url="root_url_example",
                secret="secret_example",
                service_accounts_enabled=True,
                standard_flow_enabled=True,
                surrogate_auth_required=True,
                web_origins=[
                    "web_origins_example",
                ],
            ),
        ],
        components=MultivaluedHashMap(
            empty=True,
            load_factor=3.14,
            threshold=1,
        ),
        default_default_client_scopes=[
            "default_default_client_scopes_example",
        ],
        default_groups=[
            "default_groups_example",
        ],
        default_locale="default_locale_example",
        default_optional_client_scopes=[
            "default_optional_client_scopes_example",
        ],
        default_role=RoleRepresentation(
            attributes={},
            client_role=True,
            composite=True,
            composites=RoleRepresentationComposites(
                client={},
                realm=[
                    "realm_example",
                ],
            ),
            container_id="container_id_example",
            description="description_example",
            id="id_example",
            name="name_example",
        ),
        default_signature_algorithm="default_signature_algorithm_example",
        direct_grant_flow="direct_grant_flow_example",
        display_name="display_name_example",
        display_name_html="display_name_html_example",
        docker_authentication_flow="docker_authentication_flow_example",
        duplicate_emails_allowed=True,
        edit_username_allowed=True,
        email_theme="email_theme_example",
        enabled=True,
        enabled_event_types=[
            "enabled_event_types_example",
        ],
        events_enabled=True,
        events_expiration=1,
        events_listeners=[
            "events_listeners_example",
        ],
        failure_factor=1,
        federated_users=[
            UserRepresentation(
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
            ),
        ],
        groups=[
            GroupRepresentation(
                access={},
                attributes={},
                client_roles={},
                id="id_example",
                name="name_example",
                path="path_example",
                realm_roles=[
                    "realm_roles_example",
                ],
                sub_groups=[],
            ),
        ],
        id="id_example",
        identity_provider_mappers=[
            IdentityProviderMapperRepresentation(
                config={},
                id="id_example",
                identity_provider_alias="identity_provider_alias_example",
                identity_provider_mapper="identity_provider_mapper_example",
                name="name_example",
            ),
        ],
        identity_providers=[
            IdentityProviderRepresentation(
                add_read_token_role_on_create=True,
                alias="alias_example",
                config={},
                display_name="display_name_example",
                enabled=True,
                first_broker_login_flow_alias="first_broker_login_flow_alias_example",
                internal_id="internal_id_example",
                link_only=True,
                post_broker_login_flow_alias="post_broker_login_flow_alias_example",
                provider_id="provider_id_example",
                store_token=True,
                trust_email=True,
            ),
        ],
        internationalization_enabled=True,
        keycloak_version="keycloak_version_example",
        login_theme="login_theme_example",
        login_with_email_allowed=True,
        max_delta_time_seconds=1,
        max_failure_wait_seconds=1,
        minimum_quick_login_wait_seconds=1,
        not_before=1,
        o_auth2_device_code_lifespan=1,
        o_auth2_device_polling_interval=1,
        oauth2_device_code_lifespan=1,
        oauth2_device_polling_interval=1,
        offline_session_idle_timeout=1,
        offline_session_max_lifespan=1,
        offline_session_max_lifespan_enabled=True,
        otp_policy_algorithm="otp_policy_algorithm_example",
        otp_policy_digits=1,
        otp_policy_initial_counter=1,
        otp_policy_look_ahead_window=1,
        otp_policy_period=1,
        otp_policy_type="otp_policy_type_example",
        otp_supported_applications=[
            "otp_supported_applications_example",
        ],
        password_policy="password_policy_example",
        permanent_lockout=True,
        protocol_mappers=[
            ProtocolMapperRepresentation(
                config={},
                id="id_example",
                name="name_example",
                protocol="protocol_example",
                protocol_mapper="protocol_mapper_example",
            ),
        ],
        quick_login_check_milli_seconds=1,
        realm="realm_example",
        refresh_token_max_reuse=1,
        registration_allowed=True,
        registration_email_as_username=True,
        registration_flow="registration_flow_example",
        remember_me=True,
        required_actions=[
            RequiredActionProviderRepresentation(
                alias="alias_example",
                config={},
                default_action=True,
                enabled=True,
                name="name_example",
                priority=1,
                provider_id="provider_id_example",
            ),
        ],
        reset_credentials_flow="reset_credentials_flow_example",
        reset_password_allowed=True,
        revoke_refresh_token=True,
        roles=RolesRepresentation(
            client={},
            realm=[
                RoleRepresentation(
                    attributes={},
                    client_role=True,
                    composite=True,
                    composites=RoleRepresentationComposites(
                        client={},
                        realm=[
                            "realm_example",
                        ],
                    ),
                    container_id="container_id_example",
                    description="description_example",
                    id="id_example",
                    name="name_example",
                ),
            ],
        ),
        scope_mappings=[
            ScopeMappingRepresentation(
                client="client_example",
                client_scope="client_scope_example",
                roles=[
                    "roles_example",
                ],
                _self="_self_example",
            ),
        ],
        smtp_server={},
        ssl_required="ssl_required_example",
        sso_session_idle_timeout=1,
        sso_session_idle_timeout_remember_me=1,
        sso_session_max_lifespan=1,
        sso_session_max_lifespan_remember_me=1,
        supported_locales=[
            "supported_locales_example",
        ],
        user_federation_mappers=[
            UserFederationMapperRepresentation(
                config={},
                federation_mapper_type="federation_mapper_type_example",
                federation_provider_display_name="federation_provider_display_name_example",
                id="id_example",
                name="name_example",
            ),
        ],
        user_federation_providers=[
            UserFederationProviderRepresentation(
                changed_sync_period=1,
                config={},
                display_name="display_name_example",
                full_sync_period=1,
                id="id_example",
                last_sync=1,
                priority=1,
                provider_name="provider_name_example",
            ),
        ],
        user_managed_access_allowed=True,
        users=[
            UserRepresentation(
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
            ),
        ],
        verify_email=True,
        wait_increment_seconds=1,
        web_authn_policy_acceptable_aaguids=[
            "web_authn_policy_acceptable_aaguids_example",
        ],
        web_authn_policy_attestation_conveyance_preference="web_authn_policy_attestation_conveyance_preference_example",
        web_authn_policy_authenticator_attachment="web_authn_policy_authenticator_attachment_example",
        web_authn_policy_avoid_same_authenticator_register=True,
        web_authn_policy_create_timeout=1,
        web_authn_policy_passwordless_acceptable_aaguids=[
            "web_authn_policy_passwordless_acceptable_aaguids_example",
        ],
        web_authn_policy_passwordless_attestation_conveyance_preference="web_authn_policy_passwordless_attestation_conveyance_preference_example",
        web_authn_policy_passwordless_authenticator_attachment="web_authn_policy_passwordless_authenticator_attachment_example",
        web_authn_policy_passwordless_avoid_same_authenticator_register=True,
        web_authn_policy_passwordless_create_timeout=1,
        web_authn_policy_passwordless_require_resident_key="web_authn_policy_passwordless_require_resident_key_example",
        web_authn_policy_passwordless_rp_entity_name="web_authn_policy_passwordless_rp_entity_name_example",
        web_authn_policy_passwordless_rp_id="web_authn_policy_passwordless_rp_id_example",
        web_authn_policy_passwordless_signature_algorithms=[
            "web_authn_policy_passwordless_signature_algorithms_example",
        ],
        web_authn_policy_passwordless_user_verification_requirement="web_authn_policy_passwordless_user_verification_requirement_example",
        web_authn_policy_require_resident_key="web_authn_policy_require_resident_key_example",
        web_authn_policy_rp_entity_name="web_authn_policy_rp_entity_name_example",
        web_authn_policy_rp_id="web_authn_policy_rp_id_example",
        web_authn_policy_signature_algorithms=[
            "web_authn_policy_signature_algorithms_example",
        ],
        web_authn_policy_user_verification_requirement="web_authn_policy_user_verification_requirement_example",
    ) # RealmRepresentation | JSON representation of the realm

    # example passing only required values which don't have defaults set
    try:
        # Import a realm   Imports a realm from a full representation of that realm.
        api_instance.admin_realms_post(realm_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->admin_realms_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm_representation** | [**RealmRepresentation**](RealmRepresentation.md)| JSON representation of the realm |

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

# **realm_admin_events_delete**
> realm_admin_events_delete(realm)

Delete all admin events

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Delete all admin events
        api_instance.realm_admin_events_delete(realm)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_admin_events_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

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

# **realm_admin_events_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_admin_events_get(realm)

Get admin events   Returns all admin events, or filters events based on URL query parameters listed here

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    auth_client = "authClient_example" # str |  (optional)
    auth_ip_address = "authIpAddress_example" # str |  (optional)
    auth_realm = "authRealm_example" # str |  (optional)
    auth_user = "authUser_example" # str | user id (optional)
    date_from = "dateFrom_example" # str |  (optional)
    date_to = "dateTo_example" # str |  (optional)
    first = 1 # int |  (optional)
    max = 1 # int | Maximum results size (defaults to 100) (optional)
    operation_types = [
        "operationTypes_example",
    ] # [str] |  (optional)
    _resource_path = "resourcePath_example" # str |  (optional)
    resource_types = [
        "resourceTypes_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get admin events   Returns all admin events, or filters events based on URL query parameters listed here
        api_response = api_instance.realm_admin_events_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_admin_events_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get admin events   Returns all admin events, or filters events based on URL query parameters listed here
        api_response = api_instance.realm_admin_events_get(realm, auth_client=auth_client, auth_ip_address=auth_ip_address, auth_realm=auth_realm, auth_user=auth_user, date_from=date_from, date_to=date_to, first=first, max=max, operation_types=operation_types, _resource_path=_resource_path, resource_types=resource_types)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_admin_events_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **auth_client** | **str**|  | [optional]
 **auth_ip_address** | **str**|  | [optional]
 **auth_realm** | **str**|  | [optional]
 **auth_user** | **str**| user id | [optional]
 **date_from** | **str**|  | [optional]
 **date_to** | **str**|  | [optional]
 **first** | **int**|  | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]
 **operation_types** | **[str]**|  | [optional]
 **_resource_path** | **str**|  | [optional]
 **resource_types** | **[str]**|  | [optional]

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

# **realm_clear_keys_cache_post**
> realm_clear_keys_cache_post(realm)

Clear cache of external public keys (Public keys of clients or Identity providers)

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Clear cache of external public keys (Public keys of clients or Identity providers)
        api_instance.realm_clear_keys_cache_post(realm)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_clear_keys_cache_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

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

# **realm_clear_realm_cache_post**
> realm_clear_realm_cache_post(realm)

Clear realm cache

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Clear realm cache
        api_instance.realm_clear_realm_cache_post(realm)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_clear_realm_cache_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

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

# **realm_clear_user_cache_post**
> realm_clear_user_cache_post(realm)

Clear user cache

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Clear user cache
        api_instance.realm_clear_user_cache_post(realm)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_clear_user_cache_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

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

# **realm_client_description_converter_post**
> ClientRepresentation realm_client_description_converter_post(realm, body)

Base path for importing clients under this realm.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.client_representation import ClientRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Base path for importing clients under this realm.
        api_response = api_instance.realm_client_description_converter_post(realm, body)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_client_description_converter_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **body** | **str**|  |

### Return type

[**ClientRepresentation**](ClientRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_client_policies_policies_get**
> ClientPoliciesRepresentation realm_client_policies_policies_get(realm)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.client_policies_representation import ClientPoliciesRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_client_policies_policies_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_client_policies_policies_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

### Return type

[**ClientPoliciesRepresentation**](ClientPoliciesRepresentation.md)

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

# **realm_client_policies_policies_put**
> realm_client_policies_policies_put(realm, client_policies_representation)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.client_policies_representation import ClientPoliciesRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client_policies_representation = ClientPoliciesRepresentation(
        policies=[
            ClientPolicyRepresentation(
                conditions=[
                    ClientPolicyConditionRepresentation(
                        condition="condition_example",
                        configuration=JsonNode(
                            array=True,
                            big_decimal=True,
                            big_integer=True,
                            binary=True,
                            boolean=True,
                            container_node=True,
                            double=True,
                            empty=True,
                            float=True,
                            floating_point_number=True,
                            int=True,
                            integral_number=True,
                            long=True,
                            missing_node=True,
                            node_type="ARRAY",
                            null=True,
                            number=True,
                            object=True,
                            pojo=True,
                            short=True,
                            textual=True,
                            value_node=True,
                        ),
                    ),
                ],
                description="description_example",
                enabled=True,
                name="name_example",
                profiles=[
                    "profiles_example",
                ],
            ),
        ],
    ) # ClientPoliciesRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_client_policies_policies_put(realm, client_policies_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_client_policies_policies_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client_policies_representation** | [**ClientPoliciesRepresentation**](ClientPoliciesRepresentation.md)|  |

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

# **realm_client_policies_profiles_get**
> ClientProfilesRepresentation realm_client_policies_profiles_get(realm)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.client_profiles_representation import ClientProfilesRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    include_global_profiles = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_client_policies_profiles_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_client_policies_profiles_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.realm_client_policies_profiles_get(realm, include_global_profiles=include_global_profiles)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_client_policies_profiles_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **include_global_profiles** | **bool**|  | [optional]

### Return type

[**ClientProfilesRepresentation**](ClientProfilesRepresentation.md)

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

# **realm_client_policies_profiles_put**
> realm_client_policies_profiles_put(realm, client_profiles_representation)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.client_profiles_representation import ClientProfilesRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client_profiles_representation = ClientProfilesRepresentation(
        global_profiles=[
            ClientProfileRepresentation(
                description="description_example",
                executors=[
                    ClientPolicyExecutorRepresentation(
                        configuration=JsonNode(
                            array=True,
                            big_decimal=True,
                            big_integer=True,
                            binary=True,
                            boolean=True,
                            container_node=True,
                            double=True,
                            empty=True,
                            float=True,
                            floating_point_number=True,
                            int=True,
                            integral_number=True,
                            long=True,
                            missing_node=True,
                            node_type="ARRAY",
                            null=True,
                            number=True,
                            object=True,
                            pojo=True,
                            short=True,
                            textual=True,
                            value_node=True,
                        ),
                        executor="executor_example",
                    ),
                ],
                name="name_example",
            ),
        ],
        profiles=[
            ClientProfileRepresentation(
                description="description_example",
                executors=[
                    ClientPolicyExecutorRepresentation(
                        configuration=JsonNode(
                            array=True,
                            big_decimal=True,
                            big_integer=True,
                            binary=True,
                            boolean=True,
                            container_node=True,
                            double=True,
                            empty=True,
                            float=True,
                            floating_point_number=True,
                            int=True,
                            integral_number=True,
                            long=True,
                            missing_node=True,
                            node_type="ARRAY",
                            null=True,
                            number=True,
                            object=True,
                            pojo=True,
                            short=True,
                            textual=True,
                            value_node=True,
                        ),
                        executor="executor_example",
                    ),
                ],
                name="name_example",
            ),
        ],
    ) # ClientProfilesRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_client_policies_profiles_put(realm, client_profiles_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_client_policies_profiles_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client_profiles_representation** | [**ClientProfilesRepresentation**](ClientProfilesRepresentation.md)|  |

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

# **realm_client_session_stats_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_client_session_stats_get(realm)

Get client session stats   Returns a JSON map.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get client session stats   Returns a JSON map.
        api_response = api_instance.realm_client_session_stats_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_client_session_stats_get: %s\n" % e)
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

# **realm_credential_registrators_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_credential_registrators_get(realm)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_credential_registrators_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_credential_registrators_get: %s\n" % e)
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

# **realm_default_default_client_scopes_client_scope_id_delete**
> realm_default_default_client_scopes_client_scope_id_delete(realm, client_scope_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client_scope_id = "clientScopeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_default_default_client_scopes_client_scope_id_delete(realm, client_scope_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_default_default_client_scopes_client_scope_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client_scope_id** | **str**|  |

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

# **realm_default_default_client_scopes_client_scope_id_put**
> realm_default_default_client_scopes_client_scope_id_put(realm, client_scope_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client_scope_id = "clientScopeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_default_default_client_scopes_client_scope_id_put(realm, client_scope_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_default_default_client_scopes_client_scope_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client_scope_id** | **str**|  |

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

# **realm_default_default_client_scopes_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_default_default_client_scopes_get(realm)

Get realm default client scopes.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get realm default client scopes.
        api_response = api_instance.realm_default_default_client_scopes_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_default_default_client_scopes_get: %s\n" % e)
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

# **realm_default_groups_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_default_groups_get(realm)

Get group hierarchy.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get group hierarchy.
        api_response = api_instance.realm_default_groups_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_default_groups_get: %s\n" % e)
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

# **realm_default_groups_group_id_delete**
> realm_default_groups_group_id_delete(realm, group_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    group_id = "groupId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_default_groups_group_id_delete(realm, group_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_default_groups_group_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
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

# **realm_default_groups_group_id_put**
> realm_default_groups_group_id_put(realm, group_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    group_id = "groupId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_default_groups_group_id_put(realm, group_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_default_groups_group_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
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

# **realm_default_optional_client_scopes_client_scope_id_delete**
> realm_default_optional_client_scopes_client_scope_id_delete(realm, client_scope_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client_scope_id = "clientScopeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_default_optional_client_scopes_client_scope_id_delete(realm, client_scope_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_default_optional_client_scopes_client_scope_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client_scope_id** | **str**|  |

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

# **realm_default_optional_client_scopes_client_scope_id_put**
> realm_default_optional_client_scopes_client_scope_id_put(realm, client_scope_id)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client_scope_id = "clientScopeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_default_optional_client_scopes_client_scope_id_put(realm, client_scope_id)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_default_optional_client_scopes_client_scope_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client_scope_id** | **str**|  |

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

# **realm_default_optional_client_scopes_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_default_optional_client_scopes_get(realm)

Get realm optional client scopes.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get realm optional client scopes.
        api_response = api_instance.realm_default_optional_client_scopes_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_default_optional_client_scopes_get: %s\n" % e)
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

# **realm_delete**
> realm_delete(realm)

Delete the realm

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Delete the realm
        api_instance.realm_delete(realm)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

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

# **realm_events_config_get**
> RealmEventsConfigRepresentation realm_events_config_get(realm)

Get the events provider configuration   Returns JSON object with events provider configuration

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.realm_events_config_representation import RealmEventsConfigRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get the events provider configuration   Returns JSON object with events provider configuration
        api_response = api_instance.realm_events_config_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_events_config_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

### Return type

[**RealmEventsConfigRepresentation**](RealmEventsConfigRepresentation.md)

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

# **realm_events_config_put**
> realm_events_config_put(realm, realm_events_config_representation)

Update the events provider   Change the events provider and/or its configuration

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.realm_events_config_representation import RealmEventsConfigRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    realm_events_config_representation = RealmEventsConfigRepresentation(
        admin_events_details_enabled=True,
        admin_events_enabled=True,
        enabled_event_types=[
            "enabled_event_types_example",
        ],
        events_enabled=True,
        events_expiration=1,
        events_listeners=[
            "events_listeners_example",
        ],
    ) # RealmEventsConfigRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update the events provider   Change the events provider and/or its configuration
        api_instance.realm_events_config_put(realm, realm_events_config_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_events_config_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **realm_events_config_representation** | [**RealmEventsConfigRepresentation**](RealmEventsConfigRepresentation.md)|  |

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

# **realm_events_delete**
> realm_events_delete(realm)

Delete all events

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Delete all events
        api_instance.realm_events_delete(realm)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_events_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

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

# **realm_events_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_events_get(realm)

Get events   Returns all events, or filters them based on URL query parameters listed here

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    client = "client_example" # str | App or oauth client name (optional)
    date_from = "dateFrom_example" # str | From date (optional)
    date_to = "dateTo_example" # str | To date (optional)
    first = 1 # int | Paging offset (optional)
    ip_address = "ipAddress_example" # str | IP address (optional)
    max = 1 # int | Maximum results size (defaults to 100) (optional)
    type = [
        "type_example",
    ] # [str] | The types of events to return (optional)
    user = "user_example" # str | User id (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get events   Returns all events, or filters them based on URL query parameters listed here
        api_response = api_instance.realm_events_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_events_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get events   Returns all events, or filters them based on URL query parameters listed here
        api_response = api_instance.realm_events_get(realm, client=client, date_from=date_from, date_to=date_to, first=first, ip_address=ip_address, max=max, type=type, user=user)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_events_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **client** | **str**| App or oauth client name | [optional]
 **date_from** | **str**| From date | [optional]
 **date_to** | **str**| To date | [optional]
 **first** | **int**| Paging offset | [optional]
 **ip_address** | **str**| IP address | [optional]
 **max** | **int**| Maximum results size (defaults to 100) | [optional]
 **type** | **[str]**| The types of events to return | [optional]
 **user** | **str**| User id | [optional]

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

# **realm_get**
> RealmRepresentation realm_get(realm)

Get the top-level representation of the realm   It will not include nested information like User and Client representations.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.realm_representation import RealmRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Get the top-level representation of the realm   It will not include nested information like User and Client representations.
        api_response = api_instance.realm_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

### Return type

[**RealmRepresentation**](RealmRepresentation.md)

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

# **realm_group_by_path_path_get**
> GroupRepresentation realm_group_by_path_path_get(realm, path)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.group_representation import GroupRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    path = "path_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_group_by_path_path_get(realm, path)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_group_by_path_path_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **path** | **str**|  |

### Return type

[**GroupRepresentation**](GroupRepresentation.md)

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

# **realm_ldap_server_capabilities_post**
> realm_ldap_server_capabilities_post(realm, test_ldap_connection_representation)

Get LDAP supported extensions.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.test_ldap_connection_representation import TestLdapConnectionRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    test_ldap_connection_representation = TestLdapConnectionRepresentation(
        action="action_example",
        auth_type="auth_type_example",
        bind_credential="bind_credential_example",
        bind_dn="bind_dn_example",
        component_id="component_id_example",
        connection_timeout="connection_timeout_example",
        connection_url="connection_url_example",
        start_tls="start_tls_example",
        use_truststore_spi="use_truststore_spi_example",
    ) # TestLdapConnectionRepresentation | LDAP configuration

    # example passing only required values which don't have defaults set
    try:
        # Get LDAP supported extensions.
        api_instance.realm_ldap_server_capabilities_post(realm, test_ldap_connection_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_ldap_server_capabilities_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **test_ldap_connection_representation** | [**TestLdapConnectionRepresentation**](TestLdapConnectionRepresentation.md)| LDAP configuration |

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

# **realm_localization_get**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] realm_localization_get(realm)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_localization_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_localization_get: %s\n" % e)
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

# **realm_localization_locale_delete**
> realm_localization_locale_delete(realm, locale)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    locale = "locale_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_localization_locale_delete(realm, locale)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_localization_locale_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **locale** | **str**|  |

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

# **realm_localization_locale_get**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} realm_localization_locale_get(realm, locale)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    locale = "locale_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_localization_locale_get(realm, locale)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_localization_locale_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **locale** | **str**|  |

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

# **realm_localization_locale_key_delete**
> realm_localization_locale_key_delete(realm, locale, key)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    locale = "locale_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_localization_locale_key_delete(realm, locale, key)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_localization_locale_key_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **locale** | **str**|  |
 **key** | **str**|  |

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

# **realm_localization_locale_key_get**
> str realm_localization_locale_key_get(realm, locale, key)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    locale = "locale_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_localization_locale_key_get(realm, locale, key)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_localization_locale_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **locale** | **str**|  |
 **key** | **str**|  |

### Return type

**str**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realm_localization_locale_key_put**
> realm_localization_locale_key_put(realm, locale, key, body)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    locale = "locale_example" # str | 
    key = "key_example" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_localization_locale_key_put(realm, locale, key, body)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_localization_locale_key_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **locale** | **str**|  |
 **key** | **str**|  |
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

# **realm_localization_locale_post**
> realm_localization_locale_post(realm, locale, request_body)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    locale = "locale_example" # str | 
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_localization_locale_post(realm, locale, request_body)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_localization_locale_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **locale** | **str**|  |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

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

# **realm_logout_all_post**
> GlobalRequestResult realm_logout_all_post(realm)

Removes all user sessions.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.global_request_result import GlobalRequestResult
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Removes all user sessions.
        api_response = api_instance.realm_logout_all_post(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_logout_all_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

### Return type

[**GlobalRequestResult**](GlobalRequestResult.md)

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

# **realm_partial_export_post**
> RealmRepresentation realm_partial_export_post(realm)

Partial export of existing realm into a JSON file.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.realm_representation import RealmRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    export_clients = True # bool |  (optional)
    export_groups_and_roles = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Partial export of existing realm into a JSON file.
        api_response = api_instance.realm_partial_export_post(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_partial_export_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Partial export of existing realm into a JSON file.
        api_response = api_instance.realm_partial_export_post(realm, export_clients=export_clients, export_groups_and_roles=export_groups_and_roles)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_partial_export_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **export_clients** | **bool**|  | [optional]
 **export_groups_and_roles** | **bool**|  | [optional]

### Return type

[**RealmRepresentation**](RealmRepresentation.md)

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

# **realm_partial_import_post**
> realm_partial_import_post(realm, partial_import_representation)

Partial import from a JSON file to an existing realm.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.partial_import_representation import PartialImportRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    partial_import_representation = PartialImportRepresentation(
        clients=[
            ClientRepresentation(
                access={},
                admin_url="admin_url_example",
                always_display_in_console=True,
                attributes={},
                authentication_flow_binding_overrides={},
                authorization_services_enabled=True,
                authorization_settings=ResourceServerRepresentation(
                    allow_remote_resource_management=True,
                    client_id="client_id_example",
                    decision_strategy="AFFIRMATIVE",
                    id="id_example",
                    name="name_example",
                    policies=[
                        PolicyRepresentation(
                            config={},
                            decision_strategy="AFFIRMATIVE",
                            description="description_example",
                            id="id_example",
                            logic="POSITIVE",
                            name="name_example",
                            owner="owner_example",
                            policies=[
                                "policies_example",
                            ],
                            resources=[
                                "resources_example",
                            ],
                            resources_data=[
                                ResourceRepresentation(
                                    id="id_example",
                                    attributes={},
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    name="name_example",
                                    owner_managed_access=True,
                                    scopes=[
                                        ScopeRepresentation(
                                            display_name="display_name_example",
                                            icon_uri="icon_uri_example",
                                            id="id_example",
                                            name="name_example",
                                            policies=[],
                                            resources=[],
                                        ),
                                    ],
                                    type="type_example",
                                    uris=[
                                        "uris_example",
                                    ],
                                ),
                            ],
                            scopes=[
                                "scopes_example",
                            ],
                            scopes_data=[
                                ScopeRepresentation(
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    id="id_example",
                                    name="name_example",
                                    policies=[],
                                    resources=[
                                        ResourceRepresentation(
                                            id="id_example",
                                            attributes={},
                                            display_name="display_name_example",
                                            icon_uri="icon_uri_example",
                                            name="name_example",
                                            owner_managed_access=True,
                                            scopes=[],
                                            type="type_example",
                                            uris=[
                                                "uris_example",
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            type="type_example",
                        ),
                    ],
                    policy_enforcement_mode="ENFORCING",
                    resources=[
                        ResourceRepresentation(
                            id="id_example",
                            attributes={},
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            name="name_example",
                            owner_managed_access=True,
                            scopes=[
                                ScopeRepresentation(
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    id="id_example",
                                    name="name_example",
                                    policies=[
                                        PolicyRepresentation(
                                            config={},
                                            decision_strategy="AFFIRMATIVE",
                                            description="description_example",
                                            id="id_example",
                                            logic="POSITIVE",
                                            name="name_example",
                                            owner="owner_example",
                                            policies=[
                                                "policies_example",
                                            ],
                                            resources=[
                                                "resources_example",
                                            ],
                                            resources_data=[],
                                            scopes=[
                                                "scopes_example",
                                            ],
                                            scopes_data=[],
                                            type="type_example",
                                        ),
                                    ],
                                    resources=[],
                                ),
                            ],
                            type="type_example",
                            uris=[
                                "uris_example",
                            ],
                        ),
                    ],
                    scopes=[
                        ScopeRepresentation(
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            id="id_example",
                            name="name_example",
                            policies=[
                                PolicyRepresentation(
                                    config={},
                                    decision_strategy="AFFIRMATIVE",
                                    description="description_example",
                                    id="id_example",
                                    logic="POSITIVE",
                                    name="name_example",
                                    owner="owner_example",
                                    policies=[
                                        "policies_example",
                                    ],
                                    resources=[
                                        "resources_example",
                                    ],
                                    resources_data=[
                                        ResourceRepresentation(
                                            id="id_example",
                                            attributes={},
                                            display_name="display_name_example",
                                            icon_uri="icon_uri_example",
                                            name="name_example",
                                            owner_managed_access=True,
                                            scopes=[],
                                            type="type_example",
                                            uris=[
                                                "uris_example",
                                            ],
                                        ),
                                    ],
                                    scopes=[
                                        "scopes_example",
                                    ],
                                    scopes_data=[],
                                    type="type_example",
                                ),
                            ],
                            resources=[
                                ResourceRepresentation(
                                    id="id_example",
                                    attributes={},
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    name="name_example",
                                    owner_managed_access=True,
                                    scopes=[],
                                    type="type_example",
                                    uris=[
                                        "uris_example",
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                base_url="base_url_example",
                bearer_only=True,
                client_authenticator_type="client_authenticator_type_example",
                client_id="client_id_example",
                consent_required=True,
                default_client_scopes=[
                    "default_client_scopes_example",
                ],
                description="description_example",
                direct_access_grants_enabled=True,
                enabled=True,
                frontchannel_logout=True,
                full_scope_allowed=True,
                id="id_example",
                implicit_flow_enabled=True,
                name="name_example",
                node_re_registration_timeout=1,
                not_before=1,
                oauth2_device_authorization_grant_enabled=True,
                optional_client_scopes=[
                    "optional_client_scopes_example",
                ],
                origin="origin_example",
                protocol="protocol_example",
                protocol_mappers=[
                    ProtocolMapperRepresentation(
                        config={},
                        id="id_example",
                        name="name_example",
                        protocol="protocol_example",
                        protocol_mapper="protocol_mapper_example",
                    ),
                ],
                public_client=True,
                redirect_uris=[
                    "redirect_uris_example",
                ],
                registered_nodes={},
                registration_access_token="registration_access_token_example",
                root_url="root_url_example",
                secret="secret_example",
                service_accounts_enabled=True,
                standard_flow_enabled=True,
                surrogate_auth_required=True,
                web_origins=[
                    "web_origins_example",
                ],
            ),
        ],
        groups=[
            GroupRepresentation(
                access={},
                attributes={},
                client_roles={},
                id="id_example",
                name="name_example",
                path="path_example",
                realm_roles=[
                    "realm_roles_example",
                ],
                sub_groups=[],
            ),
        ],
        identity_providers=[
            IdentityProviderRepresentation(
                add_read_token_role_on_create=True,
                alias="alias_example",
                config={},
                display_name="display_name_example",
                enabled=True,
                first_broker_login_flow_alias="first_broker_login_flow_alias_example",
                internal_id="internal_id_example",
                link_only=True,
                post_broker_login_flow_alias="post_broker_login_flow_alias_example",
                provider_id="provider_id_example",
                store_token=True,
                trust_email=True,
            ),
        ],
        if_resource_exists="if_resource_exists_example",
        policy="SKIP",
        roles=RolesRepresentation(
            client={},
            realm=[
                RoleRepresentation(
                    attributes={},
                    client_role=True,
                    composite=True,
                    composites=RoleRepresentationComposites(
                        client={},
                        realm=[
                            "realm_example",
                        ],
                    ),
                    container_id="container_id_example",
                    description="description_example",
                    id="id_example",
                    name="name_example",
                ),
            ],
        ),
        users=[
            UserRepresentation(
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
            ),
        ],
    ) # PartialImportRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Partial import from a JSON file to an existing realm.
        api_instance.realm_partial_import_post(realm, partial_import_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_partial_import_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **partial_import_representation** | [**PartialImportRepresentation**](PartialImportRepresentation.md)|  |

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

# **realm_push_revocation_post**
> realm_push_revocation_post(realm)

Push the realm’s revocation policy to any client that has an admin url associated with it.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        # Push the realm’s revocation policy to any client that has an admin url associated with it.
        api_instance.realm_push_revocation_post(realm)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_push_revocation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

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

# **realm_put**
> realm_put(realm, realm_representation)

Update the top-level information of the realm   Any user, roles or client information in the representation  will be ignored.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.realm_representation import RealmRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    realm_representation = RealmRepresentation(
        access_code_lifespan=1,
        access_code_lifespan_login=1,
        access_code_lifespan_user_action=1,
        access_token_lifespan=1,
        access_token_lifespan_for_implicit_flow=1,
        account_theme="account_theme_example",
        action_token_generated_by_admin_lifespan=1,
        action_token_generated_by_user_lifespan=1,
        admin_events_details_enabled=True,
        admin_events_enabled=True,
        admin_theme="admin_theme_example",
        attributes={},
        authentication_flows=[
            AuthenticationFlowRepresentation(
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
            ),
        ],
        authenticator_config=[
            AuthenticatorConfigRepresentation(
                alias="alias_example",
                config={},
                id="id_example",
            ),
        ],
        browser_flow="browser_flow_example",
        browser_security_headers={},
        brute_force_protected=True,
        client_authentication_flow="client_authentication_flow_example",
        client_offline_session_idle_timeout=1,
        client_offline_session_max_lifespan=1,
        client_policies=JsonNode(
            array=True,
            big_decimal=True,
            big_integer=True,
            binary=True,
            boolean=True,
            container_node=True,
            double=True,
            empty=True,
            float=True,
            floating_point_number=True,
            int=True,
            integral_number=True,
            long=True,
            missing_node=True,
            node_type="ARRAY",
            null=True,
            number=True,
            object=True,
            pojo=True,
            short=True,
            textual=True,
            value_node=True,
        ),
        client_profiles=JsonNode(
            array=True,
            big_decimal=True,
            big_integer=True,
            binary=True,
            boolean=True,
            container_node=True,
            double=True,
            empty=True,
            float=True,
            floating_point_number=True,
            int=True,
            integral_number=True,
            long=True,
            missing_node=True,
            node_type="ARRAY",
            null=True,
            number=True,
            object=True,
            pojo=True,
            short=True,
            textual=True,
            value_node=True,
        ),
        client_scope_mappings={},
        client_scopes=[
            ClientScopeRepresentation(
                attributes={},
                description="description_example",
                id="id_example",
                name="name_example",
                protocol="protocol_example",
                protocol_mappers=[
                    ProtocolMapperRepresentation(
                        config={},
                        id="id_example",
                        name="name_example",
                        protocol="protocol_example",
                        protocol_mapper="protocol_mapper_example",
                    ),
                ],
            ),
        ],
        client_session_idle_timeout=1,
        client_session_max_lifespan=1,
        clients=[
            ClientRepresentation(
                access={},
                admin_url="admin_url_example",
                always_display_in_console=True,
                attributes={},
                authentication_flow_binding_overrides={},
                authorization_services_enabled=True,
                authorization_settings=ResourceServerRepresentation(
                    allow_remote_resource_management=True,
                    client_id="client_id_example",
                    decision_strategy="AFFIRMATIVE",
                    id="id_example",
                    name="name_example",
                    policies=[
                        PolicyRepresentation(
                            config={},
                            decision_strategy="AFFIRMATIVE",
                            description="description_example",
                            id="id_example",
                            logic="POSITIVE",
                            name="name_example",
                            owner="owner_example",
                            policies=[
                                "policies_example",
                            ],
                            resources=[
                                "resources_example",
                            ],
                            resources_data=[
                                ResourceRepresentation(
                                    id="id_example",
                                    attributes={},
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    name="name_example",
                                    owner_managed_access=True,
                                    scopes=[
                                        ScopeRepresentation(
                                            display_name="display_name_example",
                                            icon_uri="icon_uri_example",
                                            id="id_example",
                                            name="name_example",
                                            policies=[],
                                            resources=[],
                                        ),
                                    ],
                                    type="type_example",
                                    uris=[
                                        "uris_example",
                                    ],
                                ),
                            ],
                            scopes=[
                                "scopes_example",
                            ],
                            scopes_data=[
                                ScopeRepresentation(
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    id="id_example",
                                    name="name_example",
                                    policies=[],
                                    resources=[
                                        ResourceRepresentation(
                                            id="id_example",
                                            attributes={},
                                            display_name="display_name_example",
                                            icon_uri="icon_uri_example",
                                            name="name_example",
                                            owner_managed_access=True,
                                            scopes=[],
                                            type="type_example",
                                            uris=[
                                                "uris_example",
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            type="type_example",
                        ),
                    ],
                    policy_enforcement_mode="ENFORCING",
                    resources=[
                        ResourceRepresentation(
                            id="id_example",
                            attributes={},
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            name="name_example",
                            owner_managed_access=True,
                            scopes=[
                                ScopeRepresentation(
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    id="id_example",
                                    name="name_example",
                                    policies=[
                                        PolicyRepresentation(
                                            config={},
                                            decision_strategy="AFFIRMATIVE",
                                            description="description_example",
                                            id="id_example",
                                            logic="POSITIVE",
                                            name="name_example",
                                            owner="owner_example",
                                            policies=[
                                                "policies_example",
                                            ],
                                            resources=[
                                                "resources_example",
                                            ],
                                            resources_data=[],
                                            scopes=[
                                                "scopes_example",
                                            ],
                                            scopes_data=[],
                                            type="type_example",
                                        ),
                                    ],
                                    resources=[],
                                ),
                            ],
                            type="type_example",
                            uris=[
                                "uris_example",
                            ],
                        ),
                    ],
                    scopes=[
                        ScopeRepresentation(
                            display_name="display_name_example",
                            icon_uri="icon_uri_example",
                            id="id_example",
                            name="name_example",
                            policies=[
                                PolicyRepresentation(
                                    config={},
                                    decision_strategy="AFFIRMATIVE",
                                    description="description_example",
                                    id="id_example",
                                    logic="POSITIVE",
                                    name="name_example",
                                    owner="owner_example",
                                    policies=[
                                        "policies_example",
                                    ],
                                    resources=[
                                        "resources_example",
                                    ],
                                    resources_data=[
                                        ResourceRepresentation(
                                            id="id_example",
                                            attributes={},
                                            display_name="display_name_example",
                                            icon_uri="icon_uri_example",
                                            name="name_example",
                                            owner_managed_access=True,
                                            scopes=[],
                                            type="type_example",
                                            uris=[
                                                "uris_example",
                                            ],
                                        ),
                                    ],
                                    scopes=[
                                        "scopes_example",
                                    ],
                                    scopes_data=[],
                                    type="type_example",
                                ),
                            ],
                            resources=[
                                ResourceRepresentation(
                                    id="id_example",
                                    attributes={},
                                    display_name="display_name_example",
                                    icon_uri="icon_uri_example",
                                    name="name_example",
                                    owner_managed_access=True,
                                    scopes=[],
                                    type="type_example",
                                    uris=[
                                        "uris_example",
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                base_url="base_url_example",
                bearer_only=True,
                client_authenticator_type="client_authenticator_type_example",
                client_id="client_id_example",
                consent_required=True,
                default_client_scopes=[
                    "default_client_scopes_example",
                ],
                description="description_example",
                direct_access_grants_enabled=True,
                enabled=True,
                frontchannel_logout=True,
                full_scope_allowed=True,
                id="id_example",
                implicit_flow_enabled=True,
                name="name_example",
                node_re_registration_timeout=1,
                not_before=1,
                oauth2_device_authorization_grant_enabled=True,
                optional_client_scopes=[
                    "optional_client_scopes_example",
                ],
                origin="origin_example",
                protocol="protocol_example",
                protocol_mappers=[
                    ProtocolMapperRepresentation(
                        config={},
                        id="id_example",
                        name="name_example",
                        protocol="protocol_example",
                        protocol_mapper="protocol_mapper_example",
                    ),
                ],
                public_client=True,
                redirect_uris=[
                    "redirect_uris_example",
                ],
                registered_nodes={},
                registration_access_token="registration_access_token_example",
                root_url="root_url_example",
                secret="secret_example",
                service_accounts_enabled=True,
                standard_flow_enabled=True,
                surrogate_auth_required=True,
                web_origins=[
                    "web_origins_example",
                ],
            ),
        ],
        components=MultivaluedHashMap(
            empty=True,
            load_factor=3.14,
            threshold=1,
        ),
        default_default_client_scopes=[
            "default_default_client_scopes_example",
        ],
        default_groups=[
            "default_groups_example",
        ],
        default_locale="default_locale_example",
        default_optional_client_scopes=[
            "default_optional_client_scopes_example",
        ],
        default_role=RoleRepresentation(
            attributes={},
            client_role=True,
            composite=True,
            composites=RoleRepresentationComposites(
                client={},
                realm=[
                    "realm_example",
                ],
            ),
            container_id="container_id_example",
            description="description_example",
            id="id_example",
            name="name_example",
        ),
        default_signature_algorithm="default_signature_algorithm_example",
        direct_grant_flow="direct_grant_flow_example",
        display_name="display_name_example",
        display_name_html="display_name_html_example",
        docker_authentication_flow="docker_authentication_flow_example",
        duplicate_emails_allowed=True,
        edit_username_allowed=True,
        email_theme="email_theme_example",
        enabled=True,
        enabled_event_types=[
            "enabled_event_types_example",
        ],
        events_enabled=True,
        events_expiration=1,
        events_listeners=[
            "events_listeners_example",
        ],
        failure_factor=1,
        federated_users=[
            UserRepresentation(
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
            ),
        ],
        groups=[
            GroupRepresentation(
                access={},
                attributes={},
                client_roles={},
                id="id_example",
                name="name_example",
                path="path_example",
                realm_roles=[
                    "realm_roles_example",
                ],
                sub_groups=[],
            ),
        ],
        id="id_example",
        identity_provider_mappers=[
            IdentityProviderMapperRepresentation(
                config={},
                id="id_example",
                identity_provider_alias="identity_provider_alias_example",
                identity_provider_mapper="identity_provider_mapper_example",
                name="name_example",
            ),
        ],
        identity_providers=[
            IdentityProviderRepresentation(
                add_read_token_role_on_create=True,
                alias="alias_example",
                config={},
                display_name="display_name_example",
                enabled=True,
                first_broker_login_flow_alias="first_broker_login_flow_alias_example",
                internal_id="internal_id_example",
                link_only=True,
                post_broker_login_flow_alias="post_broker_login_flow_alias_example",
                provider_id="provider_id_example",
                store_token=True,
                trust_email=True,
            ),
        ],
        internationalization_enabled=True,
        keycloak_version="keycloak_version_example",
        login_theme="login_theme_example",
        login_with_email_allowed=True,
        max_delta_time_seconds=1,
        max_failure_wait_seconds=1,
        minimum_quick_login_wait_seconds=1,
        not_before=1,
        o_auth2_device_code_lifespan=1,
        o_auth2_device_polling_interval=1,
        oauth2_device_code_lifespan=1,
        oauth2_device_polling_interval=1,
        offline_session_idle_timeout=1,
        offline_session_max_lifespan=1,
        offline_session_max_lifespan_enabled=True,
        otp_policy_algorithm="otp_policy_algorithm_example",
        otp_policy_digits=1,
        otp_policy_initial_counter=1,
        otp_policy_look_ahead_window=1,
        otp_policy_period=1,
        otp_policy_type="otp_policy_type_example",
        otp_supported_applications=[
            "otp_supported_applications_example",
        ],
        password_policy="password_policy_example",
        permanent_lockout=True,
        protocol_mappers=[
            ProtocolMapperRepresentation(
                config={},
                id="id_example",
                name="name_example",
                protocol="protocol_example",
                protocol_mapper="protocol_mapper_example",
            ),
        ],
        quick_login_check_milli_seconds=1,
        realm="realm_example",
        refresh_token_max_reuse=1,
        registration_allowed=True,
        registration_email_as_username=True,
        registration_flow="registration_flow_example",
        remember_me=True,
        required_actions=[
            RequiredActionProviderRepresentation(
                alias="alias_example",
                config={},
                default_action=True,
                enabled=True,
                name="name_example",
                priority=1,
                provider_id="provider_id_example",
            ),
        ],
        reset_credentials_flow="reset_credentials_flow_example",
        reset_password_allowed=True,
        revoke_refresh_token=True,
        roles=RolesRepresentation(
            client={},
            realm=[
                RoleRepresentation(
                    attributes={},
                    client_role=True,
                    composite=True,
                    composites=RoleRepresentationComposites(
                        client={},
                        realm=[
                            "realm_example",
                        ],
                    ),
                    container_id="container_id_example",
                    description="description_example",
                    id="id_example",
                    name="name_example",
                ),
            ],
        ),
        scope_mappings=[
            ScopeMappingRepresentation(
                client="client_example",
                client_scope="client_scope_example",
                roles=[
                    "roles_example",
                ],
                _self="_self_example",
            ),
        ],
        smtp_server={},
        ssl_required="ssl_required_example",
        sso_session_idle_timeout=1,
        sso_session_idle_timeout_remember_me=1,
        sso_session_max_lifespan=1,
        sso_session_max_lifespan_remember_me=1,
        supported_locales=[
            "supported_locales_example",
        ],
        user_federation_mappers=[
            UserFederationMapperRepresentation(
                config={},
                federation_mapper_type="federation_mapper_type_example",
                federation_provider_display_name="federation_provider_display_name_example",
                id="id_example",
                name="name_example",
            ),
        ],
        user_federation_providers=[
            UserFederationProviderRepresentation(
                changed_sync_period=1,
                config={},
                display_name="display_name_example",
                full_sync_period=1,
                id="id_example",
                last_sync=1,
                priority=1,
                provider_name="provider_name_example",
            ),
        ],
        user_managed_access_allowed=True,
        users=[
            UserRepresentation(
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
            ),
        ],
        verify_email=True,
        wait_increment_seconds=1,
        web_authn_policy_acceptable_aaguids=[
            "web_authn_policy_acceptable_aaguids_example",
        ],
        web_authn_policy_attestation_conveyance_preference="web_authn_policy_attestation_conveyance_preference_example",
        web_authn_policy_authenticator_attachment="web_authn_policy_authenticator_attachment_example",
        web_authn_policy_avoid_same_authenticator_register=True,
        web_authn_policy_create_timeout=1,
        web_authn_policy_passwordless_acceptable_aaguids=[
            "web_authn_policy_passwordless_acceptable_aaguids_example",
        ],
        web_authn_policy_passwordless_attestation_conveyance_preference="web_authn_policy_passwordless_attestation_conveyance_preference_example",
        web_authn_policy_passwordless_authenticator_attachment="web_authn_policy_passwordless_authenticator_attachment_example",
        web_authn_policy_passwordless_avoid_same_authenticator_register=True,
        web_authn_policy_passwordless_create_timeout=1,
        web_authn_policy_passwordless_require_resident_key="web_authn_policy_passwordless_require_resident_key_example",
        web_authn_policy_passwordless_rp_entity_name="web_authn_policy_passwordless_rp_entity_name_example",
        web_authn_policy_passwordless_rp_id="web_authn_policy_passwordless_rp_id_example",
        web_authn_policy_passwordless_signature_algorithms=[
            "web_authn_policy_passwordless_signature_algorithms_example",
        ],
        web_authn_policy_passwordless_user_verification_requirement="web_authn_policy_passwordless_user_verification_requirement_example",
        web_authn_policy_require_resident_key="web_authn_policy_require_resident_key_example",
        web_authn_policy_rp_entity_name="web_authn_policy_rp_entity_name_example",
        web_authn_policy_rp_id="web_authn_policy_rp_id_example",
        web_authn_policy_signature_algorithms=[
            "web_authn_policy_signature_algorithms_example",
        ],
        web_authn_policy_user_verification_requirement="web_authn_policy_user_verification_requirement_example",
    ) # RealmRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Update the top-level information of the realm   Any user, roles or client information in the representation  will be ignored.
        api_instance.realm_put(realm, realm_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **realm_representation** | [**RealmRepresentation**](RealmRepresentation.md)|  |

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

# **realm_sessions_session_delete**
> realm_sessions_session_delete(realm, session)

Remove a specific user session.

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    session = "session_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove a specific user session.
        api_instance.realm_sessions_session_delete(realm, session)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_sessions_session_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **session** | **str**|  |

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

# **realm_test_ldap_connection_post**
> realm_test_ldap_connection_post(realm, test_ldap_connection_representation)

Test LDAP connection

### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.test_ldap_connection_representation import TestLdapConnectionRepresentation
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    test_ldap_connection_representation = TestLdapConnectionRepresentation(
        action="action_example",
        auth_type="auth_type_example",
        bind_credential="bind_credential_example",
        bind_dn="bind_dn_example",
        component_id="component_id_example",
        connection_timeout="connection_timeout_example",
        connection_url="connection_url_example",
        start_tls="start_tls_example",
        use_truststore_spi="use_truststore_spi_example",
    ) # TestLdapConnectionRepresentation | 

    # example passing only required values which don't have defaults set
    try:
        # Test LDAP connection
        api_instance.realm_test_ldap_connection_post(realm, test_ldap_connection_representation)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_test_ldap_connection_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **test_ldap_connection_representation** | [**TestLdapConnectionRepresentation**](TestLdapConnectionRepresentation.md)|  |

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

# **realm_test_smtp_connection_post**
> realm_test_smtp_connection_post(realm, request_body)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.realm_test_smtp_connection_post(realm, request_body)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_test_smtp_connection_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

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

# **realm_users_management_permissions_get**
> ManagementPermissionReference realm_users_management_permissions_get(realm)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.management_permission_reference import ManagementPermissionReference
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_users_management_permissions_get(realm)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_users_management_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

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

# **realm_users_management_permissions_put**
> ManagementPermissionReference realm_users_management_permissions_put(realm, management_permission_reference)



### Example

* Bearer Authentication (access_token):

```python
import time
import keycloak_api
from keycloak_api.api import realms_admin_api
from keycloak_api.model.management_permission_reference import ManagementPermissionReference
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
    api_instance = realms_admin_api.RealmsAdminApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
    management_permission_reference = ManagementPermissionReference(
        enabled=True,
        resource="resource_example",
        scope_permissions={},
    ) # ManagementPermissionReference | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.realm_users_management_permissions_put(realm, management_permission_reference)
        pprint(api_response)
    except keycloak_api.ApiException as e:
        print("Exception when calling RealmsAdminApi->realm_users_management_permissions_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **str**| realm name (not id!) |
 **management_permission_reference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  |

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

