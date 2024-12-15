# SQLAlchemy

For the purposes of learning how to use this, i stick to the simplest database (sqlite)

## Installation

This will be for Version 2.0

https://docs.sqlalchemy.org/en/20/intro.html#installation

![](img/2024-12-15-17-48-43.png)

When pip is available, the distribution can be downloaded from PyPI and installed in one step:

`pip install SQLAlchemy`

## Check the version

```python
import sqlalchemy

sqlalchemy.__version__
```

## Core layer

You can use raw SQL directly with SQLAlchemy's Core layer. Why use SQLAlchemy for raw SQL instead of sqlite3?
* Database Independence: You can switch between databases (e.g., SQLite, PostgreSQL, MySQL) by just changing the connection string.
* Connection Pooling: SQLAlchemy provides efficient connection management.
* Transactions: Automatically manages transactions, ensuring consistency.
* Integration: Combines raw SQL with the flexibility of SQLAlchemy Core or ORM.

1. Create a connection to the database

Select a database engine and a driver

For that, you create a database engine. The url passed depends on the database and driver

`"<dialect>+<driver>://<username>:<password>@<host>:<port>/<db_name>"`

the dialect is the database you are using; and you can add an optional driver

```python
# Create a Connection to the Database

db_url_postgres = 'postgresql://username:password@localhost/my_database'
# 'postgresql+psycopg2://username:password@localhost/my_database'

db_url_mysql = 'mysql://username:password@localhost/my_database'
# 'mysql+pymysql://username:password@localhost/my_database'

db_url_mssql = 'mssql+pyodbc://username:password@server/my_database?driver=SQL Server'

db_url_sqlite = 'sqlite:///my_database.db'
engine = sqlalchemy.create_engine(db_url_sqlite, echo=True)

# Connect to the database
connection = engine.connect()
```

The path to the database can be specified like this

```python
# create a database books1 at the root of the project directory
db_url1 = "sqlite:///books1.db"
engine1 = sqlalchemy.create_engine(db_url1)

# create a database books2 at the relative path /db/
db_url2 = "sqlite:///db/books2.db"
engine2 = sqlalchemy.create_engine(db_url2)

# create a database books3 at the absolute path /path/to/db/books3.db
# the difference is there's an additional slash (/)
# engine = sqlalchemy.create_engine('sqlite:////path/to/db/books3.db')

connection1 = engine1.connect()
connection2 = engine2.connect()
```

2. Execute raw SQL

```python

# Create a table
connection.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
''')


# Insert data
connection.execute('''
INSERT INTO users (name, age, email)
VALUES ('Alice', 30, 'alice@example.com')
''')


# Retrieve/read data
result = connection.execute('SELECT * FROM users')

for row in result:
    print(row)

# Update data
connection.execute('''
UPDATE users
SET age = 31
WHERE name = 'Alice'
''')


# Delete data
connection.execute('''
DELETE FROM users
WHERE name = 'Alice'
''')

```

3. Use parameters for secure queries

```python
connection.execute(
    '''
    INSERT INTO users (name, age, email)
    VALUES (:name, :age, :email)
    ''',
    {"name": "Bob", "age": 25, "email": "bob@example.com"}
)
```

4. Use transactions

SQLAlchemy automatically manages transactions, but you can explicitly use them.

```python
with engine.begin() as conn:
    conn.execute('INSERT INTO users (name, age, email) VALUES ("Charlie", 28, "charlie@example.com")')
    conn.execute('UPDATE users SET age = 29 WHERE name = "Charlie"')
```
