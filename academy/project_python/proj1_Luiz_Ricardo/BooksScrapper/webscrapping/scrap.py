"""
Get data from web scrapping: https://books.toscrape.com/index.html
"""

import re
from bs4 import BeautifulSoup
import requests


def fetch_books():
    urls = []
    for i in range(1, 51):
        urls.append("https://books.toscrape.com/catalogue/page-" + str(i) + ".html")
    
    # m_url = "https://books.toscrape.com/catalogue/page-1.html"
    books = []
    for m_url in urls:
        print("scrapping page: " + m_url)
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
        #print("Extracted links:", links)

        base_url = "https://books.toscrape.com/catalogue/"
        detail_urls = []
        for link in links:
            detail_urls.append(base_url + link)
        print(detail_urls)

        # Extract the data for each book

        for e in detail_urls:

            res = requests.get(e)
            soup = BeautifulSoup(res.text, 'html.parser')
            # `product_main`
            product_main = soup.find('div', class_='product_main')

            # Extract the title
            title_text = product_main.find('h1').text
            # print(title_text)

            # Extract the price
            price_text = product_main.find(class_ = 'price_color').text
            # print(price_text)
            # Extract the numeric part (integer and decimal)
            price_text = re.search(r'\d+\.\d+', price_text).group()
            price = float(price_text)

            instock_availability = product_main.find(class_ = 'instock availability')

            #print(instock_availability)
            availability_text = instock_availability.text.strip()
            # print(availability_text)
            # Extract the number using a regular expression
            stock_num = re.search(r'\((\d+)\s+available\)', availability_text).group(1)
            # print(stock_num)

            # 'product_description'
            product_summary_text = ""
            product_description = soup.find('div', id='product_description')
            if product_description:

                # Find the next <p> tag in the DOM
                product_summary_text = product_description.find_next('p')
                if product_summary_text:
                    product_summary_text = product_summary_text.text
            else:
                product_summary_text = "Not available"
            # print(product_summary_text)


            # Find the <th> tag with the text 'UPC'
            upc_th = soup.find('th', string='UPC')

            # Find the corresponding <td> next to the <th>
            upc_text = upc_th.find_next('td').text

            # print(upc_text)

            books.append({
                "UPC": upc_text,
                "title": title_text,
                "price": price,
                "summary": product_summary_text,
                "stock_num": stock_num
            })

    # print(books)
    return books

if __name__ == "__main__":
    fetch_books()