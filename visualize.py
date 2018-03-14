"""This module visualize the house data."""

from sys import argv
import matplotlib.pyplot as plt
import plotly

from utils.csv import readHousesCSVToList
from utils.args import getopts, areArgumentsValid
from constants import HEADERS

plotly.tools.set_credentials_file(
    username='alexrieux', api_key='YpnKqaPtouuMlfXDMJei')


# Arguments handling
ARGS = getopts(argv)
ARE_ARGUMENTS_VALID = areArgumentsValid(["-i"], ARGS)

if not ARE_ARGUMENTS_VALID:
    print('Please provide all required arguments')
    exit()


OUTPUT = {}
with open(ARGS["-i"][0], 'rt', encoding='utf-8') as csvfile:
    RES = readHousesCSVToList(csvfile)
    COUNT = 0
    for row in RES:
        code_arr = row[HEADERS.get('postcode')].split(' ')
        if len(code_arr) < 2:
            COUNT = COUNT + 1
            continue

        code_hash = code_arr[0] + code_arr[1][0]
        if code_hash in OUTPUT:
            OUTPUT[code_hash].append(row)
        else:
            OUTPUT[code_hash] = [row]

HEIGHTS = list(map(len, OUTPUT.values()))

dictionary = plt.figure()

X_RANGE = range(len(OUTPUT.keys()))
X_LABELS = list(OUTPUT.keys())

plt.bar(X_RANGE, HEIGHTS, align='center')
plt.xticks(X_RANGE, X_LABELS)

plot_url = plotly.plotly.plot_mpl(dictionary, filename='mpl-dictionary')
# plt.show()
