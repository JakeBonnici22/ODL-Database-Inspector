import pyodbc
from pyodbc import Row


def get_connection(connection_string: str) -> pyodbc.Connection:
    return pyodbc.connect(connection_string)


def read_sql_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()


def execute_query(connection: pyodbc.Connection, query: str) -> list[Row]:
    """return results of the query"""
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


