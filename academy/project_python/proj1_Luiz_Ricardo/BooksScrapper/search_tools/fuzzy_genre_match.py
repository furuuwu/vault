from rapidfuzz import process, fuzz


def get_similar_genre(user_input, available_genres, threshold=40):
    """
    Find the most similar genres based on user input.

    Args:
        user_input (str): The genre input from the user.
        available_genres (dict): Dictionary of available genres with IDs as keys.
        threshold (int): Minimum similarity score to consider a match.

    Returns:
        list: List of (genre_id, genre_name, score) for similar genres.
    """
    genre_names = list(available_genres.values())
    matches = process.extract(user_input, genre_names, scorer=fuzz.ratio, limit=5)

    # Filter matches above the similarity threshold
    """
    similar_genres = [
        (genre_id, genre_name, score)
        for genre_name, score, genre_id in matches
        if score >= threshold
    ]
    """
    similar_genres = [
        (genre_id, genre_name, score)
        for genre_name, score, _ in matches
        for genre_id, name in available_genres.items()
        if name == genre_name
        if score >= threshold
    ]

    return similar_genres


def search_books_with_fuzzy_genres():
    try:
        genre_quantity = int(
            input("How many genres would you like to search for? (MAX 3): ")
        )
        while genre_quantity < 1 or genre_quantity > 3:
            print("Please enter a number between 1 and 3.")
            genre_quantity = int(
                input("How many genres would you like to search for? (MAX 3): ")
            )

        genre_list_input = []

        for _ in range(genre_quantity):
            user_input = input("Tell me a genre: ").strip()
            similar_genres = get_similar_genre(user_input, available_genres)

            if similar_genres:
                print("Here are the closest matches:")
                for idx, (genre_id, genre_name, score) in enumerate(similar_genres, 1):
                    print(f"{idx}. {genre_name} (Similarity: {score}%)")

                # Let user select one of the similar genres
                choice = int(input("Select a genre by number: "))
                while choice < 1 or choice > len(similar_genres):
                    print("Invalid choice. Try again.")
                    choice = int(input("Select a genre by number: "))

                selected_genre = similar_genres[choice - 1][1]
                genre_list_input.append(selected_genre)
            else:
                print("No similar genres found. Please try again.")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":

    # Convert the genres tuple into a dictionary for quick lookups
    available_genres = {
        10898: "logic",
        10899: "lugares imaginarios",
        10900: "mythical animals",
        # (Add the rest of the genres here)
    }

    search_books_with_fuzzy_genres()
