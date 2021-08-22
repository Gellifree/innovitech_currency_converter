import requests
import os
from datetime import date
from currency.file_handler import FileHandler
from currency.language_handler import LanguageHandler
from currency import settings as s


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
			f = open("currency/data/exchange_rates.json", "w")
			f.write(response.text)
			f.close()
			ApiHandler.status = ApiHandler.l.lang["status_up_to_date"]
		else:
			f = open("currency/data/error_log", "a")
			f.write("  >>> Error while updating <<<\n")
			f.write("  Code:" + str(response.status_code) + "\n")
			f.close()
			print(ApiHandler.l.lang["update_failed"])


	@staticmethod
	def refresh_data():
		if(ApiHandler.check_status() == ApiHandler.l.lang["status_old"]):
			print(ApiHandler.l.lang["update_needed"])
			ApiHandler.request_api()
		elif(ApiHandler.check_status() == ApiHandler.l.lang["status_up_to_date"]):
			print(ApiHandler.l.lang["no_update_needed"])

if(False):
    url = "http://api.exchangeratesapi.io/v1/symbols?access_key=0f0626556ccdfcbf4b712ee1e7086914"
    response = requests.request("GET", url)
    print(response.text)

    f = open("currency/data/symbols.json", "w")
    f.write(response.text)
    f.close()
