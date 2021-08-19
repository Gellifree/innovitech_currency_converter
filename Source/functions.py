import file_handler, settings as s
import converter, menu

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
		self.md = menu.MenuDrawer()

	def exchange(self):
		#Hibakezelés később
		print(l.lang["value"])
		value = float(input("  >> "))
		print(l.lang["base"])
		base = input("  >> ").upper()
		print(l.lang["target"])
		target = input ("  >> ").upper()

		fh = file_handler.FileHandler()
		fh.saveExchange(base, target, value)

		print("Az eredmény: ", self.c.convert(base, target, value))


	def printHeader(self):
		print()
		fh = file_handler.FileHandler()
		dataSet = fh.readSavedConversions()

		for headerTitle in next(dataSet):
			if(headerTitle == 'date'):
				print(headerTitle + "\t\t", end="")
			elif(headerTitle == 'result'):
				print(headerTitle + "\t", end="\n")
				print("------------------------------------------------------------", end="")
			else:
				print(headerTitle + "\t", end="")
		print()

	def viewAll(self):
		fh = file_handler.FileHandler()
		dataSet = fh.readSavedConversions()
		print(l.lang["table_title"])
		self.printHeader()
		next(dataSet)
		for data in dataSet:
			for detail in data:
				print(detail + "\t", end="")
			print()
		print()

	def viewByDate(self, date):
		fh = file_handler.FileHandler()
		dataSet = fh.readSavedConversions()
		self.printHeader()
		for data in dataSet:
			if(data[0] == date):
				for detail in data:
					print(detail + "\t", end="")
				print()
		print()

	def viewByCurrency(self, currency):
		fh = file_handler.FileHandler()
		dataSet = fh.readSavedConversions()
		self.printHeader()
		for data in dataSet:
			if(data[1] == currency or data[2] == currency):
				for detail in data:
					print(detail + "\t", end="")
				print()
		print()

	def view(self):
		subMenu = [l.lang["sub_menu_all"], l.lang["sub_menu_date"], l.lang["sub_menu_currency"]]
		subMenuFuncList = [self.viewAll, self.viewByDate, self.viewByCurrency]

		answer = self.md.draw(subMenu)
		if(answer == -2 or answer == -3):
			input(l.lang["press_enter"])
		elif(answer != -1):
			print(" >> " + subMenu[answer] + " <<\n")
			if(answer == 0):
				subMenuFuncList[answer]()
			if(answer == 1):
				print(l.lang["ask_date"])
				date = input("  >> ")
				subMenuFuncList[answer](date)
			if(answer == 2):
				print(l.lang["ask_currency"])
				currency = input("  >> ").upper()
				subMenuFuncList[answer](currency)


	def settings(self):
		print("third function")

	def help(self):
		print("fourth function")
