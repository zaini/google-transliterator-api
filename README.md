[![Build Status](https://travis-ci.com/AliMZaini/google-transliterator-api.svg?token=DBtzE6aVUQsPLsj6qBSd&branch=master)](https://travis-ci.com/AliMZaini/google-transliterator-api)

# google-transliterator-api

An API wrapper for https://www.google.com/inputtools/try/

The Transliterator class takes a string (in English), target language and a maximum number of candidates and updates it's list of candidates to the target language transliterations provided by Google Input Tools

Providing a string with multiple words will return candidate strings.

# Usage

```python
t = Transliterator("shlonak ya sadeeqi", "arabic", 2)
print(t.candidates)

>>> ['شلونك يا صديقي', 'شلونك يا صديق']
```

The list is in order of confidence, so take t.candidates[0] for the best prediction.

If language provided is invalid, English will be used.

# Languages

(doesn't have to be capitalised)

|  Language | Language code if different  |
|---|---|
| Amharic | |
| Arabic | |
| Bengali | |
| Chinese (Hong Kong) | chinesehk |
| Chinese (Simplified, China) | chinesesimp |
| Chinese (Traditional, Taiwan) | chinesetrad |
| Greek | |
| Gujarati | |
| Hindi | |
| Kannada | |
| Malayalam | |
| Marathi | |
| Nepali | |
| Oriya | |
| Persian | |
| Punjabi | |
| Russian | |
| Sanskrit | |
| Serbian | |
| Sinhalese | |
| Tamil | |
| Telugu | |
| Thai | |
| Tigrinya | |
| Urdu | |

# Related

https://github.com/AliMZaini/yamli-api

https://www.google.com/inputtools/try/

https://www.npmjs.com/package/google-input-tool?activeTab=readme

https://www.yamli.com/
