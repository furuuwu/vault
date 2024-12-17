import json
import os


def save_books_to_json(books, filename="data/books.json"):
    # Save the list of books (dictionaries) to a JSON file
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
    print(f"Books saved to {filename}")


def load_books_from_json(filename="data/books.json"):
    if os.path.exists(filename):
        print(f"Loading books from {filename}...")
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)  # Load the list of dictionaries
    else:
        print(f"No existing file found. Need to fetch books.")
        return None
