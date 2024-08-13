from config import CONNECTION
from utils.helpers import read_sql_from_file, execute_query


def check_permissions(conn):
    try:
        print("Connection successful")

        results = execute_query(CONNECTION, read_sql_from_file('./resources/sql/check_permissions.sql'))
        
        if results:
            print("Permissions:")
            for row in results:
                print(f"User: {row.UserName}, Permission: {row.Permission}, State: {row.PermissionState}, ObjectId: {row.ObjectId}")
        else:
            print("No permissions found or user might not have sufficient access.")

    except Exception as e:
        print("Error:", e)
