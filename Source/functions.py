import file_handler, settings as s
import converter

# Megfelelő nyelvi fájl betöltése
if(s.settings["language"] == "hungarian"):
	import languages.hungarian as l
elif(s.settings["language"] == "english"):
	import languages.english as l
else:
	# nem értelmezhető nyelvi beállítás
	import languages.hungarian as l


# A menühöz tartozó funkciók
class Functions():
    def __init__(self):
        self.c = converter.Converter()

    def exchange(self):
        print(l.lang["value"])
        value = float(input("  >> "))
        print(l.lang["base"])
        base = input("  >> ")
        print(l.lang["target"])
        target = input ("  >> ")
        print("Az eredmény: ", self.c.convert(base, target, value))
        #with open("data/exchange_rates.json") as json_file:
        #    data = json.load(json_file)

        #    text = json.dumps(data, indent=4)
        #    print(text)
        #    print("Darab: ", len(data['rates']))
            #print(data['rates']['HUF'])
            #for element in data['rates']:
            #    print(element, end="\t")
            #    print(data['rates'][element])


    def view(self):
        print("second function")

    def settings(self):
        print("third function")

    def help(self):
        print("fourth function")
