#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#
import menu, settings as s

testMenuItems = ["Első", "Második", "Harmadik", "Negyedik", "Kilépés"]

def main():
	testMenu = menu.MenuDrawer()
	print(testMenu.draw(testMenuItems))

	print(s.settings["kukac"])

if __name__ == "__main__":
	main()
