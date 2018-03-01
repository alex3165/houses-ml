"""This module download the houses data."""
# pylint: disable=E0611
import urllib.request
import re
import os.path
from bs4 import BeautifulSoup

from utils.throttle import throttle

BASE_URL = 'https://data.gov.uk'


def get_page():
    with urllib.request.urlopen(BASE_URL + '/dataset/land-registry-monthly-price-paid-data') as response:
        html = response.read()
        return html.decode('utf-8')


@throttle(2, 0, 0)
def dl_progress(count, blockSize, totalSize):
    print(str(count) + '/' + str(totalSize))


SOUP = BeautifulSoup(get_page(), 'html5lib')

for elem in SOUP(text=re.compile(r'Price Paid Data YTD')):
    for el in elem.find_parents("div", {"class": "inner"}):
        link = el.find_all('a')[1]['href']
        filename = link.split('/').pop()
        filewithpath = './data/' + filename

        if os.path.isfile(filewithpath):
            open(filewithpath, 'w')

        urllib.request.urlretrieve(
            link, filename=filewithpath, reporthook=dl_progress)
