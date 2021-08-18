#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

import os
import menu, settings as s, functions

md = menu.MenuDrawer()
f = functions.Functions()

def main():
	testMenuItems = ["Első", "Második", "Harmadik", "Negyedik", "Kilépés"]
	func_list = [f.first, f.second, f.third, f.fourth]

	answer = 0
	while(answer != -1):
		os.system("clear")

		width = os.get_terminal_size().columns
		middleText = "Valutaátváltó\n"
		print("2021 Kovács Norbert", end="")
		print(middleText.center(width-len(middleText)))
		answer = md.draw(testMenuItems)

		if(answer == -2 or answer == -3):
			input("  >> Nyomj entert a viszatéréshez! <<")
		elif(answer != -1):
			print(" >> " + testMenuItems[answer] + " <<\n")
			func_list[answer]()
			input(" >> Kész <<")
		else:
			input(" >> A program most kilép <<")
			os.system("clear")

	#print(md.draw(testMenuItems))
	#print(s.settings["language"])
	#func_list[0]()

if __name__ == "__main__":
	main()
