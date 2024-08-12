import logging
from src.config import CONNECTION
from src.maar_global_structure import list_and_query_tables
from src.maar_permissions import check_permissions
from src.maar_structure_specific import check_table_structure


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    logging.info('Starting main function.')

    try:
        with CONNECTION as conn:
            logging.info('Connection established successfully.')

            try:
                # Check permissions
                logging.info('Checking permissions.')
                check_permissions(conn)
                logging.info('Permissions checked successfully.')

                # List all tables and query the first one
                logging.info('Listing and querying tables.')
                list_and_query_tables(conn)
                logging.info('Tables listed and queried successfully.')

                # Check the structure of a specific table
                table_name = 'Orders'
                schema_name = 'Kope'
                logging.info(f'Checking structure of table: {table_name} in schema: {schema_name}.')
                check_table_structure(conn, table_name, schema_name)
                logging.info(f'Structure of table {table_name} checked successfully.')

            except Exception as e:
                logging.error(f"An error occurred during database operations: {e}")
                raise

    except Exception as e:
        logging.error(f"An error occurred while establishing connection: {e}")


if __name__ == "__main__":
    main()
