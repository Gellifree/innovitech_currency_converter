import requests, os

class ApiHandler:
    def checkStatus():
        pass


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
