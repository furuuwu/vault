import sqlite3
import os


def retrieve_all():
    db_path = os.path.abspath("db/books.db")

    if not os.path.exists(db_path):
        print(f"No database file found at {db_path}.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM book;")
        rows = cursor.fetchall()
        print("Total number of books: " + str(len(rows)))

        if rows:
            print("All records from 'book' table:")
            for row in rows:
                # print(row)
                pass
        else:
            print("No records found in the 'book' table.")

    except sqlite3.Error as e:
        print(f"Error retrieving data: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    retrieve_all()
