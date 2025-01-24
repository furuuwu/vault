import requests

# Define the query string and format it for the URL
query = "It's Only the Himalayas"
formatted_query = query.replace(" ", "+")

# Construct the Open Library API URL
api_url = f"https://openlibrary.org/search.json?title={formatted_query}"

# Make the request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)  # Print or process the API response
else:
    print(f"Failed to retrieve data: {response.status_code}")