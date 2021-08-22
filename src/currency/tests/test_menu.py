import unittest
from currency.menu import MenuDrawer
import sys
from io import StringIO

class TestMenu(unittest.TestCase):
    def setUp(self):
        pass

    def test_menu_draw(self):
        sys.stdout = StringIO("")
        list = ['menu 1', 'menu 2']

        sys.stdin = StringIO("-1")
        answer = MenuDrawer.draw(list)
        self.assertEqual(answer, -2, "Should be -2")

        sys.stdin = StringIO(" ")
        answer = MenuDrawer.draw(list)
        self.assertEqual(answer, -3, "Should be -3")

        sys.stdin = StringIO("0")
        answer = MenuDrawer.draw(list)
        self.assertEqual(answer, 0, "Should be 0")

        sys.stdin = StringIO("99")
        answer = MenuDrawer.draw(list)
        self.assertEqual(answer, -2, "Should be -2")

        sys.stdin = StringIO("unknown")
        answer = MenuDrawer.draw(list)
        self.assertEqual(answer, -3, "Should be -3")

        sys.stdin = StringIO("Q")
        answer = MenuDrawer.draw(list)
        self.assertEqual(answer, -1, "Should be -1")

        sys.stdout = sys.__stdout__
