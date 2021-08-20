import file_handler
import settings as s
import error_handler
import api_handler
import converter
import menu
import language_handler


# A menühöz tartozó funkciók
class Functions():
	def __init__(self):
		self.c = converter.Converter()
		self.md = menu.MenuDrawer()
		self.eh = error_handler.ErrorHandler()
		self.fh = file_handler.FileHandler()
		self.ah = api_handler.ApiHandler()
		self.lh = language_handler.LanguageHandler()
		self.l = self.lh.reimport_language()

	def update_language(self):
		self.l = self.lh.reimport_language()

	def exchange(self):
		#Hibakezelés később

		value = "unknown"
		while(self.eh.valid_number(value) == False):
			print(self.l.lang["value"])
			value = input("  >> ")

			if(self.eh.valid_number(value)):
				value = float(value)
			else:
				print(self.l.lang["not_a_number"])


		base = "unknown"
		while(self.eh.valid_currency(base) == False):
			print(self.l.lang["base"])
			base = input("  >> ").upper()
			if(self.eh.valid_currency(base) == False):
				print(self.l.lang["not_a_currency"])
				print(self.l.lang["check_currency_list"])


		target = "unknown"
		while(self.eh.valid_currency(target) == False):
			print(self.l.lang["target"])
			target = input ("  >> ").upper()
			if(self.eh.valid_currency(target) == False):
				print(self.l.lang["not_a_currency"])
				print(self.l.lang["check_currency_list"])


		self.fh.save_exchange(base, target, value)

		print(self.l.lang["result"], self.c.convert(base, target, value))

	def print_header(self):
		print()
		data_set = self.fh.read_saved_conversions()

		for header_title in next(data_set):
			if(header_title == 'date'):
				print("  " + header_title + "\t\t", end="")
			elif(header_title == 'result'):
				print(header_title + "\t", end="\n")
				print("  ------------------------------------------------------------", end="")
			else:
				print(header_title + "\t", end="")
		print()

	def view_all(self):
		counter = 0
		data_set = self.fh.read_saved_conversions()
		print(self.l.lang["table_title"])
		self.print_header()
		next(data_set)
		for data in data_set:
			print("  ", end='')
			for detail in data:
				print(detail + "\t", end="")
			counter += 1
			print()
		print("\n  " + str(counter) + self.l.lang["all_item"])
		print()

	def view_by_date(self, date):
		counter = 0
		data_set = self.fh.read_saved_conversions()
		self.print_header()
		for data in data_set:
			if(data[0] == date):
				print("  ", end='')
				for detail in data:
					print(detail + "\t", end="")
				counter += 1
				print()
		print("\n  " + str(counter) + self.l.lang["item_counter"])
		print()

	def view_by_currency(self, currency):
		counter = 0
		data_set = self.fh.read_saved_conversions()
		self.print_header()
		for data in data_set:
			if(data[1] == currency or data[2] == currency):
				print("  ", end='')
				for detail in data:
					print(detail + "\t", end="")
				counter += 1
				print()
		print("\n  " + str(counter) + self.l.lang["item_counter"])
		print()

	def view(self):
		sub_menu = [self.l.lang["sub_menu_all"], self.l.lang["sub_menu_date"], self.l.lang["sub_menu_currency"]]
		sub_menu_func_list = [self.view_all, self.view_by_date, self.view_by_currency]

		answer = self.md.draw(sub_menu)
		if(answer == -2 or answer == -3):
			print(self.l.lang["press_enter"])
		elif(answer != -1):
			print(" >> " + sub_menu[answer] + " <<\n")
			if(answer == 0):
				sub_menu_func_list[answer]()
			if(answer == 1):
				print(self.l.lang["ask_date"])
				date = input("  >> ")
				sub_menu_func_list[answer](date)
			if(answer == 2):
				print(self.l.lang["ask_currency"])
				currency = input("  >> ").upper()
				sub_menu_func_list[answer](currency)

	def list(self):
		data_set = self.fh.read_symbols()['symbols']
		counter = 0
		for data in data_set:
			print(data + " - " + data_set[data])

		print("\n")

	def force_update(self):
		self.ah.update_language()
		self.ah.refresh_data()

	def change_lang(self):
		language_menu = [self.l.lang["hungarian"], self.l.lang["english"]]
		print(self.l.lang["current_lang"] + self.l.lang[s.settings['language']] + "\n")
		answer = self.md.draw(language_menu)

		if(answer == 0):
			s.settings["language"] = "hungarian"
		elif(answer == 1):
			s.settings["language"] = "english"



	def recognise(self):
		print("recognise option")

	def settings(self):
		settings_menu = [self.l.lang["settings_change_lang"], self.l.lang["settings_recognise"]]
		settings_menu_func_list = [self.change_lang, self.recognise]

		answer = self.md.draw(settings_menu)

		if(answer == -2 or answer == -3):
			print(self.l.lang["press_enter"])
		elif(answer != -1):
			print(">> " + settings_menu[answer] + " <<\n")
			settings_menu_func_list[answer]()

	def help(self):
		print("fourth function")
