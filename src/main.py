#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

import os
import sys

from currency import settings as s
from currency.menu import MenuDrawer
from currency.functions import Functions
from currency.api_handler import ApiHandler
from currency.language_handler import LanguageHandler
from currency.settings_handler import SettingsHandler

def main():
	ApiHandler.refresh_data()
	SettingsHandler.apply_settings()
	l = LanguageHandler.reimport_language()
	answer = 0
	while(answer != -1):
		MenuDrawer.update_language()
		Functions.update_language()
		ApiHandler.update_language()
		l = LanguageHandler.reimport_language()

		main_menu = (l.lang["menu_item_exchange"], l.lang["menu_item_list_currency"] ,l.lang["menu_item_view"], l.lang["menu_item_settings"], l.lang["menu_item_help"], l.lang["menu_item_quit"])
		func_list = [Functions.exchange, Functions.list, Functions.view, Functions.settings, Functions.help]
		os.system("clear")

		width = os.get_terminal_size().columns
		middle_text = l.lang["title"] + "\n"
		print("2021 Kovács Norbert - " + ApiHandler.status, end="")
		print(middle_text.center(width-(4*len(middle_text))))
		answer = MenuDrawer.draw(main_menu)

		if(answer == -2 or answer == -3):
			input(l.lang["press_enter"])
		elif(answer != -1):
			print(" >> " + main_menu[answer] + " <<\n")
			func_list[answer]()
			input(l.lang["done"])
		else:
			SettingsHandler.save_settings()
			input(l.lang["quitting"])
			os.system("clear")

if __name__ == "__main__":
	main()
