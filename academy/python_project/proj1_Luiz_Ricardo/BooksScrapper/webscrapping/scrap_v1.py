import re
from bs4 import BeautifulSoup

import requests


m_url = "https://books.toscrape.com/catalogue/page-1.html"


res = requests.get(m_url)

# print(res.content)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())


# Sample HTML
html_content = '''
<article class="product_pod">
    <div class="image_container">
        <a href="frankenstein_20/index.html">
            <img src="../media/cache/00/25/0025515e987a1ebd648773f9ac70bfe6.jpg" alt="Frankenstein" class="thumbnail">
        </a>
    </div>
    <p class="star-rating Two">
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
    </p>
    <h3><a href="frankenstein_20/index.html" title="Frankenstein">Frankenstein</a></h3>
    <div class="product_price">
        <p class="price_color">£38.00</p>
        <p class="instock availability">
            <i class="icon-ok"></i>
            In stock
        </p>
        <form>
            <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
        </form>
    </div>
</article>
'''

soup_sample = BeautifulSoup(html_content, 'html.parser')


article_sample = soup_sample.find('article', class_='product_pod')
link_sample = article_sample.find('a', href=True)['href']
print("Extracted link:", link_sample)


# Extract the link
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

# details_urls = [base_url + link for link in links]



html_product_main = '''
<div class="col-sm-6 product_main">
            <h1>A Light in the Attic</h1>
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock (22 available)
</p>
    <p class="star-rating Three">
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>
        <i class="icon-star"></i>

        <!-- <small><a href="/catalogue/a-light-in-the-attic_1000/reviews/">
                    0 customer reviews
        </a></small>
         -->&nbsp;
<!-- 
    <a id="write_review" href="/catalogue/a-light-in-the-attic_1000/reviews/add/#addreview" class="btn btn-success btn-sm">
        Write a review
    </a>
 --></p>
            <hr>
            <div class="alert alert-warning" role="alert"><strong>Warning!</strong> This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning.</div>
        </div>
'''


soup_product_main = BeautifulSoup(html_product_main, 'html.parser')
# `product_main`
product_main = soup_product_main.find('div', class_='product_main')

# Extract the title
title_text = product_main.find('h1').text
print(title_text)

# Extract the price
price_text = product_main.find(class_ = 'price_color').text
print(price_text)

instock_availability = product_main.find(class_ = 'instock availability')

print(instock_availability)
availability_text = instock_availability.text.strip()
print(availability_text)
# Extract the number using a regular expression
available_number = re.search(r'\((\d+)\s+available\)', availability_text).group(1)
print(available_number)


html_product_description = '''
<div class="product_page">
    <div class="product_description">
        <h2>Product Description</h2>
    </div>
    <p>This is the description of the product.</p>
    <p class="price_color">£38.00</p>
</div>
'''

soup_product_description = BeautifulSoup(html_product_description, 'html.parser')
# 'product_description'
product_description = soup_product_description.find('div', class_='product_description')

# Find the next <p> tag in the DOM
product_summary_text = product_description.find_next('p').text

print(product_summary_text)

html_upc = '''
<tbody>
    <tr>
        <th>UPC</th><td>38d45839cb1c83c1</td>
    </tr>
    <tr>
        <th>Product Type</th><td>Books</td>
    </tr>
    <tr>
        <th>Price (excl. tax)</th><td>£30.81</td>
    </tr>
    <tr>
        <th>Price (incl. tax)</th><td>£30.81</td>
    </tr>
    <tr>
        <th>Tax</th><td>£0.00</td>
    </tr>
    <tr>
        <th>Availability</th>
        <td>In stock (16 available)</td>
    </tr>
    <tr>
        <th>Number of reviews</th>
        <td>0</td>
    </tr>
</tbody>
'''

soup_upc = BeautifulSoup(html_upc, 'html.parser')

# Find the <th> tag with the text 'UPC'
upc_th = soup_upc.find('th', string='UPC')

# Find the corresponding <td> next to the <th>
upc_text = upc_th.find_next('td').text

print(upc_text)