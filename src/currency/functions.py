import os
from currency.file_handler import FileHandler
from currency.error_handler import ErrorHandler
from currency.converter import Converter
from currency.info_bar import InfoBar
from currency.analizer import Analizer
from currency import settings as s
from currency.menu import MenuDrawer
from currency.api_handler import ApiHandler
from currency.language_handler import LanguageHandler
from currency.settings_handler import SettingsHandler

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
		result = []
		base_list = []
		target_list = []

		while(ErrorHandler.valid_number_with_currency(value) == False):
			print(Functions.l.lang["value"])
			value = input("  >> ")

			if(ErrorHandler.valid_number_with_currency(value)):
				result = ErrorHandler.recognise_currency(value)
				value = float(ErrorHandler.recognise_currency(value)[0])
			else:
				print(Functions.l.lang["bad_input"])

		base = "unknown"

		if(result[1] == "unknown"):
			if(s.settings["show_last_or_most"] == 'on'):
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
		else:
			base = result[1]

		target = "unknown"

		if(s.settings["show_last_or_most"] == 'on'):
			if(s.settings["last_or_most"] == "mostly_used"):
				target_list = Analizer.calculate_mostly_used()[1]
				InfoBar.draw_mostly_used(target_list)
			else:
				target_list = Analizer.calculate_last_five()[1]
				InfoBar.draw_recent(target_list)

		if(s.settings["list_multiple"] == 'on'):
			convert_results = Converter.convert_from_list(base, target_list, value)
			InfoBar.draw_results(convert_results)

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
		result = "\n"
		data_set = FileHandler.read_saved_conversions()

		for header_title in next(data_set):
			if(header_title == 'date'):
				result += "  " + header_title + "\t\t"
			elif(header_title == 'result'):
				result += header_title + "\t\n"
				result+= "  -------------------------------------------------"
			else:
				result += header_title + "\t"
		result += "\n"
		return result

	@staticmethod
	def view_all():
		counter = 0
		data_set = FileHandler.read_saved_conversions()
		header = Functions.print_header()
		next(data_set)
		buffer = ""
		for data in data_set:
			buffer += "  "
			for detail in data:
				buffer += detail + "\t"
			counter += 1
			buffer += "\n"
		if(counter > 0):
			print(Functions.l.lang["table_title"])
			print(header + buffer)
		print("  " + str(counter) + Functions.l.lang["all_item"])

	@staticmethod
	def view_by_date(date):
		counter = 0
		data_set = FileHandler.read_saved_conversions()
		header = Functions.print_header()
		buffer = ""
		for data in data_set:
			if(data[0] == date):
				buffer += "  "
				for detail in data:
					buffer += detail + "\t"
				counter += 1
				buffer += "\n"
		if(counter > 0):
			print(header + buffer)
		print("\n  " + str(counter) + Functions.l.lang["item_counter"])

	@staticmethod
	def view_by_currency(currency):
		counter = 0
		data_set = FileHandler.read_saved_conversions()
		header = Functions.print_header()
		buffer = ""
		for data in data_set:
			if(data[1] == currency or data[2] == currency):
				buffer += "  "
				for detail in data:
					buffer += detail + "\t"
				counter += 1
				buffer += "\n"
		if(counter > 0):
			print(header + buffer)
		print("\n  " + str(counter) + Functions.l.lang["item_counter"])

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
				date = "unknown"
				while(ErrorHandler.valid_date(date) == False):
					date = input("  >> ")
					if(ErrorHandler.valid_date(date) == False):
						print(Functions.l.lang["not_a_date"])
				sub_menu_func_list[answer](date)
			if(answer == 2):
				print(Functions.l.lang["ask_currency"])
				currency = "unkown"
				while(ErrorHandler.valid_currency(currency) == False):
					currency = input("  >> ").upper()
					if(ErrorHandler.valid_currency(currency) == False):
						print(Functions.l.lang["not_a_currency"])
						print(Functions.l.lang["check_currency_list"])
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
	def function_on_off():
		turn_on_off_menu = [Functions.l.lang["result_list"], Functions.l.lang["list_last_or_most"]]
		answer = MenuDrawer.draw(turn_on_off_menu)
		on_off_menu = [Functions.l.lang["on"], Functions.l.lang["off"]]
		print()

		if(answer == 0):
			print("   Jelenlegi állapot: " + Functions.l.lang[s.settings['list_multiple']] + "\n")

			sub_answer = MenuDrawer.draw(on_off_menu)
			if(sub_answer == 0):
				SettingsHandler.add_setting('list_multiple', 'on')
			elif(sub_answer == 1):
				SettingsHandler.add_setting('list_multiple', 'off')
		if(answer == 1):
			print("   Jelenlegi állapot: " + Functions.l.lang[s.settings['show_last_or_most']] + "\n")

			sub_answer = MenuDrawer.draw(on_off_menu)
			if(sub_answer == 0):
				SettingsHandler.add_setting('show_last_or_most', 'on')
			elif(sub_answer == 1):
				SettingsHandler.add_setting('show_last_or_most', 'off')
		SettingsHandler.save_settings()
		SettingsHandler.apply_settings()

	@staticmethod
	def set_currency_bar():
		set_currency_menu = [Functions.l.lang["mostly_used"][:-2], Functions.l.lang["recently_used"][:-2]]

		if(s.settings["show_last_or_most"] == 'off'):
			print(Functions.l.lang["function_turned_off"])

		print(Functions.l.lang["currency_bar_status"] + Functions.l.lang[s.settings['last_or_most']][:-2] + "\n")

		answer = MenuDrawer.draw(set_currency_menu)

		if(answer == 0):
			s.settings['last_or_most'] = "mostly_used"
			SettingsHandler.add_setting('last_or_most', 'mostly_used')
		elif(answer == 1):
			s.settings['last_or_most'] = "recently_used"
			SettingsHandler.add_setting('last_or_most', 'recently_used')

	@staticmethod
	def clear_history():
		print(Functions.l.lang["delete_confirmation"])
		answer = input("  >> ")
		if(answer == "Y" or answer == "y" or answer == "I" or answer == "i" or answer == ""):
			FileHandler.delete_history()
			print(Functions.l.lang["cleared_history"])
		else:
			print(Functions.l.lang["cancelled"])

	@staticmethod
	def watch_settings():
		for setting in s.settings:
			print("  " + setting + ":   \t" + s.settings[setting])
		print()

	def update_symbols():
		ApiHandler.request_api_symbols()

	@staticmethod
	def settings():
		settings_menu = [Functions.l.lang["settings_change_lang"], Functions.l.lang["settings_func_on_off"], Functions.l.lang["currency_bar"], Functions.l.lang["clear_history"],Functions.l.lang["update_symbols"] , Functions.l.lang["watch_settings"]]
		settings_menu_func_list = [Functions.change_lang, Functions.function_on_off, Functions.set_currency_bar, Functions.clear_history, Functions.update_symbols, Functions.watch_settings]

		answer = MenuDrawer.draw(settings_menu)

		if(answer == -2 or answer == -3):
			print(Functions.l.lang["press_enter"])
		elif(answer != -1):
			print(" >> " + settings_menu[answer] + " <<\n")
			settings_menu_func_list[answer]()

	@staticmethod
	def help():
		if(s.settings["language"] == "english"):
			os.system("cat currency/help_files/help_english")
		elif(s.settings["language"] == "hungarian"):
			os.system("cat currency/help_files/help_hungarian")
