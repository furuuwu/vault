"""
Use public APIs to complete book information
• https://openlibrary.org/developers/api
• https://github.com/thundercomb/poetrydb#readme
• https://gutendex.com/
• Find more on: https://github.com/public-apis/public-apis?tab=readme-ov-file#books

"""

import requests

def fetch_authors_and_genres(books):
    for book in books:
        query = book["title"]
        formatted_query = query.replace(" ", "+")
        api_url = f"https://openlibrary.org/search.json?title={formatted_query}"
        print(f"Fetching data from URL: {api_url}")
        
        try:
            response = requests.get(api_url, timeout=10)  # Add a timeout to avoid hanging requests
            
            # Check if the response is JSON
            if response.headers.get("Content-Type", "").startswith("application/json"):
                data = response.json()
            else:
                print(f"Non-JSON response for book '{query}': {response.text[:200]}")
                book["author"] = "Unknown"
                book["genres"] = []
                continue
            
            # Extract authors and genres
            if data.get("docs"):  # Safely check for 'docs'
                temp_dic: dict = data["docs"][0]
                book["author"] = temp_dic.get("author_name", ["Unknown"])[0]
                book["genres"] = temp_dic.get("subject", [])
            else:
                book["author"] = "Unknown"
                book["genres"] = []
        
        except requests.exceptions.RequestException as e:
            print(f"Network error for book '{query}': {e}")
            book["author"] = "Unknown"
            book["genres"] = []
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON decoding error for book '{query}': {e}")
            book["author"] = "Unknown"
            book["genres"] = []

    return books

def main():
    # Example books for independent execution
    books = [
        {
            "UPC": "0987654321",
            "title": "A Walk in the Woods",
            "price": 10.99,
            "summary": "A humorous take on hiking.",
            "stock_num": 5
        }
    ]

    enriched_books = fetch_authors_and_genres(books)
    print(enriched_books)

if __name__ == "__main__":
    main()