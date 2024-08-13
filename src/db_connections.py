from utils.helpers import read_sql_from_file


def list_and_query_first_table(connection):
    """
    List all tables in the database and query the first table.

    Args:
        connection: An open pyodbc connection object.

    Returns:
        None
    """
    try:
        print("Connection successful")

        # List all tables in the database
        cursor = connection.cursor()
        cursor.execute(read_sql_from_file('./resources/sql/list_all_tables.sql'))

        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(f"Schema: {table.TABLE_SCHEMA}, Table: {table.TABLE_NAME}")

        # Query the first table
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
