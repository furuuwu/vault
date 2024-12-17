from data.save_and_load_json import load_books_from_json, save_books_to_json
from db_ops.create_db import create_db
from db_ops.seed_db import seed_db
from search_tools.search import search_books
from webscrapping.scrap import fetch_books
from apis.get_author_and_genres import fetch_authors_and_genres


def run_etl(run_webscrapping=False, run_api=False, run_db=False):
    books = {}
    if run_webscrapping:
        # Webscrapping to fetch books
        books = fetch_books()
        save_books_to_json(books, "data/books.json")
    else:
        books = load_books_from_json("data/books.json")

    enriched_books = {}
    if run_api:
        # APIs to get additional information
        # Fetch and enrich books with author and genre data
        enriched_books = fetch_authors_and_genres(books)
        save_books_to_json(enriched_books, "data/enriched_books.json")
    else:
        enriched_books = load_books_from_json("data/enriched_books.json")
    if run_db:
        # Save to db
        create_db()
        seed_db(enriched_books)  # this needs to run only once...
    else:
        pass


def main():
    run_etl(False, False, False)
    search_books()


if __name__ == "__main__":
    main()
