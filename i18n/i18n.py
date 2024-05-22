import json
import os

def load_language_list(language):
    with open(f"./i18n/{language}.json", "r", encoding="utf-8") as f:
        language_list = json.load(f)
    return language_list

class I18nAuto:
    def __init__(self, language=None):  # Ignore the language argument
        self.language = "en_US"  # Force en_US
        self.language_map = load_language_list(self.language)  

    def __call__(self, key):
        return self.language_map.get(key, key)

    def print(self):
        print("Use Language:", self.language)  # Will always print "en_US"
