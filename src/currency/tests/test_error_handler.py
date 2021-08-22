import unittest
from currency.error_handler import ErrorHandler

class TestErrorHandler(unittest.TestCase):
    def setUp(self):
        pass


    def test_valid_currency(self):
        self.assertTrue(ErrorHandler.valid_currency('USD'), "Should be True")
        self.assertFalse(ErrorHandler.valid_currency('None'), "Should be False")
        self.assertFalse(ErrorHandler.valid_currency(''), "Should be False")
        self.assertFalse(ErrorHandler.valid_currency('huf'), "Should be False")
        self.assertTrue(ErrorHandler.valid_currency('huf'.upper()), "Should be True")

    def test_valid_date(self):
        self.assertTrue(ErrorHandler.valid_date('2021-08-20'), "Should be True")
        self.assertFalse(ErrorHandler.valid_date('2021.08.20'), "Should be False")
        self.assertFalse(ErrorHandler.valid_date('2021-08'), "Should be False")
        self.assertFalse(ErrorHandler.valid_date('2021'), "Should be False")
        self.assertFalse(ErrorHandler.valid_date(''), "Should be False")
        self.assertFalse(ErrorHandler.valid_date('2021-13-31'), "Should be False")

    def test_valid_number(self):
        self.assertTrue(ErrorHandler.valid_number('1'), "Should be True")
        self.assertTrue(ErrorHandler.valid_number('1.1'), "Should be True")
        self.assertTrue(ErrorHandler.valid_number('-1'), "Should be True")
        self.assertFalse(ErrorHandler.valid_number(''), "Should be False")

    def test_slice_input(self):
        self.assertEqual(ErrorHandler.slice_input('first second'), ['first', 'second'], "Should be equal")
        self.assertEqual(ErrorHandler.slice_input('first second third'), ['first', 'second', 'third'], "Should be equal")
        self.assertEqual(ErrorHandler.slice_input('first'), ['first', ''], "Second has to be empty")
        self.assertEqual(ErrorHandler.slice_input(''), ['', ''], "Both should be empty")

    def test_recognise_currency(self):
        self.assertEqual(ErrorHandler.recognise_currency('1 huf'), ['1', 'HUF'], "Should recognise")
        self.assertEqual(ErrorHandler.recognise_currency('-1 usd'), ['-1', 'USD'], "Should recognise")
        self.assertEqual(ErrorHandler.recognise_currency('-1'), ['-1', 'unknown'], "Should'nt recognise")
        self.assertEqual(ErrorHandler.recognise_currency('-1 notvalidcurrency'), ['-1', 'not_valid'], "Should recognise it is not valid")
        # Később implementáljuk a megvalósítását a szóköz nélküli felismerésnek?
        self.assertEqual(ErrorHandler.recognise_currency('1huf'), ['not_valid', 'not_valid'], "Should'nt recognise")
        self.assertEqual(ErrorHandler.recognise_currency('0 huf'), ['0', 'HUF'], "Should recognise")

    def test_valid_number_with_currency(self):
        self.assertTrue(ErrorHandler.valid_number_with_currency('1 huf'), "Should be True")
        self.assertTrue(ErrorHandler.valid_number_with_currency('-1'), "Should be True")
        self.assertFalse(ErrorHandler.valid_number_with_currency('-1 notvalidcurrency'), "Should be False")


if __name__ == '__main__':
    unittest.main()
