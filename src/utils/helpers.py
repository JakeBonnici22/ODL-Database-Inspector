import pyodbc


def get_connection(connection_string: str) -> pyodbc.Connection:
    return pyodbc.connect(connection_string)