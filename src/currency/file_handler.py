import json
import os
from datetime import date
import csv

class FileHandler:
    @staticmethod
    def read_exchange():
        with open("currency/data/exchange_rates.json") as json_file:
            return json.load(json_file)

    @staticmethod
    def read_symbols():
        with open("currency/data/symbols.json") as json_file:
            return json.load(json_file)

    @staticmethod
    def save_exchange(base, target, value):
        from currency.converter import Converter
        f = open("currency/data/saved_conversions.csv", 'a')
        data = str(date.today()) + ';' + base + ';' + target + ';' + str(value) + ';' + str(Converter.convert(base, target, value)) + '\n'
        f.write(data)
        f.close()

    @staticmethod
    def delete_history():
        csv_path = "currency/data/saved_conversions.csv"
        with open(csv_path, 'w') as saved_conversions:
            writer = csv.writer(saved_conversions, delimiter=";")
            writer.writerow(['date','base','target','value','result'])

    @staticmethod
    def read_saved_conversions():
        csv_path = "currency/data/saved_conversions.csv"
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
