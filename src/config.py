from os import environ

from src.utils.helpers import get_connection

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={environ['SERVER']};"
    f"DATABASE={environ['DATABASE']};"
    f"UID={environ['UID']};"
    f"PWD={environ['PWD']};"
)

CONNECTION = get_connection(conn_str)
