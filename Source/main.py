#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#
import menu, settings as s, functions

md = menu.MenuDrawer()
f = functions.Functions()

testMenuItems = ["Első", "Második", "Harmadik", "Negyedik", "Kilépés"]
func_list = [f.first, f.second, f.third]

def main():
	print(md.draw(testMenuItems))
	print(s.settings["language"])
	func_list[0]()


if __name__ == "__main__":
	main()
