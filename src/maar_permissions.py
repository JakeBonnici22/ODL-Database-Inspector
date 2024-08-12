def check_permissions(conn):
    try:
        print("Connection successful")

        # Simplified query to check permissions
        query = """
        SELECT 
            USER_NAME(grantee_principal_id) AS UserName,
            permission_name AS Permission,
            state_desc AS PermissionState,
            major_id AS ObjectId
        FROM 
            sys.database_permissions
        WHERE 
            USER_NAME(grantee_principal_id) = USER_NAME();
        """

        cursor = conn.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        if results:
            print("Permissions:")
            for row in results:
                print(f"User: {row.UserName}, Permission: {row.Permission}, State: {row.PermissionState}, ObjectId: {row.ObjectId}")
        else:
            print("No permissions found or user might not have sufficient access.")


    except Exception as e:
        print("Error:", e)
