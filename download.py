import urllib.request
from bs4 import BeautifulSoup
import re
import os.path
from utils.throttle import throttle

BASE_URL = 'https://data.gov.uk'


def getPage():
    with urllib.request.urlopen(BASE_URL + '/dataset/land-registry-monthly-price-paid-data') as response:
        html = response.read()
        return html.decode('utf-8')


@throttle(2, 0, 0)
def dlProgress(count, blockSize, totalSize):
    print(str(count) + '/' + str(totalSize))


soup = BeautifulSoup(getPage(), 'html5lib')

for elem in soup(text=re.compile(r'Price Paid Data YTD')):
    for el in elem.find_parents("div", {"class": "inner"}):
        link = el.find_all('a')[1]['href']
        filename = link.split('/').pop()
        filewithpath = './data/' + filename

        if (os.path.isfile(filewithpath)):
            open(filewithpath, 'w')

        urllib.request.urlretrieve(
            link, filename=filewithpath, reporthook=dlProgress)
