import unittest
from currency.settings_handler import SettingsHandler

class TestSettingsHandler(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        del SettingsHandler.settings['test_setting']

    def test_add_setting(self):
        SettingsHandler.add_setting('test_setting', 'value')
        self.assertTrue('test_setting' in SettingsHandler.settings, 'test_settings has to be in the settings dictionary')

        SettingsHandler.add_setting('test_setting', 'different_value')
        self.assertEqual('different_value', SettingsHandler.settings['test_setting'], 'Should change the value to different_value')
