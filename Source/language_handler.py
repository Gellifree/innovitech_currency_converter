import importlib
import settings as s

class LanguageHandler:
    l = ""

    @staticmethod
    def reimport_language():
        importlib.invalidate_caches()
        if(s.settings["language"] == "hungarian"):
            LanguageHandler.l = importlib.import_module("languages.hungarian")
        elif(s.settings["language"] == "english"):
            LanguageHandler.l = importlib.import_module("languages.english")
        else:
            # nem értelmezhető nyelvi beállítás
            LanguageHandler.l = importlib.import_module("languages.hungarian")
        return LanguageHandler.l
