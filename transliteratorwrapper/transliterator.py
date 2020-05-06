import json
import requests

languages = {
    "amharic": "am-t-i0-und",
    "arabic": "ar-t-i0-und",
    "bengali": "bn-t-i0-und",
    "chinesehk": "yue-hant-t-i0-und",
    "chinesesimp": "zh-t-i0-pinyin",
    "chinesetrad": "zh-hant-t-i0-und",
    "farsi": "fa-t-i0-und",
    "greek": "el-t-i0-und",
    "gujrati": "gu-t-i0-und",
    "hindi": "hi-t-i0-und",
    "kannada": "kn-t-i0-und",
    "malayalam": "ml-t-i0-und",
    "marathi": "mr-t-i0-und",
    "nepali": "ne-t-i0-und",
    "oriya": "or-t-i0-und",
    "punjabi": "pu-t-i0-und",
    "russian": "ru-t-i0-und",
    "sanskrit": "sa-t-i0-und",
    "serbian": "sr-t-i0-und",
    "sinhalese": "si-t-i0-und",
    "tamil": "ta-t-i0-und",
    "telugu": "te-t-i0-und",
    "thai": "th-t-i0-und",
    "tigrinya": "ti-t-i0-und",
    "urdu": "ur-t-i0-und"
}


class Transliterator(object):
    def __init__(self, word, language, result_count):
        self.word = word
        sel_language = "en-t-i0-und"
        language = language.lower()
        if language in languages: sel_language = languages.get(language)
        self.candidates = self.transliterate(word, sel_language, result_count)

    def transliterate(self, word, language, result_count):
        path = "https://inputtools.google.com/request?text={}&itc={}&num={}".format(word, language, result_count)
        response = requests.get(path)
        html = response.content
        candidates = json.loads(html)[1][0][1]
        return candidates
