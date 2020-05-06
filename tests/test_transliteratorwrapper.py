from gtransliteratewrapper import Transliterator


def test_transliterator():
    transliteration = Transliterator("shlonak ya sadeeqi", "arabic", 3)
    words = transliteration.candidates

    assert words[0] == "شلونك يا صديقي", "Incorrect response from call for 'shlonak ya sadeeqi'. Google's API may be down."
