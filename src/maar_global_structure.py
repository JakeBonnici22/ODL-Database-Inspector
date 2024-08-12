def list_and_query_tables(connection):
    """
    List all tables in the database and optionally query the first table.

    Args:
        connection: An open pyodbc connection object.

    Returns:
        None
    """
    try:
        # List all tables in the database
        cursor = connection.cursor()
        cursor.execute("""
            SELECT TABLE_SCHEMA, TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_TYPE = 'BASE TABLE'
        """)

        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(f"Schema: {table.TABLE_SCHEMA}, Table: {table.TABLE_NAME}")

        # Optionally, query the first table in the list
        if tables:
            first_table_schema = tables[0].TABLE_SCHEMA
            first_table_name = tables[0].TABLE_NAME
            print(f"\nQuerying the first table: {first_table_name}")
            cursor.execute(f"SELECT TOP 10 * FROM {first_table_schema}.{first_table_name}")

            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except Exception as e:
        print("Error:", e)
