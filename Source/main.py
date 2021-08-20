#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

import os
import sys
import settings as s
from menu import MenuDrawer
from functions import Functions
from api_handler import ApiHandler
from language_handler import LanguageHandler


l = LanguageHandler.reimport_language()

def main():
	ApiHandler.refresh_data()

	answer = 0
	while(answer != -1):

		MenuDrawer.update_language()
		Functions.update_language()
		ApiHandler.update_language()
		l = LanguageHandler.reimport_language()



		main_menu = (l.lang["menu_item_exchange"], l.lang["menu_item_list_currency"] ,l.lang["menu_item_view"], l.lang["force_update"], l.lang["menu_item_settings"], l.lang["menu_item_help"], l.lang["menu_item_quit"])
		func_list = [Functions.exchange, Functions.list, Functions.view, Functions.force_update, Functions.settings, Functions.help]
		os.system("clear")

		width = os.get_terminal_size().columns
		middle_text = l.lang["title"] + "\n"
		print("2021 Kovács Norbert - " + ApiHandler.status, end="")
		print(middle_text.center(width-(2*len(middle_text))))
		answer = MenuDrawer.draw(main_menu)

		if(answer == -2 or answer == -3):
			input(l.lang["press_enter"])
		elif(answer != -1):
			print(" >> " + main_menu[answer] + " <<\n")
			func_list[answer]()
			input(l.lang["done"])
		else:
			input(l.lang["quitting"])
			os.system("clear")

if __name__ == "__main__":
	main()
