import sqlite3

# Connect to your SQLite database (change the database name as needed)
connection = sqlite3.connect('db/books.db')
cursor = connection.cursor()

# SQL command to delete all rows from the table
cursor.execute("DELETE FROM book")
cursor.execute("DELETE FROM genre")
cursor.execute("DELETE FROM saved_books")
cursor.execute("DELETE FROM book_genre")
# Commit changes and close the connection
connection.commit()
connection.close()

print("Database erased successfully!")