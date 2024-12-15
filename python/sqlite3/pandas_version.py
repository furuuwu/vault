import sqlite3
import pandas as pd

# 1. Create or open an SQLite database file
conn = sqlite3.connect("example.db")

# 2. List the existing tables
tables_query = "SELECT name FROM sqlite_master WHERE type='table'"
tables = pd.read_sql_query(tables_query, conn)
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
conn.execute(create_table_query)

# Check if the table was successfully created
table_exists_query = (
    "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
)
table_exists = pd.read_sql_query(table_exists_query, conn)
print("Table exists:", not table_exists.empty)

# 4. Insert data into the table
data_to_insert = pd.DataFrame(
    {
        "name": ["John Doe"],
        "age": [30],
        "email": ["john.doe@example.com"],
    }
)
data_to_insert.to_sql("users", conn, if_exists="append", index=False)

# Insert multiple rows
additional_users = pd.DataFrame(
    {
        "name": ["Jane Smith", "Alice Johnson"],
        "age": [28, 32],
        "email": ["jane.smith@example.com", "alice.johnson@example.com"],
    }
)
additional_users.to_sql("users", conn, if_exists="append", index=False)

# 5. Retrieve data
# Retrieve all users
users_query = "SELECT * FROM users"
users = pd.read_sql_query(users_query, conn)
print("All users:")
print(users)

# Retrieve users with a specific name
specific_user_query = "SELECT * FROM users WHERE name = ?"
specific_user = pd.read_sql_query(specific_user_query, conn, params=("Jane Smith",))
print("Specific user:")
print(specific_user)

# 6. Update data
update_query = "UPDATE users SET age = ? WHERE name = ?"
conn.execute(update_query, (31, "Jane Smith"))
conn.commit()

# Verify the update
updated_user_query = "SELECT * FROM users WHERE name = ?"
updated_user = pd.read_sql_query(updated_user_query, conn, params=("Jane Smith",))
print("Updated user:")
print(updated_user)

# 7. Delete data
delete_query = "DELETE FROM users WHERE id = ?"
conn.execute(delete_query, (2,))
conn.commit()

# Verify deletion
all_users_after_deletion = pd.read_sql_query(users_query, conn)
print("All users after deletion:")
print(all_users_after_deletion)

# 8. Close the connection
conn.close()
