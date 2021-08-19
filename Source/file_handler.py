import json, os
from datetime import date
import converter
import csv

class FileHandler():
    def readExchange(self):
        with open("data/exchange_rates.json") as json_file:
            return json.load(json_file)

    def readSymbols(self):
        with open("data/symbols.json") as json_file:
            return json.load(json_file)

    def saveExchange(self, base, target, value):
        c = converter.Converter()
        f = open("data/saved_conversions.csv", 'a')
        data = str(date.today()) + ';' + base + ';' + target + ';' + str(value) + ';' + str(c.convert(base, target, value)) + '\n'
        f.write(data)
        f.close()

    def readSavedConversions(self):
        csvPath = "data/saved_conversions.csv"
        with open(csvPath) as saved_conversions:
            reader = csv.reader(saved_conversions)

            data_list = []
            data = ''
            for row in reader:
                for i in row[0]:
                    if(i != ';'):
                        data += i
                    if(i == ';'):
                        data_list.append(data)
                        data = ''
                data_list.append(data)
                data = ''
                yield data_list
                data_list = []


if __name__ == '__main__':
    fh = FileHandler()
    x = fh.readSavedConversions()
    for data in x:
        print(data)
