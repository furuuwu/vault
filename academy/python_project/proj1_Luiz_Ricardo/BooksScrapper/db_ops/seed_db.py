import sqlite3


def seed_db(books):
    # Connect to SQLite database
    conn = sqlite3.connect("db/books.db")
    cursor = conn.cursor()

    # Check if the book table is empty
    cursor.execute("SELECT COUNT(*) FROM book")
    book_count = cursor.fetchone()[0]

    # Seed the book table if it is empty
    if book_count == 0:
        for book in books:
            try:
                # Validate required fields
                required_fields = [
                    "UPC",
                    "title",
                    "author",
                    "price",
                    "stock_num",
                    "summary",
                ]
                if not all(field in book for field in required_fields):
                    print(f"Skipping book due to missing fields: {book}")
                    continue

                # Insert book details
                stock_num = int(book["stock_num"])  # Ensure stock_num is an integer
                cursor.execute(
                    """
                    INSERT OR IGNORE INTO book (upc, title, author, price, stock_number, summary)
                    VALUES (?, ?, ?, ?, ?, ?)
                """,
                    (
                        book["UPC"],
                        book["title"],
                        book["author"],
                        book["price"],
                        stock_num,
                        book["summary"],
                    ),
                )

                # Insert genres and create associations
                for genre in book["genres"]:
                    # Normalize genre to lowercase
                    normalized_genre = genre.strip().lower()

                    # Insert genre if not exists
                    cursor.execute(
                        """
                        INSERT OR IGNORE INTO genre (name) VALUES (?)
                        """,
                        (normalized_genre,),
                    )

                    # Get the genre ID
                    cursor.execute(
                        "SELECT id FROM genre WHERE name = ?", (normalized_genre,)
                    )
                    genre_id = cursor.fetchone()[0]

                    # Insert into book_genre table
                    cursor.execute(
                        """
                        INSERT OR IGNORE INTO book_genre (book_utc, genre_id) VALUES (?, ?)
                        """,
                        (book["UPC"], genre_id),
                    )

            except Exception as e:
                print(f"Error processing book {book['title']}: {e}")
        else:
            print("Book table already seeded.")

    # Commit changes and close connection
    conn.commit()
    conn.close()


if __name__ == "__main__":

    # don't run this script directly
    books = [
        {
            "UPC": "0987654321",
            "title": "A Walk in the Woods",
            "author": "Some person idk",
            "price": 10.99,
            "summary": "A humorous take on hiking.",
            "stock_num": 5,
            "genres": ["Mosquitos", "Sleep"],
        }
    ]

    seed_db(books)
