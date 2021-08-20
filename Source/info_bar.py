from language_handler import LanguageHandler

class InfoBar:
    l = LanguageHandler.reimport_language()

    @staticmethod
    def update_language():
    	InfoBar.l = LanguageHandler.reimport_language()

    @staticmethod
    def draw(data_list):
        if(len(data_list) == 0):
            print(InfoBar.l.lang["no_recent_found"])
        else:
            print("\n ", InfoBar.l.lang["mostly_used"], end="")
            for data in data_list:
                print(" [" + data + "] ", end="")
            print()
