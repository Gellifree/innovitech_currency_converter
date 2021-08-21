import settings as s
import csv

class SettingsHandler:
    settings = [
        ('name', 'value')
    ]
    @staticmethod
    def add_setting(name, value):
        SettingsHandler.settings.append((name, value))

    @staticmethod
    def apply_settings():
    	x = SettingsHandler.load_settings()
    	for data in x:
    		if(data[0] in s.settings):
    			s.settings[data[0]] = data[1]

    @staticmethod
    def check_settings():
        x = SettingsHandler.load_settings()
        #SettingsHandler.add_setting('language', 'english')
        print(SettingsHandler.settings)
        name_list = []
        for data in x:
            name_list.append(data[0])
        print("tulajdonságok neve: ", name_list) # Lementett adatok
        # Ha ezek nincsenek benne a beállításokban futásidőben, tegyük bele
        settings_list = []
        for setting in SettingsHandler.settings:
            settings_list.append(setting[0])
        for setting in name_list:
            if setting not in settings_list:
                print("\nNincs benne a", setting)







    @staticmethod
    def save_settings():
        csv_path = "data/settings.csv"
        with open(csv_path, 'w') as settings:
            writer = csv.writer(settings, delimiter=';')
            for setting in SettingsHandler.settings:
                writer.writerow(setting)

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

if __name__ == '__main__':
    SettingsHandler.check_settings()
