import file_handler, settings as s, error_handler
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
		self.eh = error_handler.ErrorHandler()

	def exchange(self):
		#Hibakezelés később

		value = "unknown"
		while(self.eh.valid_number(value) == False):
			print(l.lang["value"])
			value = input("  >> ")

			if(self.eh.valid_number(value)):
				value = float(value)
			else:
				print(l.lang["not_a_number"])


		base = "unknown"
		while(self.eh.valid_currency(base) == False):
			print(l.lang["base"])
			base = input("  >> ").upper()
			if(self.eh.valid_currency(base) == False):
				print(l.lang["not_a_currency"])
				print(l.lang["check_currency_list"])


		target = "unknown"
		while(self.eh.valid_currency(target) == False):
			print(l.lang["target"])
			target = input ("  >> ").upper()
			if(self.eh.valid_currency(target) == False):
				print(l.lang["not_a_currency"])
				print(l.lang["check_currency_list"])



		fh = file_handler.FileHandler()
		fh.save_exchange(base, target, value)

		print(l.lang["result"], self.c.convert(base, target, value))


	def print_header(self):
		print()
		fh = file_handler.FileHandler()
		dataSet = fh.read_saved_conversions()

		for headerTitle in next(dataSet):
			if(headerTitle == 'date'):
				print("  " + headerTitle + "\t\t", end="")
			elif(headerTitle == 'result'):
				print(headerTitle + "\t", end="\n")
				print("  ------------------------------------------------------------", end="")
			else:
				print(headerTitle + "\t", end="")
		print()

	def view_all(self):
		counter = 0
		fh = file_handler.FileHandler()
		dataSet = fh.read_saved_conversions()
		print(l.lang["table_title"])
		self.print_header()
		next(dataSet)
		for data in dataSet:
			print("  ", end='')
			for detail in data:
				print(detail + "\t", end="")
			counter += 1
			print()
		print("\n  " + str(counter) + l.lang["all_item"])
		print()

	def view_by_date(self, date):
		counter = 0
		fh = file_handler.FileHandler()
		dataSet = fh.read_saved_conversions()
		self.print_header()
		for data in dataSet:
			if(data[0] == date):
				print("  ", end='')
				for detail in data:
					print(detail + "\t", end="")
				counter += 1
				print()
		print("\n  " + str(counter) + l.lang["item_counter"])
		print()

	def view_by_currency(self, currency):
		counter = 0
		fh = file_handler.FileHandler()
		dataSet = fh.read_saved_conversions()
		self.print_header()
		for data in dataSet:
			if(data[1] == currency or data[2] == currency):
				print("  ", end='')
				for detail in data:
					print(detail + "\t", end="")
				counter += 1
				print()
		print("\n  " + str(counter) + l.lang["item_counter"])
		print()

	def view(self):
		subMenu = [l.lang["sub_menu_all"], l.lang["sub_menu_date"], l.lang["sub_menu_currency"]]
		subMenuFuncList = [self.view_all, self.view_by_date, self.view_by_currency]

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

	def list(self):
		fh = file_handler.FileHandler()
		dataSet = fh.read_symbols()['symbols']
		counter = 0
		for data in dataSet:
			print(data + " - " + dataSet[data])

		print("\n")

	def settings(self):
		print("third function")

	def help(self):
		print("fourth function")
