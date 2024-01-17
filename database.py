import csv
import psycopg2
from psycopg2 import sql

from constants import FILE_PATH

# Database connection parameters
db_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

# CSV file path
csv_file_path = FILE_PATH / "Cinecenter-product-sales.csv"

# Define the table schema
table_schema = [
    ('order_id', 'TEXT'),
    ('product_id', 'TEXT'),
    ('product_name', 'TEXT'),
    ('category', 'TEXT'),
    ('price', 'NUMERIC'),
    ('worth', 'NUMERIC'),
    ('status', 'TEXT'),
    ('created_at', 'TEXT')
]

# Create a connection to the PostgreSQL database
with psycopg2.connect(**db_params) as connection:
    with connection.cursor() as cursor:
        # Create a table if it doesn't exist
        table_name = 'cinecenter_bar_verkoop'

        # Optionally, drop the table if it already exists
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} {datatype}' for col, datatype in table_schema])})"
        cursor.execute(query)

        # Commit the changes
        connection.commit()

        # Read the CSV file and insert records into the table
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                # Insert the row into the table
                query = (
                    f"INSERT INTO {table_name} ({', '.join(row.keys())}) "
                    f"VALUES ({', '.join(['%s' for val in row.values()])})"
                )

                insert_query = sql.SQL(query)
                cursor.execute(insert_query, tuple(row.values()))

            # Commit the changes
            connection.commit()

print(f"Data inserted into table: {table_name}")
