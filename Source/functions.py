import settings as s
from file_handler import FileHandler
from error_handler import ErrorHandler
from api_handler import ApiHandler
from converter import Converter
from menu import MenuDrawer
from language_handler import LanguageHandler
from info_bar import InfoBar
from analizer import Analizer
from settings_handler import SettingsHandler

# A menühöz tartozó funkciók
class Functions:
	l = LanguageHandler.reimport_language()

	@staticmethod
	def update_language():
		Functions.l = LanguageHandler.reimport_language()
		InfoBar.update_language()

	@staticmethod
	def exchange():
		value = "unknown"
		while(ErrorHandler.valid_number(value) == False):
			print(Functions.l.lang["value"])
			value = input("  >> ")

			if(ErrorHandler.valid_number(value)):
				value = float(value)
			else:
				print(Functions.l.lang["not_a_number"])


		base = "unknown"


		if(s.settings["last_or_most"] == "mostly_used"):
			base_list = Analizer.calculate_mostly_used()[0]
			InfoBar.draw_mostly_used(base_list)
		else:
			base_list = Analizer.calculate_last_five()[0]
			InfoBar.draw_recent(base_list)

		while(ErrorHandler.valid_currency(base) == False):
			print(Functions.l.lang["base"])
			base = input("  >> ").upper()
			if(ErrorHandler.valid_currency(base) == False):
				print(Functions.l.lang["not_a_currency"])
				print(Functions.l.lang["check_currency_list"])


		target = "unknown"

		if(s.settings["last_or_most"] == "mostly_used"):
			base_list = Analizer.calculate_mostly_used()[1]
			InfoBar.draw_mostly_used(base_list)
		else:
			base_list = Analizer.calculate_last_five()[1]
			InfoBar.draw_recent(base_list)

		while(ErrorHandler.valid_currency(target) == False):
			print(Functions.l.lang["target"])
			target = input ("  >> ").upper()
			if(ErrorHandler.valid_currency(target) == False):
				print(Functions.l.lang["not_a_currency"])
				print(Functions.l.lang["check_currency_list"])


		FileHandler.save_exchange(base, target, value)

		print(Functions.l.lang["result"], Converter.convert(base, target, value))


	@staticmethod
	def print_header():
		print()
		data_set = FileHandler.read_saved_conversions()

		for header_title in next(data_set):
			if(header_title == 'date'):
				print("  " + header_title + "\t\t", end="")
			elif(header_title == 'result'):
				print(header_title + "\t", end="\n")
				print("  ------------------------------------------------------------", end="")
			else:
				print(header_title + "\t", end="")
		print()

	@staticmethod
	def view_all():
		counter = 0
		data_set = FileHandler.read_saved_conversions()
		print(Functions.l.lang["table_title"])
		Functions.print_header()
		next(data_set)
		for data in data_set:
			print("  ", end='')
			for detail in data:
				print(detail + "\t", end="")
			counter += 1
			print()
		print("\n  " + str(counter) + Functions.l.lang["all_item"])
		print()


	@staticmethod
	def view_by_date(date):
		counter = 0
		data_set = FileHandler.read_saved_conversions()
		Functions.print_header()
		for data in data_set:
			if(data[0] == date):
				print("  ", end='')
				for detail in data:
					print(detail + "\t", end="")
				counter += 1
				print()
		print("\n  " + str(counter) + Functions.l.lang["item_counter"])
		print()

	@staticmethod
	def view_by_currency(currency):
		counter = 0
		data_set = FileHandler.read_saved_conversions()
		Functions.print_header()
		for data in data_set:
			if(data[1] == currency or data[2] == currency):
				print("  ", end='')
				for detail in data:
					print(detail + "\t", end="")
				counter += 1
				print()
		print("\n  " + str(counter) + Functions.l.lang["item_counter"])
		print()

	@staticmethod
	def view():
		sub_menu = [Functions.l.lang["sub_menu_all"], Functions.l.lang["sub_menu_date"], Functions.l.lang["sub_menu_currency"]]
		sub_menu_func_list = [Functions.view_all, Functions.view_by_date, Functions.view_by_currency]

		answer = MenuDrawer.draw(sub_menu)
		if(answer == -2 or answer == -3):
			print(Functions.l.lang["press_enter"])
		elif(answer != -1):
			print(" >> " + sub_menu[answer] + " <<\n")
			if(answer == 0):
				sub_menu_func_list[answer]()
			if(answer == 1):
				print(Functions.l.lang["ask_date"])
				date = input("  >> ")
				sub_menu_func_list[answer](date)
			if(answer == 2):
				print(Functions.l.lang["ask_currency"])
				currency = input("  >> ").upper()
				sub_menu_func_list[answer](currency)

	@staticmethod
	def list():
		data_set = FileHandler.read_symbols()['symbols']
		counter = 0
		for data in data_set:
			print(data + " - " + data_set[data])

		print("\n")

	@staticmethod
	def force_update():
		ApiHandler.update_language()
		ApiHandler.refresh_data()

	@staticmethod
	def change_lang():
		language_menu = [Functions.l.lang["hungarian"], Functions.l.lang["english"]]
		print(Functions.l.lang["current_lang"] + Functions.l.lang[s.settings['language']] + "\n")
		answer = MenuDrawer.draw(language_menu)

		if(answer == 0):
			s.settings["language"] = "hungarian"
			SettingsHandler.add_setting('language', 'hungarian')
		elif(answer == 1):
			s.settings["language"] = "english"
			SettingsHandler.add_setting('language', 'english')


	@staticmethod
	def recognise():
		print("recognise option")

	@staticmethod
	def set_currency_bar():
		set_currency_menu = [Functions.l.lang["mostly_used"][:-2], Functions.l.lang["recently_used"][:-2]]

		print(Functions.l.lang["currency_bar_status"] + Functions.l.lang[s.settings['last_or_most']][:-2] + "\n")
		answer = MenuDrawer.draw(set_currency_menu)

		if(answer == 0):
			s.settings['last_or_most'] = "mostly_used"
			SettingsHandler.add_setting('last_or_most', 'mostly_used')
		elif(answer == 1):
			s.settings['last_or_most'] = "recently_used"
			SettingsHandler.add_setting('last_or_most', 'recently_used')

	@staticmethod
	def settings():
		settings_menu = [Functions.l.lang["settings_change_lang"], Functions.l.lang["settings_recognise"], Functions.l.lang["currency_bar"]]
		settings_menu_func_list = [Functions.change_lang, Functions.recognise, Functions.set_currency_bar]

		answer = MenuDrawer.draw(settings_menu)

		if(answer == -2 or answer == -3):
			print(Functions.l.lang["press_enter"])
		elif(answer != -1):
			print(" >> " + settings_menu[answer] + " <<\n")
			settings_menu_func_list[answer]()

	@staticmethod
	def help():
		print("fourth function")
