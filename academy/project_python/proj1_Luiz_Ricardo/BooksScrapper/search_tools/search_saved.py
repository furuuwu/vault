"""
Create a script to search the saved books by:
• By price
• Stock
• Title
• Author
• Keywords on description
The script must run on cmd, and ask the user the field to search for first

"""

import sqlite3


def search_saved_books():
    """Main function to allow users to search saved books."""
    try:
        # Prompt for search criteria
        print("Search saved books by:")
        print("1. Price")
        print("2. Stock")
        print("3. Title")
        print("4. Author")
        print("5. Keywords in description")

        # Input validation for search field
        while True:
            search_field = input("Please choose an option (1-5): ").strip()
            if search_field in ["1", "2", "3", "4", "5"]:
                break  # Exit loop when a valid input is given
            print("Invalid option. Please choose a number between 1 and 5.")

        # Based on the search choice, gather relevant input
        if search_field == "1":
            while True:
                try:
                    # Input validation for prices
                    min_price = float(input("Enter minimum price: "))
                    max_price = float(input("Enter maximum price: "))
                    if min_price > max_price:
                        print(
                            "Minimum price cannot be greater than maximum price. Please try again."
                        )
                        continue  # Restart the loop if invalid range is entered
                    break  # Exit loop if input is valid
                except ValueError:
                    print(
                        "Invalid input! Please enter valid numbers for minimum and maximum prices."
                    )

            results = search_by_price(min_price, max_price)

        elif search_field == "2":
            while True:
                try:
                    # Input validation for stock number
                    min_stock = int(input("Enter minimum stock number: "))
                    break  # Exit loop if input is valid
                except ValueError:
                    print(
                        "Invalid input! Please enter a valid integer for the minimum stock number."
                    )

            results = search_by_stock(min_stock)

        elif search_field == "3":
            while True:
                # Ensure title is not empty
                title_search = input("Enter part of the title to search for: ").strip()
                if title_search:
                    break  # Exit loop if title input is valid
                print("Title cannot be empty. Please try again.")

            results = search_by_title(title_search)

        elif search_field == "4":
            while True:
                # Ensure author name is not empty
                author_search = input(
                    "Enter part of the author name to search for: "
                ).strip()
                if author_search:
                    break  # Exit loop if author input is valid
                print("Author name cannot be empty. Please try again.")

            results = search_by_author(author_search)

        elif search_field == "5":
            while True:
                # Ensure keyword is not empty
                keyword = input(
                    "Enter a keyword to search in the description: "
                ).strip()
                if keyword:
                    break  # Exit loop if keyword input is valid
                print("Keyword cannot be empty. Please try again.")

            results = search_by_description(keyword)

        # Display the results
        if results:
            print(f"\nFound {len(results)} book(s) matching your search:")
            for book in results:
                print(
                    f"Title: {book[0]}, Author: {book[1]}, Price: {book[2]}, Stock: {book[3]}, Summary: {book[4]}, Genre: {book[5]}"
                )
        else:
            print("No books found matching your search criteria.")

    except ValueError as e:
        print(f"Invalid input: {e}")


def search_saved_books_v1():
    """Main function to allow users to search saved books."""
    try:
        # Prompt for search criteria
        print("Search saved books by:")
        print("1. Price")
        print("2. Stock")
        print("3. Title")
        print("4. Author")
        print("5. Keywords in description")
        search_field = input("Please choose an option (1-5): ").strip()

        while search_field not in ["1", "2", "3", "4", "5"]:
            print("Invalid option. Please choose a number between 1 and 5.")
            search_field = input("Please choose an option (1-5): ").strip()

        # Based on the search choice, gather relevant input
        if search_field == "1":
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            results = search_by_price(min_price, max_price)
        elif search_field == "2":
            min_stock = int(input("Enter minimum stock number: "))
            results = search_by_stock(min_stock)
        elif search_field == "3":
            title_search = input("Enter part of the title to search for: ").strip()
            results = search_by_title(title_search)
        elif search_field == "4":
            author_search = input(
                "Enter part of the author name to search for: "
            ).strip()
            results = search_by_author(author_search)
        elif search_field == "5":
            keyword = input("Enter a keyword to search in the description: ").strip()
            results = search_by_description(keyword)

        # Display the results
        if results:
            print(f"\nFound {len(results)} book(s) matching your search:")
            for book in results:
                print(
                    f"Title: {book[0]}, Author: {book[1]}, Price: {book[2]}, Stock: {book[3]}, Summary: {book[4]}, Genre: {book[5]}"
                )
        else:
            print("No books found matching your search criteria.")

    except ValueError as e:
        print(f"Invalid input: {e}")


def search_by_price(min_price, max_price):
    """Searches saved books based on price range."""
    conn = sqlite3.connect("db/books.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, author, price, stock_number, summary, genre
        FROM saved_books
        WHERE price BETWEEN ? AND ?
    """,
        (min_price, max_price),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def search_by_stock(min_stock):
    """Searches saved books based on minimum stock number."""
    conn = sqlite3.connect("db/books.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, author, price, stock_number, summary, genre
        FROM saved_books
        WHERE stock_number >= ?
    """,
        (min_stock,),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def search_by_title(title_search):
    """Searches saved books by title."""
    conn = sqlite3.connect("db/books.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, author, price, stock_number, summary, genre
        FROM saved_books
        WHERE title LIKE ?
    """,
        ("%" + title_search + "%",),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def search_by_author(author_search):
    """Searches saved books by author."""
    conn = sqlite3.connect("db/books.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, author, price, stock_number, summary, genre
        FROM saved_books
        WHERE author LIKE ?
    """,
        ("%" + author_search + "%",),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def search_by_description(keyword):
    """Searches saved books based on a keyword in the description."""
    conn = sqlite3.connect("db/books.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT title, author, price, stock_number, summary, genre
        FROM saved_books
        WHERE summary LIKE ?
    """,
        ("%" + keyword + "%",),
    )
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == "__main__":
    search_saved_books()
