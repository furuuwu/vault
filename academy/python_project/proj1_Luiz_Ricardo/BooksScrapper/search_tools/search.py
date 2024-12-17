"""
User input:
• Number of books to search
• Minimum price (must have a default value of 0)
• Maximum price (must have a default value of 100)
• Minimum stock value (mandatory)
• Books genres: 
• User input list (mandatory)
• Maximum 3
• Genres must be validated and real (figure out how to do it ☺)

Save results
"""

import sqlite3

from search_tools.fuzzy_genre_match import get_similar_genre


def search_books_v1():
    # Get user input
    try:
        number_of_books_to_search = int(
            input("How many books would you like to search for? ")
        )
        while number_of_books_to_search < 1 or number_of_books_to_search > 15:
            print("Please enter a number between 1 and 15.")
            number_of_books_to_search = int(
                input("How many books would you like to search for? ")
            )

        min_price = round(
            float(input("What should be the minimum price? (default: 0) ") or 0), 2
        )
        max_price = round(
            float(input("What should be the maximum price? (default: 100) ") or 100), 2
        )

        min_stock_value = int(
            input("What should be the minimum stock value of books available? ")
        )

        genre_quantity = int(
            input("How many genres would you like to search for? (MAX 3) ")
        )
        while genre_quantity < 1 or genre_quantity > 3:
            print("Please enter a number between 1 and 3.")
            genre_quantity = int(
                input("How many genres would you like to search for? (MAX 3) ")
            )

        genre_list_input = []
        genre_list_options = (
            get_available_genres()
        )  # Function to fetch genres from the database

        for _ in range(genre_quantity):
            genre_input = input("Tell me a genre: ").strip()
            while genre_input not in genre_list_options:
                print("Sorry! That genre does not exist.")
                genre_input = input("Tell me a genre: ").strip()
            while genre_input in genre_list_input:
                print("You already selected that genre.")
                genre_input = input("Tell me a different genre: ").strip()
            genre_list_input.append(genre_input)

        # Query the database
        results = query_books(
            number_of_books_to_search,
            min_price,
            max_price,
            min_stock_value,
            genre_list_input,
        )
        print("Search Results:")
        for book in results:
            print(book)

            """
            # Ask if user wants to save the results
            save_option = (
                input("Would you like to save the results? (yes/no): ").strip().lower()
            )
            if save_option == "yes":
                save_books(results, genre_list_input)
            """

            # Save all results at once
            if results:
                save_books(results, genre_list_input)
                print("All results have been saved successfully.")
            else:
                print("No books found matching your criteria.")
    except ValueError as e:
        print(f"Invalid input: {e}")


def search_books_v2():
    """Search books with fuzzy genre matching."""
    try:
        number_of_books_to_search = int(
            input("How many books would you like to search for? ")
        )
        while number_of_books_to_search < 1 or number_of_books_to_search > 15:
            print("Please enter a number between 1 and 15.")
            number_of_books_to_search = int(
                input("How many books would you like to search for? ")
            )

        min_price = round(
            float(input("What should be the minimum price? (default: 0) ") or 0), 2
        )
        max_price = round(
            float(input("What should be the maximum price? (default: 100) ") or 100), 2
        )

        min_stock_value = int(
            input("What should be the minimum stock value of books available? ")
        )

        genre_quantity = int(
            input("How many genres would you like to search for? (MAX 3) ")
        )
        while genre_quantity < 1 or genre_quantity > 3:
            print("Please enter a number between 1 and 3.")
            genre_quantity = int(
                input("How many genres would you like to search for? (MAX 3) ")
            )

        # Fetch available genres
        available_genres = get_available_genres()

        # Select genres with fuzzy matching
        genre_list_input = []
        for _ in range(genre_quantity):
            user_input = input("Tell me a genre: ").strip()
            similar_genres = get_similar_genre(user_input, available_genres)

            if similar_genres:
                print("Here are the closest matches:")
                for idx, (genre_id, genre_name, score) in enumerate(similar_genres, 1):
                    print(f"{idx}. {genre_name} (Similarity: {score}%)")

                choice = int(input("Select a genre by number: "))
                while choice < 1 or choice > len(similar_genres):
                    print("Invalid choice. Try again.")
                    choice = int(input("Select a genre by number: "))

                selected_genre = similar_genres[choice - 1][1]
                genre_list_input.append(selected_genre)
            else:
                print("No similar genres found. Please try again.")

        # Query the database
        results = query_books(
            number_of_books_to_search,
            min_price,
            max_price,
            min_stock_value,
            genre_list_input,
        )

        print("Search Results:")
        for book in results:
            print(book)

        # Save all results at once
        if results:
            save_books(results, genre_list_input)
            print("All results have been saved successfully.")
        else:
            print("No books found matching your criteria.")
    except ValueError as e:
        print(f"Invalid input: {e}")


