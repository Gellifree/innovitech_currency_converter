#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

import os
import menu, settings as s, functions, sys

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


def main():
	mainMenu = (l.lang["menu_item_exchange"], l.lang["menu_item_view"], l.lang["menu_item_settings"], l.lang["menu_item_help"], l.lang["menu_item_quit"])
	func_list = [f.exchange, f.view, f.settings, f.help]

	answer = 0
	while(answer != -1):
		os.system("clear")

		width = os.get_terminal_size().columns
		middleText = l.lang["title"] + "\n"
		print("2021 Kovács Norbert", end="")
		print(middleText.center(width-(2*len(middleText))))
		answer = md.draw(mainMenu)

		if(answer == -2 or answer == -3):
			input(l.lang["press_enter"])
		elif(answer != -1):
			print(" >> " + mainMenu[answer] + " <<\n")
			func_list[answer]()
			input(l.lang["done"])
		else:
			input(l.lang["quitting"])
			os.system("clear")

if __name__ == "__main__":
	main()
