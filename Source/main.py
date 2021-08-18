#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#
import menu

testMenuItems = ["Első", "Második", "Harmadik", "Negyedik", "Kilépés"]

def main():
	testMenu = menu.MenuDrawer()
	print(testMenu.draw(testMenuItems))

if __name__ == "__main__":
	main()
