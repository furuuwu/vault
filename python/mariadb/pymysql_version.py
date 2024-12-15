from sqlalchemy import create_engine, text
import os

# MariaDB Connection Setup (update with your actual credentials)
"""
username = "your_username"  # Replace with your MariaDB username
password = "your_password"  # Replace with your MariaDB password
host = "localhost"  # Or the IP of your MariaDB server
port = "3306"  # Default port for MariaDB
database = "example_db"  # Replace with your desired database name
"""
username = "root"
password = "my-secret-pw"
host = "localhost"
port = "3306"
database = "example_db"

# Create the MariaDB connection URL
# engine_url = f"mysql+mysqlclient://{username}:{password}@{host}:{port}/{database}"
engine_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

# 1. Create or open a MariaDB database
engine = create_engine(engine_url)

# Debug: Check if we can connect to the MariaDB database
try:
    with engine.connect() as connection:
        print("Successfully connected to MariaDB.")
except Exception as e:
    print("Error connecting to MariaDB:", e)

# 2. List the existing tables
with engine.connect() as connection:
    result = connection.execute(text("SHOW TABLES"))
    tables = result.fetchall()
print("Existing tables:")
print(tables)

# 3. Create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    email VARCHAR(255) UNIQUE
)
"""
with engine.connect() as connection:
    connection.execute(text(create_table_query))
    connection.commit()  # Commit changes

# Check if the table was successfully created
with engine.connect() as connection:
    result = connection.execute(text("SHOW TABLES LIKE 'users'"))
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
    connection.commit()  # Commit changes

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
    connection.commit()  # Commit changes

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
    connection.commit()  # Commit changes

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
    connection.commit()  # Commit changes

# Verify deletion
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM users"))
    all_users_after_deletion = result.fetchall()
print("All users after deletion:")
print(all_users_after_deletion)
