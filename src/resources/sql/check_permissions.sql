SELECT USER_NAME(grantee_principal_id) AS UserName,
                  permission_name AS Permission,
                  state_desc AS PermissionState,
                  major_id AS ObjectId
           FROM sys.database_permissions
           WHERE USER_NAME(grantee_principal_id) = USER_NAME()
