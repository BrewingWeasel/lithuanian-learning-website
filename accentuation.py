import unicodedata

accented = 'ãúàáąìíĩũỹýòõóẽéèñù'
unaccented = 'auaaąiiiuyyoooeeenu'

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ą', 'č', 'ę', 'ė', 'į', 'š', 'ų', 'ū', 'ž', ',', ' ', '\n']

replace_dict = {
    'ė́': 'ė',
    'l̃': 'l',
    'õ': 'o',
    'ỹ': 'y',
    'ė̃': 'ė',
    'r̃': 'r',
    'm̃': 'm',
    'ū̃': 'ū',
    'ū́': 'ū',
    'ą̃': 'ą',
    'ù': 'u',
    'ę́': 'e',
    'į̃': 'į',
    "į́": "į",
    'ę̃': 'ę',
    'ų́': 'ų',
    "ų̃": 'ų',
    'ą́': 'ą'
}


def remove_accents(word):
    word = unicodedata.normalize('NFC', word)
    trans = word.maketrans(accented, unaccented)
    new_text = word.translate(trans)
    for i, o in replace_dict.items():
        new_text = new_text.replace(i, o)
    return new_text


def match_case(orig_word, match_word):
    new_word = ""
    for (orig, match) in zip(unicodedata.normalize('NFC', orig_word), match_word):
        if match.isupper():
            new_word += orig.upper()
        else:
            new_word += orig.lower()
    return new_word
