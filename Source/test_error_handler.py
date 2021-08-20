import unittest
import error_handler

class TestErrorHandler(unittest.TestCase):
    def setUp(self):
        self.eh = error_handler.ErrorHandler()

    def test_exchange(self):
        self.assertTrue(self.eh.valid_currency('USD'), "Should be True")
        self.assertFalse(self.eh.valid_currency('None'), "Should be False")
        self.assertFalse(self.eh.valid_currency(''), "Should be False")
        self.assertFalse(self.eh.valid_currency('huf'), "Should be False")

    def test_valid_date(self):
        self.assertTrue(self.eh.valid_date('2021-08-20'), "Should be True")
        self.assertFalse(self.eh.valid_date('2021.08.20'), "Should be False")
        self.assertFalse(self.eh.valid_date('2021-08'), "Should be False")
        self.assertFalse(self.eh.valid_date('2021'), "Should be False")
        self.assertFalse(self.eh.valid_date(''), "Should be False")


if __name__ == '__main__':
    unittest.main()
