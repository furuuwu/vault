#

## Delimiters and mysql.connector

The error you're encountering (`MySQLInterfaceError: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax`) is related to how MySQL handles `DELIMITER` and triggers within a script.

### The problem

- In MySQL, the `DELIMITER` command is used to change the statement delimiter temporarily. However, the `mysql.connector` (the Python MySQL library) does not support the `DELIMITER` statement because it expects standard SQL queries where semicolons (`;`) mark the end of each statement.
- The `DELIMITER` command is typically used in interactive MySQL clients, but it is not valid in standard SQL execution from code like this.

### Solution

To fix this issue, you need to remove the `DELIMITER` statement from the SQL file, as it’s unnecessary when running the script from Python using `mysql.connector`. Instead, you should execute each SQL statement individually or use `multi=True` and ensure each statement is separated by a semicolon `;`.

### Steps to resolve

1. **Remove `DELIMITER` from the SQL file**: Edit the `sakila-schema.sql` and remove the `DELIMITER` statement. Specifically, remove:

   ```sql
   DELIMITER ;;
   ```

2. **Modify the trigger definition**: Ensure the trigger definition ends with a single semicolon (`;`):

   ```sql
   CREATE TRIGGER `ins_film` AFTER INSERT ON `film` FOR EACH ROW BEGIN
       INSERT INTO film_text (film_id, title, description)
           VALUES (new.film_id, new.title, new.description);
   END;
   ```

### Updated `sakila-schema.sql` snippet (after removing `DELIMITER`)

```sql
-- Triggers for loading film_text from film
CREATE TRIGGER `ins_film` AFTER INSERT ON `film` FOR EACH ROW BEGIN
    INSERT INTO film_text (film_id, title, description)
        VALUES (new.film_id, new.title, new.description);
END;
```

### Additional Notes

- Ensure that no other `DELIMITER` commands are present in your SQL file.
- When using `multi=True`, ensure that each SQL statement is properly terminated with a semicolon.

### Example adjusted code

Here’s your Python code again, which should now work after making the change to the SQL file.

```python
import mysql.connector

db_config = {
    'host': '172.18.0.6',  # or 'mysql' if resolved correctly
    'user': 'root',
    'password': 'rootpassword',
    'database': 'sakila'
}

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Run sakila-schema.sql
    with open('./sakila-db/sakila-schema.sql', 'r') as schema_file:
        schema_sql = schema_file.read()
        for result in cursor.execute(schema_sql, multi=True):
            # Consume all results
            print(result)

    connection.commit()  # Commit schema changes
    
    # Run sakila-data.sql
    with open('./sakila-db/sakila-data.sql', 'r') as data_file:
        data_sql = data_file.read()
        for result in cursor.execute(data_sql, multi=True):
            # Consume all results
            print(result)

    connection.commit()  # Commit data changes
    print("Sakila database loaded successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
```

This should resolve the syntax error related to the `DELIMITER` and allow your triggers to be created properly. Let me know if you need further assistance!
