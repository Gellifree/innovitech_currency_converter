#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

import os
import menu, settings as s, functions

if(s.settings["language"] == "hungarian"):
	import hungarian as l
elif(s.settings["language"] == "english"):
	import english as l
else:
	print(" >> Nyelvi beállítások nem megfelelőek <<")
	import hungarian as l

md = menu.MenuDrawer()
f = functions.Functions()

def main():
	testMenuItems = ("Első", "Második", "Harmadik", "Negyedik", "Kilépés")
	func_list = [f.first, f.second, f.third, f.fourth]

	answer = 0
	while(answer != -1):
		os.system("clear")

		width = os.get_terminal_size().columns
		middleText = "Valutaátváltó\n"
		middleText = l.lang["title"] + "\n"
		print("2021 Kovács Norbert", end="")
		print(middleText.center(width-(2*len(middleText))))
		answer = md.draw(testMenuItems)

		if(answer == -2 or answer == -3):
			input(l.lang["press_enter"])
		elif(answer != -1):
			print(" >> " + testMenuItems[answer] + " <<\n")
			func_list[answer]()
			input(" >> Kész <<")
		else:
			input(l.lang["quitting"])
			os.system("clear")

	#print(s.settings["language"])

if __name__ == "__main__":
	main()
