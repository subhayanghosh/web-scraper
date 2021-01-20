from bs4 import BeautifulSoup
import requests

urls = []

def scrape(site):
    # getting the request from url
    request = requests.get(site)
    soup = BeautifulSoup(request.text, "html.parser")
    # parsing the tree
    product_list = soup.find_all("div", "product-details match-height-content")
    for product in product_list:
        a_tags = product.find_all("a")
        for a_tag in a_tags:
            href = a_tag.attrs['href']
            urls.append(href)

    print(urls)         

scrape("https://specsonline.com/product-category/wine/")