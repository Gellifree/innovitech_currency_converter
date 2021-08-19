import json, os
from datetime import date
import converter

class FileHandler():
    def read_exchange(self):
        with open("data/exchange_rates.json") as json_file:
            return json.load(json_file)

    def read_symbols(self):
        with open("data/symbols.json") as json_file:
            return json.load(json_file)

    def save_exchange(self, base, target, value):
        c = converter.Converter()
        f = open("data/saved_conversions.csv", 'a')
        data = str(date.today()) + ';' + base + ';' + target + ';' + str(value) + ';' + str(c.convert(base, target, value)) + '\n'
        f.write(data)
        f.close()

if __name__ == '__main__':
    fh = FileHandler()
    fh.save_exchange('HUF', 'USD', 120)
