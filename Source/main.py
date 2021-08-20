#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

import os
import menu
import settings as s
import functions
import sys
import api_handler
import language_handler





md = menu.MenuDrawer()
f = functions.Functions()
ah = api_handler.ApiHandler()
lh = language_handler.LanguageHandler()
l = lh.reimport_language()

def main():
	ah.refresh_data()

	answer = 0
	while(answer != -1):
		l = lh.reimport_language()
		f.update_language()
		ah.update_language()




		main_menu = (l.lang["menu_item_exchange"], l.lang["menu_item_list_currency"] ,l.lang["menu_item_view"], l.lang["force_update"], l.lang["menu_item_settings"], l.lang["menu_item_help"], l.lang["menu_item_quit"])
		func_list = [f.exchange, f.list, f.view, f.force_update, f.settings, f.help]
		os.system("clear")

		width = os.get_terminal_size().columns
		middle_text = l.lang["title"] + "\n"
		print("2021 Kovács Norbert - " + ah.status, end="")
		print(middle_text.center(width-(2*len(middle_text))))
		answer = md.draw(main_menu)

		if(answer == -2 or answer == -3):
			print(l.lang["press_enter"])
		elif(answer != -1):
			print(" >> " + main_menu[answer] + " <<\n")
			func_list[answer]()
			input(l.lang["done"])
		else:
			input(l.lang["quitting"])
			os.system("clear")

if __name__ == "__main__":
	main()
