import os
import sqlite3


def create_db():

    conn = sqlite3.connect("db/books.db")
    cursor = conn.cursor()

    # Create the genre table
    """
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS genre (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name CHAR(20) NOT NULL
                );
                ''')
    """
    cursor.execute(
        """
                CREATE TABLE IF NOT EXISTS genre (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL COLLATE NOCASE UNIQUE
                );
            """
    )

    # Create the book table
    """
    # actually no need for this because the upc has to be unique. The book can have the same title but a different upc!
    cursor.execute(
        '''
    CREATE TABLE IF NOT EXISTS book (
        upc TEXT PRIMARY KEY,
        title TEXT NOT NULL COLLATE NOCASE UNIQUE,
        author TEXT NOT NULL,
        price REAL NOT NULL,
        stock_number INTEGER NOT NULL,
        summary TEXT
    );
    '''
    )
    """
    cursor.execute(
        """
                CREATE TABLE IF NOT EXISTS book (
                upc TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                price REAL NOT NULL,
                stock_number INTEGER NOT NULL,
                summary TEXT
                );
                """
    )

    # Create the junction table for the many-to-many relationship
    cursor.execute(
        """
                CREATE TABLE IF NOT EXISTS book_genre (
                book_utc TEXT NOT NULL,
                genre_id INTEGER NOT NULL,
                FOREIGN KEY(book_utc) REFERENCES books(upc),
                FOREIGN KEY(genre_id) REFERENCES genre(id)
                );
                """
    )

    # Create the a table to save search results
    cursor.execute(
        """
                CREATE TABLE IF NOT EXISTS saved_books (
                title TEXT,
                author TEXT,
                price REAL,
                stock_number INTEGER,
                summary TEXT,
                genre TEXT
                );
                """
    )

    conn.commit()
    conn.close()

    print("Tables were probably created...")


if __name__ == "__main__":
    create_db()
