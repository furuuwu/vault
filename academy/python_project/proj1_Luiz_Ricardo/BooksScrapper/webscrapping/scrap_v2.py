import re
from bs4 import BeautifulSoup

import requests


m_url = "https://books.toscrape.com/catalogue/page-1.html"


res = requests.get(m_url)
if res.status_code != 200:
    print("Failed to GET the page")
    exit()


soup = BeautifulSoup(res.text, 'html.parser')

# Extract the link for each book detail
articles = soup.findAll('article', class_='product_pod')

links = []
for article in articles:

    links.append(article.find('a', href=True)['href'])
print("Extracted links:", links)

# https://books.toscrape.com/catalogue/frankenstein_20/index.html
# https://books.toscrape.com/catalogue/{book_url}
base_url = "https://books.toscrape.com/catalogue/"
detail_urls = []
for link in links:
    detail_urls.append(base_url + link)
print(detail_urls)

# Extract the data for each book
books = []

res = requests.get("https://books.toscrape.com/catalogue/frankenstein_20/index.html")
soup = BeautifulSoup(res.text, 'html.parser')
# `product_main`
product_main = soup.find('div', class_='product_main')

# Extract the title
title_text = product_main.find('h1').text
print(title_text)

# Extract the price
price_text = product_main.find(class_ = 'price_color').text
print(price_text)

instock_availability = product_main.find(class_ = 'instock availability')

#print(instock_availability)
availability_text = instock_availability.text.strip()
print(availability_text)
# Extract the number using a regular expression
stock_num = re.search(r'\((\d+)\s+available\)', availability_text).group(1)
print(stock_num)

# 'product_description'
product_description = soup.find('div', id='product_description')

# Find the next <p> tag in the DOM
product_summary_text = product_description.find_next('p').text

print(product_summary_text)


# Find the <th> tag with the text 'UPC'
upc_th = soup.find('th', string='UPC')

# Find the corresponding <td> next to the <th>
upc_text = upc_th.find_next('td').text

print(upc_text)

books.append({
    "UPC": upc_text,
    "title": title_text,
    "price": price_text,
    "summary": product_summary_text,
    "stock_num": stock_num
})
print(books)