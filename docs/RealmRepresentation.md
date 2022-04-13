# RealmRepresentation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_code_lifespan** | **int** |  | [optional] 
**access_code_lifespan_login** | **int** |  | [optional] 
**access_code_lifespan_user_action** | **int** |  | [optional] 
**access_token_lifespan** | **int** |  | [optional] 
**access_token_lifespan_for_implicit_flow** | **int** |  | [optional] 
**account_theme** | **str** |  | [optional] 
**action_token_generated_by_admin_lifespan** | **int** |  | [optional] 
**action_token_generated_by_user_lifespan** | **int** |  | [optional] 
**admin_events_details_enabled** | **bool** |  | [optional] 
**admin_events_enabled** | **bool** |  | [optional] 
**admin_theme** | **str** |  | [optional] 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**authentication_flows** | [**[AuthenticationFlowRepresentation]**](AuthenticationFlowRepresentation.md) |  | [optional] 
**authenticator_config** | [**[AuthenticatorConfigRepresentation]**](AuthenticatorConfigRepresentation.md) |  | [optional] 
**browser_flow** | **str** |  | [optional] 
**browser_security_headers** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**brute_force_protected** | **bool** |  | [optional] 
**client_authentication_flow** | **str** |  | [optional] 
**client_offline_session_idle_timeout** | **int** |  | [optional] 
**client_offline_session_max_lifespan** | **int** |  | [optional] 
**client_policies** | [**JsonNode**](JsonNode.md) |  | [optional] 
**client_profiles** | [**JsonNode**](JsonNode.md) |  | [optional] 
**client_scope_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**client_scopes** | [**[ClientScopeRepresentation]**](ClientScopeRepresentation.md) |  | [optional] 
**client_session_idle_timeout** | **int** |  | [optional] 
**client_session_max_lifespan** | **int** |  | [optional] 
**clients** | [**[ClientRepresentation]**](ClientRepresentation.md) |  | [optional] 
**components** | [**MultivaluedHashMap**](MultivaluedHashMap.md) |  | [optional] 
**default_default_client_scopes** | **[str]** |  | [optional] 
**default_groups** | **[str]** |  | [optional] 
**default_locale** | **str** |  | [optional] 
**default_optional_client_scopes** | **[str]** |  | [optional] 
**default_role** | [**RoleRepresentation**](RoleRepresentation.md) |  | [optional] 
**default_signature_algorithm** | **str** |  | [optional] 
**direct_grant_flow** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**display_name_html** | **str** |  | [optional] 
**docker_authentication_flow** | **str** |  | [optional] 
**duplicate_emails_allowed** | **bool** |  | [optional] 
**edit_username_allowed** | **bool** |  | [optional] 
**email_theme** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**enabled_event_types** | **[str]** |  | [optional] 
**events_enabled** | **bool** |  | [optional] 
**events_expiration** | **int** |  | [optional] 
**events_listeners** | **[str]** |  | [optional] 
**failure_factor** | **int** |  | [optional] 
**federated_users** | [**[UserRepresentation]**](UserRepresentation.md) |  | [optional] 
**groups** | [**[GroupRepresentation]**](GroupRepresentation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**identity_provider_mappers** | [**[IdentityProviderMapperRepresentation]**](IdentityProviderMapperRepresentation.md) |  | [optional] 
**identity_providers** | [**[IdentityProviderRepresentation]**](IdentityProviderRepresentation.md) |  | [optional] 
**internationalization_enabled** | **bool** |  | [optional] 
**keycloak_version** | **str** |  | [optional] 
**login_theme** | **str** |  | [optional] 
**login_with_email_allowed** | **bool** |  | [optional] 
**max_delta_time_seconds** | **int** |  | [optional] 
**max_failure_wait_seconds** | **int** |  | [optional] 
**minimum_quick_login_wait_seconds** | **int** |  | [optional] 
**not_before** | **int** |  | [optional] 
**o_auth2_device_code_lifespan** | **int** |  | [optional] 
**o_auth2_device_polling_interval** | **int** |  | [optional] 
**oauth2_device_code_lifespan** | **int** |  | [optional] 
**oauth2_device_polling_interval** | **int** |  | [optional] 
**offline_session_idle_timeout** | **int** |  | [optional] 
**offline_session_max_lifespan** | **int** |  | [optional] 
**offline_session_max_lifespan_enabled** | **bool** |  | [optional] 
**otp_policy_algorithm** | **str** |  | [optional] 
**otp_policy_digits** | **int** |  | [optional] 
**otp_policy_initial_counter** | **int** |  | [optional] 
**otp_policy_look_ahead_window** | **int** |  | [optional] 
**otp_policy_period** | **int** |  | [optional] 
**otp_policy_type** | **str** |  | [optional] 
**otp_supported_applications** | **[str]** |  | [optional] 
**password_policy** | **str** |  | [optional] 
**permanent_lockout** | **bool** |  | [optional] 
**protocol_mappers** | [**[ProtocolMapperRepresentation]**](ProtocolMapperRepresentation.md) |  | [optional] 
**quick_login_check_milli_seconds** | **int** |  | [optional] 
**realm** | **str** |  | [optional] 
**refresh_token_max_reuse** | **int** |  | [optional] 
**registration_allowed** | **bool** |  | [optional] 
**registration_email_as_username** | **bool** |  | [optional] 
**registration_flow** | **str** |  | [optional] 
**remember_me** | **bool** |  | [optional] 
**required_actions** | [**[RequiredActionProviderRepresentation]**](RequiredActionProviderRepresentation.md) |  | [optional] 
**reset_credentials_flow** | **str** |  | [optional] 
**reset_password_allowed** | **bool** |  | [optional] 
**revoke_refresh_token** | **bool** |  | [optional] 
**roles** | [**RolesRepresentation**](RolesRepresentation.md) |  | [optional] 
**scope_mappings** | [**[ScopeMappingRepresentation]**](ScopeMappingRepresentation.md) |  | [optional] 
**smtp_server** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**ssl_required** | **str** |  | [optional] 
**sso_session_idle_timeout** | **int** |  | [optional] 
**sso_session_idle_timeout_remember_me** | **int** |  | [optional] 
**sso_session_max_lifespan** | **int** |  | [optional] 
**sso_session_max_lifespan_remember_me** | **int** |  | [optional] 
**supported_locales** | **[str]** |  | [optional] 
**user_federation_mappers** | [**[UserFederationMapperRepresentation]**](UserFederationMapperRepresentation.md) |  | [optional] 
**user_federation_providers** | [**[UserFederationProviderRepresentation]**](UserFederationProviderRepresentation.md) |  | [optional] 
**user_managed_access_allowed** | **bool** |  | [optional] 
**users** | [**[UserRepresentation]**](UserRepresentation.md) |  | [optional] 
**verify_email** | **bool** |  | [optional] 
**wait_increment_seconds** | **int** |  | [optional] 
**web_authn_policy_acceptable_aaguids** | **[str]** |  | [optional] 
**web_authn_policy_attestation_conveyance_preference** | **str** |  | [optional] 
**web_authn_policy_authenticator_attachment** | **str** |  | [optional] 
**web_authn_policy_avoid_same_authenticator_register** | **bool** |  | [optional] 
**web_authn_policy_create_timeout** | **int** |  | [optional] 
**web_authn_policy_passwordless_acceptable_aaguids** | **[str]** |  | [optional] 
**web_authn_policy_passwordless_attestation_conveyance_preference** | **str** |  | [optional] 
**web_authn_policy_passwordless_authenticator_attachment** | **str** |  | [optional] 
**web_authn_policy_passwordless_avoid_same_authenticator_register** | **bool** |  | [optional] 
**web_authn_policy_passwordless_create_timeout** | **int** |  | [optional] 
**web_authn_policy_passwordless_require_resident_key** | **str** |  | [optional] 
**web_authn_policy_passwordless_rp_entity_name** | **str** |  | [optional] 
**web_authn_policy_passwordless_rp_id** | **str** |  | [optional] 
**web_authn_policy_passwordless_signature_algorithms** | **[str]** |  | [optional] 
**web_authn_policy_passwordless_user_verification_requirement** | **str** |  | [optional] 
**web_authn_policy_require_resident_key** | **str** |  | [optional] 
**web_authn_policy_rp_entity_name** | **str** |  | [optional] 
**web_authn_policy_rp_id** | **str** |  | [optional] 
**web_authn_policy_signature_algorithms** | **[str]** |  | [optional] 
**web_authn_policy_user_verification_requirement** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

