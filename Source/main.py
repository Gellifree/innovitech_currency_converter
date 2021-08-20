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

# Megfelelő nyelvi fájl betöltése
if(s.settings["language"] == "hungarian"):
	import languages.hungarian as l
elif(s.settings["language"] == "english"):
	import languages.english as l
else:
	# nem értelmezhető nyelvi beállítás
	import languages.hungarian as l

md = menu.MenuDrawer()
f = functions.Functions()
ah = api_handler.ApiHandler()


def main():
	ah.refresh_data()

	main_menu = (l.lang["menu_item_exchange"], l.lang["menu_item_list_currency"] ,l.lang["menu_item_view"], l.lang["menu_item_settings"], l.lang["menu_item_help"], l.lang["menu_item_quit"])
	func_list = [f.exchange, f.list, f.view, f.settings, f.help]

	answer = 0
	while(answer != -1):
		os.system("clear")

		width = os.get_terminal_size().columns
		middle_text = l.lang["title"] + "\n"
		print("2021 Kovács Norbert - " + ah.status, end="")
		print(middle_text.center(width-(2*len(middle_text))))
		answer = md.draw(main_menu)

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
