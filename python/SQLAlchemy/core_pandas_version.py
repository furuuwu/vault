"""
changes to core_version.py:
- use of pandas
"""

from sqlalchemy import create_engine, text
import pandas as pd

# 1. Create or open an SQLite database file
engine = create_engine("sqlite:///example.db")

# 2. List the existing tables
tables_query = "SELECT name FROM sqlite_master WHERE type='table'"
with engine.connect() as connection:
    tables = pd.read_sql_query(tables_query, connection)
print("Existing tables:")
print(tables)

# 3. Create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
"""
with engine.connect() as connection:
    connection.execute(text(create_table_query))

# Check if the table was successfully created
with engine.connect() as connection:
    table_exists_query = (
        "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
    )
    table_exists = pd.read_sql_query(table_exists_query, connection)
print("Table exists:", not table_exists.empty)

# 4. Insert data into the table
data_to_insert = pd.DataFrame(
    {
        "name": ["John Doe"],
        "age": [30],
        "email": ["john.doe@example.com"],
    }
)
with engine.connect() as connection:
    data_to_insert.to_sql("users", connection, if_exists="append", index=False)

# Insert multiple rows
additional_users = pd.DataFrame(
    {
        "name": ["Jane Smith", "Alice Johnson"],
        "age": [28, 32],
        "email": ["jane.smith@example.com", "alice.johnson@example.com"],
    }
)
with engine.connect() as connection:
    additional_users.to_sql("users", connection, if_exists="append", index=False)

# 5. Retrieve data
# Retrieve all users
users_query = "SELECT * FROM users"
with engine.connect() as connection:
    users = pd.read_sql_query(users_query, connection)
print("All users:")
print(users)

# Retrieve users with a specific name
specific_user_query = "SELECT * FROM users WHERE name = :name"
with engine.connect() as connection:
    specific_user = pd.read_sql_query(
        text(specific_user_query), connection, params={"name": "Jane Smith"}
    )
print("Specific user:")
print(specific_user)

# 6. Update data
update_query = "UPDATE users SET age = :age WHERE name = :name"
with engine.connect() as connection:
    connection.execute(text(update_query), {"age": 31, "name": "Jane Smith"})

# Verify the update
updated_user_query = "SELECT * FROM users WHERE name = :name"
with engine.connect() as connection:
    updated_user = pd.read_sql_query(
        text(updated_user_query), connection, params={"name": "Jane Smith"}
    )
print("Updated user:")
print(updated_user)

# 7. Delete data
delete_query = "DELETE FROM users WHERE id = :id"
with engine.connect() as connection:
    connection.execute(text(delete_query), {"id": 2})

# Verify deletion
with engine.connect() as connection:
    all_users_after_deletion = pd.read_sql_query(users_query, connection)
print("All users after deletion:")
print(all_users_after_deletion)
