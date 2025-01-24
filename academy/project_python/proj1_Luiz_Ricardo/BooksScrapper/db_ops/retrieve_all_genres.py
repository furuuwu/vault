"""
The genres are stored almost "as is". We only enforce case-insensitive uniqueness for the name column in the genre table.
So yes, there are A LOT of weird things in here BUT it is what it is!
"""

import sqlite3
import os


def retrieve_all():
    db_path = os.path.abspath("db/books.db")  # Adjust path as needed

    if not os.path.exists(db_path):
        print(f"No database file found at {db_path}.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Replace with your actual table names and columns
        cursor.execute("SELECT * FROM genre;")  # Example query to get all books
        rows = cursor.fetchall()

        if rows:
            print("All records from 'genre' table:")
            for row in rows:
                print(row)
        else:
            print("No records found in the 'genre' table.")

    except sqlite3.Error as e:
        print(f"Error retrieving data: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    retrieve_all()
