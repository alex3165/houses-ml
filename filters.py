"""This module normalize the house data."""

import sys

from utils.args import getopts, areArgumentsValid
from constants import HEADERS, DEFAULT_CITY_FILTER, DEFAULT_RECORD_STATUS, DEFAULT_PPD_CAT
from utils.csv import readHousesCSVToList, writeHousesCSVFromList, getAllFromInputFiles

# Arguments handling
ARGS = getopts(sys.argv)
ARE_ARGUMENTS_VALID = areArgumentsValid(["-i"], ARGS)

if not ARE_ARGUMENTS_VALID:
    print('Please provide all required arguments')
    exit()


CITY = DEFAULT_CITY_FILTER if ARGS.get('-c') is None else ARGS.get('-c')
RECORD_STATUS = DEFAULT_RECORD_STATUS if ARGS.get(
    '-r') is None else ARGS.get('-r')
PPD_CAT = DEFAULT_PPD_CAT if ARGS.get('-p') is None else ARGS.get('-p')

HOUSES = getAllFromInputFiles(ARGS.get('-i'))

# Filter out "town_city"
RES = list(filter(lambda x: x[HEADERS.get(
    'town_city')] in CITY, HOUSES))

# Filter out "ppd_category"
RES2 = list(filter(lambda x: x[HEADERS.get(
    'ppd_category')] in PPD_CAT, RES))

# Filter out "record_status"
RES3 = list(filter(lambda x: x[HEADERS.get(
    'record_status')] in RECORD_STATUS, RES))

DEST = writeHousesCSVFromList('./data/houses.csv', RES3)

print('Number of transactions for this city: ' + str(len(RES3)))
