import sqlite3

# 1. Create or open an SQLite database file

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect("example.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# list the existing tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
# Fetch all the rows
rows = cursor.fetchall()
print("Existing tables:")
for row in rows:
    print(row)

# 2. Create a table

q = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
"""
cursor.execute(q)

# Commit the changes
conn.commit()

# Check if the table was successfully created
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
table_exists = cursor.fetchone() is not None

print("Table exists:", table_exists)

# 3. Insert data into the table

q = """
INSERT INTO users (name, age, email)
VALUES (?, ?, ?)
"""
cursor.execute(q, ("John Doe", 30, "john.doe@example.com"))
conn.commit()

# use row.count to check the number of affected rows
rows_affected = cursor.rowcount
print("Rows affected:", rows_affected)

# insert multiple rows

users = [
    ("Jane Smith", 28, "jane.smith@example.com"),
    ("Alice Johnson", 32, "alice.johnson@example.com"),
]
cursor.executemany(q, users)
conn.commit()

rows_affected = cursor.rowcount
print("users inserted:", rows_affected)

# 4. retrieve data

q = "SELECT * FROM users"
cursor.execute(q)
rows = cursor.fetchall()

for row in rows:
    print(row)

q = "SELECT * FROM users WHERE name = ?"
cursor.execute(q, ("Jane Smith",))
rows = cursor.fetchall()
if rows:
    print(rows[0])

# 5. Update data

q = "UPDATE users SET age = ? WHERE name = ?"
cursor.execute(q, (31, "Jane Smith"))
conn.commit()

rows_affected = cursor.rowcount
print("users updated:", rows_affected)

# check if it was updated

q = "SELECT * FROM users WHERE name = ?"
cursor.execute(q, ("Jane Smith",))
rows = cursor.fetchall()
if rows:
    print(rows[0])

# 6. Delete data

q = "DELETE FROM users WHERE id = ?"
cursor.execute(q, (2,))
conn.commit()

rows_affected = cursor.rowcount
print("users deleted:", rows_affected)

q = "SELECT * FROM users"
cursor.execute(q)
rows = cursor.fetchall()
for row in rows:
    print(row)

# 7. Close the connection

cursor.close()
conn.close()
