from utils.csv import readHousesCSVToList
from constants import HEADERS

with open('./data/pp-2017.csv', 'rt', encoding='utf-8') as csvfile:
    RES = readHousesCSVToList(csvfile)
    DICT = {}
    COUNT = 0
    for row in RES:
        CODE_ARR = row[HEADERS.get('postcode')].split(' ')
        if len(CODE_ARR) < 2:
            COUNT = COUNT + 1
            continue

        CODE_HASH = CODE_ARR[0] + CODE_ARR[1][0]
        if CODE_HASH in DICT:
            DICT[CODE_HASH].append(row)
        else:
            DICT[CODE_HASH] = [row]
    print('Transactions without postcode: ' + str(COUNT))
