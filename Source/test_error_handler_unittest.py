import unittest, error_handler

class TestErrorHandler(unittest.TestCase):
    def test_validCurrency(self):
        self.eh = error_handler.ErrorHandler()
        self.assertTrue(self.eh.validCurrency('USD'), "Should be True")


if __name__ == '__main__':
    unittest.main()
