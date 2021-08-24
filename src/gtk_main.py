#!/usr/bin/python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Kovács Norbert <mfw.kovacs.norbert@gmail.com>
#

import os
import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from currency import settings as s
from currency.menu import MenuDrawer
from currency.functions import Functions
from currency.api_handler import ApiHandler
from currency.language_handler import LanguageHandler
from currency.settings_handler import SettingsHandler


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Currency Converter")

        self.button = Gtk.Button(label="Press me", margin=15)
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("You pressed me!")


def main():
    gtk_win = MainWindow()
    gtk_win.connect("destroy", Gtk.main_quit)
    gtk_win.show_all()
    Gtk.main()

if __name__ == "__main__":
	main()
