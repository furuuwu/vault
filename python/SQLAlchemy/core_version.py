from sqlalchemy import create_engine, text
import os

# 1. Create or open an SQLite database file
db_path = "example.db"
engine = create_engine(f"sqlite:///{db_path}")

# Debug: Check where the database is located
print(f"Database file is located at: {os.path.abspath(db_path)}")

# 2. List the existing tables
with engine.connect() as connection:
    result = connection.execute(
        text("SELECT name FROM sqlite_master WHERE type='table'")
    )
    tables = result.fetchall()
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
    connection.commit()  # Explicit commit after table creation

# Check if the table was successfully created
with engine.connect() as connection:
    result = connection.execute(
        text("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    )
    table_exists = result.fetchall()
print("Table exists:", len(table_exists) > 0)

# 4. Insert data into the table (using bindparam for parameter binding)
data_to_insert = [("John Doe", 30, "john.doe@example.com")]
with engine.connect() as connection:
    connection.execute(
        text("INSERT INTO users (name, age, email) VALUES (:name, :age, :email)"),
        [
            {"name": name, "age": age, "email": email}
            for name, age, email in data_to_insert
        ],
    )
    connection.commit()  # Explicit commit after insert

# Insert multiple rows (using bindparam for parameter binding)
additional_users = [
    ("Jane Smith", 28, "jane.smith@example.com"),
    ("Alice Johnson", 32, "alice.johnson@example.com"),
]
with engine.connect() as connection:
    connection.execute(
        text("INSERT INTO users (name, age, email) VALUES (:name, :age, :email)"),
        [
            {"name": name, "age": age, "email": email}
            for name, age, email in additional_users
        ],
    )
    connection.commit()  # Explicit commit after insert

# 5. Retrieve data
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM users"))
    users = result.fetchall()
print("All users:")
print(users)

# Retrieve users with a specific name
with engine.connect() as connection:
    result = connection.execute(
        text("SELECT * FROM users WHERE name = :name"), {"name": "Jane Smith"}
    )
    specific_user = result.fetchall()
print("Specific user:")
print(specific_user)

# 6. Update data (using bindparam)
with engine.connect() as connection:
    connection.execute(
        text("UPDATE users SET age = :age WHERE name = :name"),
        {"age": 31, "name": "Jane Smith"},
    )
    connection.commit()  # Explicit commit after update

# Verify the update
with engine.connect() as connection:
    result = connection.execute(
        text("SELECT * FROM users WHERE name = :name"), {"name": "Jane Smith"}
    )
    updated_user = result.fetchall()
print("Updated user:")
print(updated_user)

# 7. Delete data (using bindparam)
with engine.connect() as connection:
    connection.execute(text("DELETE FROM users WHERE id = :id"), {"id": 2})
    connection.commit()  # Explicit commit after delete

# Verify deletion
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM users"))
    all_users_after_deletion = result.fetchall()
print("All users after deletion:")
print(all_users_after_deletion)
