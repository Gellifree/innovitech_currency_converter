import json
import os
from datetime import date

import csv

class FileHandler:
    @staticmethod
    def read_exchange():
        with open("data/exchange_rates.json") as json_file:
            return json.load(json_file)
    @staticmethod
    def read_symbols():
        with open("data/symbols.json") as json_file:
            return json.load(json_file)

    @staticmethod
    def save_exchange(base, target, value):
        from converter import Converter
        f = open("data/saved_conversions.csv", 'a')
        data = str(date.today()) + ';' + base + ';' + target + ';' + str(value) + ';' + str(Converter.convert(base, target, value)) + '\n'
        f.write(data)
        f.close()

    @staticmethod
    def read_saved_conversions():
        csv_path = "data/saved_conversions.csv"
        with open(csv_path) as saved_conversions:
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
