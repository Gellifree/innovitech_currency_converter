import importlib
import settings as s

class LanguageHandler:
    def __init__(self):
        self.l = ""

    def reimport_language(self):
        importlib.invalidate_caches()
        if(s.settings["language"] == "hungarian"):
            self.l = importlib.import_module("languages.hungarian")
        elif(s.settings["language"] == "english"):
            self.l = importlib.import_module("languages.english")
        else:
            # nem értelmezhető nyelvi beállítás
            self.l = importlib.import_module("languages.hungarian")
        return self.l
