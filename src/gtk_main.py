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
from currency.converter import Converter


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Currency Converter")
        self.set_border_width(10)

        self.box_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 20)
        self.add(self.box_container)


        self.value_entry = Gtk.Entry()
        self.base_combobox = Gtk.ComboBoxText()
        self.base_combobox.append_text('USD')
        self.base_combobox.append_text('EUR')
        self.base_combobox.append_text('HUF')
        self.base_combobox.set_active(0)


        self.target_combobox = Gtk.ComboBoxText()
        self.target_combobox.append_text('USD')
        self.target_combobox.append_text('EUR')
        self.target_combobox.append_text('HUF')
        self.target_combobox.set_active(0)

        self.result_label = Gtk.Label(label="null")
        self.convert_button = Gtk.Button(label="Convert")
        self.convert_button.connect('clicked', self.on_button_clicked)

        self.box_container.pack_start(self.value_entry, True, True, 0)

        self.second_row_box = Gtk.Box(spacing=10)

        self.second_row_box.pack_start(self.base_combobox, True, True, 0)
        self.second_row_box.pack_start(self.result_label, True, True, 0)
        self.second_row_box.pack_start(self.target_combobox, True, True, 0)

        self.box_container.pack_start(self.second_row_box, True, True, 0)
        self.box_container.pack_start(self.convert_button, True, True, 0)

    def on_button_clicked(self, widget):
        value = float(self.value_entry.get_text())
        result = ""
        base = self.base_combobox.get_active_text()
        target = self.target_combobox.get_active_text()

        result = Converter.convert(base, target, value)
        self.result_label.set_label(str(result))



def main():
    gtk_win = MainWindow()
    gtk_win.connect("destroy", Gtk.main_quit)
    gtk_win.show_all()
    Gtk.main()

if __name__ == "__main__":
	main()
