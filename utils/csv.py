import csv


def readHousesCSVToList(csvfile):
    FILE = csv.reader(csvfile, delimiter=',', quotechar='|')
    RES = []
    for row in FILE:
        NEW_ROW = list(map(lambda x: x.replace('"', ''), row))
        RES.append(NEW_ROW)
    return RES


def writeHousesCSVFromList(path, housesList):
    DEST = csv.writer(open(path, 'w'),
                      delimiter=',', quoting=csv.QUOTE_ALL)

    for row in housesList:
        DEST.writerow(row)

    return DEST


def getAllFromInputFiles(args):
    output = []
    for inputFile in args:
        with open(inputFile, 'rt', encoding='utf-8') as csvfile:
            NEW = readHousesCSVToList(csvfile)
            output = output + NEW
    return output
