import urllib.request
from bs4 import BeautifulSoup
import re

def getPage():
    with urllib.request.urlopen('https://data.gov.uk/dataset/land-registry-monthly-price-paid-data') as response:
        html = response.read()
        return html.decode('utf-8')

soup = BeautifulSoup(getPage(), 'html5lib')

for elem in soup(text=re.compile(r'Price Paid Data YTD')):
    print(elem.find_parents("div", {"class": "inner"}))