def search_books():
    """Search books with fuzzy genre matching."""
    while True:
        try:
            # Ask for number of books to search
            number_of_books_to_search = int(
                input("How many books would you like to search for? ")
            )
            if number_of_books_to_search < 1 or number_of_books_to_search > 15:
                print("Please enter a number between 1 and 15.")
                continue  # Skip to the next iteration if the input is invalid
            break  # Exit the loop if the input is valid

        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 15.")

    while True:
        try:
            # Ask for minimum price
            min_price = round(
                float(input("What should be the minimum price? (default: 0) ") or 0), 2
            )
            break  # Exit loop if input is valid

        except ValueError:
            print("Invalid input! Please enter a valid number for the minimum price.")

    while True:
        try:
            # Ask for maximum price
            max_price = round(
                float(
                    input("What should be the maximum price? (default: 100) ") or 100
                ),
                2,
            )
            break  # Exit loop if input is valid

        except ValueError:
            print("Invalid input! Please enter a valid number for the maximum price.")

    while True:
        try:
            # Ask for minimum stock value
            min_stock_value = int(
                input("What should be the minimum stock value of books available? ")
            )
            break  # Exit loop if input is valid

        except ValueError:
            print("Invalid input! Please enter an integer for the minimum stock value.")

    while True:
        try:
            # Ask for number of genres to search
            genre_quantity = int(
                input("How many genres would you like to search for? (MAX 3) ")
            )
            if genre_quantity < 1 or genre_quantity > 3:
                print("Please enter a number between 1 and 3.")
                continue  # Skip to the next iteration if the input is invalid
            break  # Exit loop if input is valid

        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 3.")

    # Fetch available genres
    available_genres = get_available_genres()

    genre_list_input = []
    for _ in range(genre_quantity):
        while True:
            try:
                # Ask user to input a genre
                user_input = input("Tell me a genre: ").strip()
                if not user_input:
                    print("Genre cannot be empty. Please try again.")
                    continue

                # Get similar genres
                similar_genres = get_similar_genre(user_input, available_genres)

                if similar_genres:
                    print("Here are the closest matches:")
                    for idx, (genre_id, genre_name, score) in enumerate(
                        similar_genres, 1
                    ):
                        print(f"{idx}. {genre_name} (Similarity: {score}%)")

                    # Ask user to select a genre
                    while True:
                        try:
                            choice = int(input("Select a genre by number: "))
                            if 1 <= choice <= len(similar_genres):
                                selected_genre = similar_genres[choice - 1][1]
                                genre_list_input.append(selected_genre)
                                break  # Exit the loop if the choice is valid
                            else:
                                print("Invalid choice. Please try again.")
                        except ValueError:
                            print("Invalid input! Please enter a valid number.")
                else:
                    print("No similar genres found. Please try again.")
                break  # Exit loop once valid genre is selected

            except ValueError:
                print("Invalid input! Please try again.")

    # Query the database
    results = query_books(
        number_of_books_to_search,
        min_price,
        max_price,
        min_stock_value,
        genre_list_input,
    )

    print("Search Results:")
    for book in results:
        print(book)

    # Save all results at once
    if results:
        save_books(results, genre_list_input)
        print("All results have been saved successfully.")
    else:
        print("No books found matching your criteria.")


def get_available_genres():
    """Fetches all available genres from the database."""
    conn = sqlite3.connect("db/books.db")
    cursor = conn.cursor()
    # cursor.execute("SELECT name FROM genre")
    # genres = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT id, name FROM genre")
    genres = {
        row[0]: row[1] for row in cursor.fetchall()
    }  # Return a dictionary of {id: name}
    conn.close()
    return genres


def query_books(limit, min_price, max_price, min_stock, genres):
    """Searches books based on user input."""
    conn = sqlite3.connect("db/books.db")
    cursor = conn.cursor()

    # Create placeholders for genre filtering
    genre_placeholders = ", ".join("?" for _ in genres)

    query = f"""
        SELECT DISTINCT b.title, b.author, b.price, b.stock_number, b.summary
        FROM book AS b
        JOIN book_genre AS bg ON b.upc = bg.book_utc
        JOIN genre AS g ON bg.genre_id = g.id
        WHERE b.price BETWEEN ? AND ?
        AND b.stock_number >= ?
        AND g.name IN ({genre_placeholders})
        LIMIT ?
    """

    # Combine filters into query parameters
    params = [min_price, max_price, min_stock] + genres + [limit]

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results


def save_books(results, genres):
    """Saves search results into the saved_books table."""
    conn = sqlite3.connect("db/books.db")
    cursor = conn.cursor()

    for book in results:
        title, author, price, stock_number, summary = book

        # We need to store the genre information as well
        for genre in genres:
            cursor.execute(
                """
                INSERT INTO saved_books (title, author, price, stock_number, summary, genre)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (title, author, price, stock_number, summary, genre),
            )

    conn.commit()
    conn.close()
    print("Results have been saved.")


if __name__ == "__main__":
    search_books()
