"""This module normalize the house data."""

import sys
import os.path

from utils.args import getopts
from constants import HEADERS, DEFAULT_CITY_FILTER
from utils.csv import readHousesCSVToList, writeHousesCSVFromList

# Arguments handling
ARGS = getopts(sys.argv)

if ARGS.get('-i') is None:
    FILES = filter(os.path.isfile, ARGS.get('-i'))

    if len(FILES) != len(ARGS.get('-i')):
        print('Please provide a valid input file')
        exit()

CITY = DEFAULT_CITY_FILTER if ARGS.get('-f') is None else ARGS.get('-f')

for inputFile in ARGS.get('-i'):
    # Body of the data handling
    print('Filtering ' + inputFile + ' for cities: ' + ', '.join(CITY))
    with open(inputFile, 'rt', encoding='utf-8') as csvfile:
        RES = list(filter(lambda x: x[HEADERS.get(
            'town_city')] in CITY, readHousesCSVToList(csvfile)))

        FILENAME = inputFile.split('/').pop()

        DEST = writeHousesCSVFromList('./data/' + FILENAME, RES)

        print('Number of transactions for this city: ' + str(len(RES)))
