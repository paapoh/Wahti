from bs4 import BeautifulSoup
import requests


class tori:
    def __init__(self, title, image, id, price, link):
        self.title = title
        self.id = id
        self.image = image
        self.link = link
        self.price = price
        self.str_id = int(id[5:])

    def __str__(self):
        return f'{self.title} | {self.price} | {self.id}'


def parseUrl(url: str):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    items_div = soup.find_all('div', class_="list_mode_thumb")[0]
    list_items = items_div.find_all('a', class_="item_row_flex")

    tori_list = []

    for listing in list_items:

        title = listing.find('div', class_="li-title").string
        image = listing.find('img', class_="item_image")['src']
        link = listing['href']
        id = listing['id']
        price = listing.find('p', class_="list_price ineuros").string
        if(price is not None):
            price = price[:-2]
        
        tori_list.append(
            tori(title, image, id, price, link)
        )
    return tori_list