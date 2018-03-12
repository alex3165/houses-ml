"""This module visualize the house data."""

from sys import argv

from utils.csv import readHousesCSVToList
from utils.args import getopts, areArgumentsValid
from constants import HEADERS

# Arguments handling
ARGS = getopts(argv)
ARE_ARGUMENTS_VALID = areArgumentsValid(["-i"], ARGS)

if not ARE_ARGUMENTS_VALID:
    print('Please provide all required arguments')
    exit()


def get_all_transactions_dictionary():
    output = {}
    for input_file in ARGS["-i"]:
        with open(input_file, 'rt', encoding='utf-8') as csvfile:
            res = readHousesCSVToList(csvfile)
            count = 0
            for row in res:
                code_arr = row[HEADERS.get('postcode')].split(' ')
                if len(code_arr) < 2:
                    count = count + 1
                    continue

                code_hash = code_arr[0] + code_arr[1][0]
                if code_hash in output:
                    output[code_hash].append(row)
                else:
                    output[code_hash] = [row]
    return output


TRANSACTIONS = get_all_transactions_dictionary()

print(TRANSACTIONS['EC2N2'])
