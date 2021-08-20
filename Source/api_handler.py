import requests
import os
from  file_handler import FileHandler
from datetime import date
import settings as s
from language_handler import LanguageHandler


class ApiHandler:
	l = LanguageHandler.reimport_language()
	status = l.lang["status_old"]

	@staticmethod
	def update_language():
		ApiHandler.l = LanguageHandler.reimport_language()
		ApiHandler.check_status()


	@staticmethod
	def check_status():
		today = date.today()
		file_date = FileHandler.read_exchange()['date']
		if(str(today) != str(file_date)):
			ApiHandler.status = ApiHandler.l.lang["status_old"]
		else:
			ApiHandler.status = ApiHandler.l.lang["status_up_to_date"]
		return ApiHandler.status


	@staticmethod
	def request_api():
		url = "http://api.exchangeratesapi.io/v1/latest?access_key=0f0626556ccdfcbf4b712ee1e7086914"
		response = requests.request("GET", url)
		if(response.ok):
			print(ApiHandler.l.lang["update_succes"])
			f = open("data/exchange_rates.json", "w")
			f.write(response.text)
			f.close()
			ApiHandler.status = ApiHandler.l.lang["status_up_to_date"]
		else:
			print(ApiHandler.l.lang["update_failed"])


	@staticmethod
	def refresh_data():
		if(ApiHandler.check_status() == ApiHandler.l.lang["status_old"]):
			print(ApiHandler.l.lang["update_needed"])
			ApiHandler.request_api()
		elif(ApiHandler.check_status() == ApiHandler.l.lang["status_up_to_date"]):
			print(ApiHandler.l.lang["no_update_needed"])


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
