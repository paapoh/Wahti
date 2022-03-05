from ast import parse
from tokenize import String
from bs4 import BeautifulSoup
import requests

def parseUrl(url: String):
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')
    items_div = soup.find_all('div', class_="list_mode_thumb")[0]
    list_items = items_div.find_all('a')
    print(list_items[0])

parseUrl('https://www.tori.fi/pirkanmaa?q=&cg=3020&w=1&st=s&st=k&st=u&st=h&st=g&c=3023&ps=&pe=&ca=11&l=0&md=th')
