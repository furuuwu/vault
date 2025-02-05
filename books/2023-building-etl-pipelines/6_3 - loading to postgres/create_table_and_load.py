import psycopg2
import json

# Database connection details
DB_NAME = "chicago_dmv"
DB_USER = "myuser"
DB_PASSWORD = "mypassword"
DB_HOST = "localhost"  # Since it's running in Docker
DB_PORT = "5432"

# SQL statement to create the table
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS my_table (
    primaryID SERIAL PRIMARY KEY,
    num_column BIGINT DEFAULT 6749380428,
    string_column CHAR(255) DEFAULT 'this is a string',
    json_column JSON DEFAULT '{"key": 1}'
);
"""

# Sample data to insert
SAMPLE_DATA = [
    (None, None, None),  # Uses default values
    (1234567890, 'Custom String', json.dumps({"key": 42, "name": "sample"})),
    (9876543210, 'Another String', json.dumps({"flag": True, "value": 99}))
]

# SQL statement to insert data
INSERT_SQL = """
INSERT INTO my_table (num_column, string_column, json_column)
VALUES (%s, %s, %s);
"""

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()

    # Create table
    cursor.execute(CREATE_TABLE_SQL)
    conn.commit()

    # Insert sample data
    cursor.executemany(INSERT_SQL, SAMPLE_DATA)
    conn.commit()

    print("Table created and sample data inserted successfully!")

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
