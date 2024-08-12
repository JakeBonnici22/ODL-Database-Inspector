def check_table_structure(connection, table_name, schema_name):
    """
    Check the structure of a specific table in the database.

    Args:
        connection: An open pyodbc connection object.
        table_name: The name of the table to inspect.
        schema_name: The schema of the table.

    Returns:
        None
    """
    try:
        # Check table structure
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = '{table_name}' AND TABLE_SCHEMA = '{schema_name}'
        """)

        columns = cursor.fetchall()
        print(f"Columns in table {schema_name}.{table_name}:")
        for column in columns:
            print(f"Column: {column.COLUMN_NAME}, Type: {column.DATA_TYPE}, Nullable: {column.IS_NULLABLE}")

    except Exception as e:
        print("Error:", e)
