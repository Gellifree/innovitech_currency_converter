import settings as s
import csv

class SettingsHandler:
    settings = {
        'name': 'value'
    }


    @staticmethod
    def add_setting(name, value):
        SettingsHandler.settings[name] = value

    @staticmethod
    def apply_settings():
        x = SettingsHandler.load_settings()
        for data in x:
            if(data[0] in s.settings):
                s.settings[data[0]] = data[1]

    @staticmethod
    def check_settings():
        x = SettingsHandler.load_settings()

        key_list = []
        data_dictionary = {}
        for data in x:
            data_dictionary[data[0]] = data[1]
            key_list.append(data[0])

        for key in key_list:
            if(key not in SettingsHandler.settings.keys()):
                SettingsHandler.settings[key] = data_dictionary[key]



    @staticmethod
    def save_settings():
        SettingsHandler.check_settings()
        csv_path = "data/settings.csv"
        with open(csv_path, 'w') as settings:
            writer = csv.writer(settings, delimiter=';')
            for setting in SettingsHandler.settings:
                writer.writerow([setting, SettingsHandler.settings[setting]])

    @staticmethod
    def load_settings():
        csv_path = "data/settings.csv"
        with open(csv_path) as settings:
            reader = csv.reader(settings)
            data_list = []
            data = ''
            for row in reader:
                for i in row[0]:
                    if(i != ';'):
                        data += i
                    if(i == ';'):
                        data_list.append(data)
                        data = ''
                data_list.append(data)
                data = ''
                yield data_list
                data_list = []
