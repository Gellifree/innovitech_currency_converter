import json, os

class FileHandler():
    def read_exchange(self):
        with open("data/exchange_rates.json") as json_file:
            return json.load(json_file)

    def read_symbols(self):
        with open("data/symbols.json") as json_file:
            return json.load(json_file)
