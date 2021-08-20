import requests
import os
import file_handler
from datetime import date
import settings as s

# Megfelelő nyelvi fájl betöltése
if(s.settings["language"] == "hungarian"):
	import languages.hungarian as l
elif(s.settings["language"] == "english"):
	import languages.english as l
else:
	# nem értelmezhető nyelvi beállítás
	import languages.hungarian as l


class ApiHandler:
    def __init__(self):
        self.fh = file_handler.FileHandler()
        self.status = "unknown"

    def check_status(self):
        today = date.today()
        file_date = self.fh.read_exchange()['date']
        if(str(today) != str(file_date)):
            self.status = l.lang["status_old"]
        else:
            self.status = l.lang["status_up_to_date"]
        return self.status

    def request_api(self):
        url = "http://api.exchangeratesapi.io/v1/latest?access_key=0f0626556ccdfcbf4b712ee1e7086914"
        response = requests.request("GET", url)
        if(response.ok):
            print(l.lang["update_succes"])
            f = open("data/exchange_rates.json", "w")
            f.write(response.text)
            f.close()
        else:
            print(l.lang["update_failed"])

    def refresh_data(self):
        if(self.check_status() == l.lang["status_old"]):
            print(l.lang["update_needed"])
            self.request_api()
        elif(self.check_status() == l.lang["status_up_to_date"]):
            print(l.lang["no_update_needed"])


if(False):
    url = "http://api.exchangeratesapi.io/v1/latest?access_key=0f0626556ccdfcbf4b712ee1e7086914"
    response = requests.request("GET", url)
    print(response.text)

    f = open("data/exchange_rates.json", "w")
    f.write(response.text)
    f.close()

if(False):
    url = "http://api.exchangeratesapi.io/v1/symbols?access_key=0f0626556ccdfcbf4b712ee1e7086914"
    response = requests.request("GET", url)
    print(response.text)

    f = open("data/symbols.json", "w")
    f.write(response.text)
    f.close()
