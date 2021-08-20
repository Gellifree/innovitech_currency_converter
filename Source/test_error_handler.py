import unittest, error_handler

class TestErrorHandler(unittest.TestCase):
    def setUp(self):
        self.eh = error_handler.ErrorHandler()

    def test_exchange(self):
        self.assertTrue(self.eh.validCurrency('USD'), "Should be True")
        self.assertFalse(self.eh.validCurrency('None'), "Should be False")
        self.assertFalse(self.eh.validCurrency(''), "Should be False")
        self.assertFalse(self.eh.validCurrency('huf'), "Should be False")

    def test_validDate(self):
        self.assertTrue(self.eh.validDate('2021-08-20'), "Should be True")
        self.assertFalse(self.eh.validDate('2021.08.20'), "Should be False")
        self.assertFalse(self.eh.validDate('2021-08'), "Should be False")
        self.assertFalse(self.eh.validDate('2021'), "Should be False")
        self.assertFalse(self.eh.validDate(''), "Should be False")


if __name__ == '__main__':
    unittest.main()
