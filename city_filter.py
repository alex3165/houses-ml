"""This module normalize the house data."""

import csv
import sys
import os.path

from utils.args import getopts
from constants import HEADERS, DEFAULT_CITY_FILTER

# Arguments handling
ARGS = getopts(sys.argv)

if ARGS.get('-i') is None or not os.path.isfile(ARGS.get('-i')[0]):
    print(os.path.isfile(ARGS.get('-i')[0]), ARGS.get('-i') is None)
    print('Please provide a valid input file')
    exit()

CITY = DEFAULT_CITY_FILTER if ARGS.get('-f') is None else ARGS.get('-f')[0]

# Body of the data handling
with open(ARGS.get('-i')[0], 'rt', encoding='utf-8') as csvfile:
    FILE = csv.reader(csvfile, delimiter=',', quotechar='|')
    RES = []
    for row in FILE:
        NEW_ROW = list(map(lambda x: x.replace('"', ''), row))
        if NEW_ROW[HEADERS.get('town_city')] == CITY:
            RES.append(NEW_ROW)

    FILENAME = ARGS.get('-i')[0].split('/').pop()

    DEST = csv.writer(open('./data/' + FILENAME, 'w'),
                      delimiter=',', quoting=csv.QUOTE_ALL)

    for row in RES:
        DEST.writerow(row)

    print('Number of transactions for this city: ' + str(len(RES)))
