# sqlite3

Using SQLite with Python's sqlite3 module

## cursor version

* execute SQL statements

The cursor.execute method is used to run SQL commands, like creating tables, inserting, updating, or deleting data.

```python
cursor.execute(sql_query, parameters)


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

cursor.execute("""
INSERT INTO users (name, age, email)
VALUES (?, ?, ?)
""", ("John Doe", 30, "john.doe@example.com"))

```

* Execute multiple statements

Use cursor.executemany to run the same SQL statement for multiple sets of data.

```python
cursor.executemany(sql_query, list_of_parameters)


users = [
    ("Jane Smith", 28, "jane.smith@example.com"),
    ("Alice Johnson", 32, "alice.johnson@example.com")
]
cursor.executemany("""
INSERT INTO users (name, age, email)
VALUES (?, ?, ?)
""", users)
```

* Fetch data

Retrieve query results with one of the following methods:

* fetchone() - fetches a single row
* fetchall() - fetches all rows from the result set
* fetchmany(size) - fetches a specified number of rows.

```python
cursor.execute("SELECT * FROM users WHERE name = ?", ("John Doe",))
row = cursor.fetchone()
print(row)


cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)


rows = cursor.fetchmany(2)
print(rows)
```

* Count rows

The cursor.rowcount property returns the number of rows affected by the last operation.

```python
cursor.execute("""
INSERT INTO users (name, age, email)
VALUES (?, ?, ?)
""", ("John Doe", 30, "john.doe@example.com"))
print("Rows affected:", cursor.rowcount)


cursor.execute("""
UPDATE users SET age = ? WHERE name = ?
""", (31, "John Doe"))
print("Rows affected:", cursor.rowcount)
```

* Parameterized queries

Use placeholders (`?`) for secure and efficient SQL execution, especially when handling user input. This helps prevent SQL injection.

```python
cursor.execute("""
SELECT * FROM users WHERE email = ?
""", ("john.doe@example.com",))
```

* Transaction management

SQLite transactions are automatically managed, but you can explicitly control them:

* Commit Changes: Save changes to the database.
* Rollback Changes: Undo uncommitted changes.

```python
conn.commit()
conn.rollback()
```

* List database metadata

Retrieve metadata such as existing tables or columns.

```python
# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables:", tables)

# Describe table structure
cursor.execute("PRAGMA table_info(users)")
columns = cursor.fetchall()
print("Columns:", columns)
```

* Close Resources

Always close the cursor and connection when you're done.

```python
# close cursor
cursor.close()

# close connection
conn.close()
```

To ensure the connection is always closed, you can use a context manager.

```python
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL
    )
    ''')
    conn.commit()
```

## pandas version

changes:

* listing tables: Used `pd.read_sql_query` to fetch existing tables into a DataFrame.
* Inserting Data: Used `to_sql` to insert single or multiple rows from pandas DataFrames into the SQLite table.
* Retrieving Data: Replaced `cursor.fetchall()` with `pd.read_sql_query` for direct loading of query results into DataFrames.
* Updating and Deleting Data: Performed these using `conn.execute` since pandas doesn’t directly provide update/delete functionality.
* Verification: Used `pd.read_sql_query` for verifying the effects of updates and deletions.
