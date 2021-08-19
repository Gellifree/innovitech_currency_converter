import unittest, error_handler

class TestErrorHandler(unittest.TestCase):
    def test_validCurrencyUSD(self):
        self.eh = error_handler.ErrorHandler()
        self.assertTrue(self.eh.validCurrency('USD'), "Should be True")

    def test_validCurrencyNone(self):
        self.eh = error_handler.ErrorHandler()
        self.assertFalse(self.eh.validCurrency('None'), "Should be False")

    def test_emptyCurrency(self):
        self.eh = error_handler.ErrorHandler()
        self.assertFalse(self.eh.validCurrency(''), "Should be False")

    def test_validCurrencyLowerCase(self):
        self.eh = error_handler.ErrorHandler()
        self.assertTrue(self.eh.validCurrency('huf'), "Should be True")


if __name__ == '__main__':
    unittest.main()
