import spacy
from verb_endings import get_endings
from phonology_engine import PhonologyEngine
from accentuation import match_case, remove_accents
import unicodedata

pe = PhonologyEngine()

nlp = spacy.load("data/better_lithuanian_model")

with open("data/third_decl_is", "r") as f:
    THIRD_DECLENSION_IS = f.read().splitlines()

ENDINGS = {
    "Gen": ["io", "o", "os", "ės", "ies", "aus", "ens", "ers", "ių", "ų", "enų", "erų"],
    "Dat": [
        "iui",
        "ui",
        "iai",
        "ai",
        "ei",
        "eniui",
        "eriui",
        "iams",
        "ams",
        "oms",
        "ėms",
        "ims",
        "ums",
        "enims",
        "erims",
        "iems",
    ],
    "Acc": [
        "ią",
        "ą",
        "ę",
        "į",
        "as",
        "ų",
        "enį",
        "erį",
        "ius",
        "us",
        "es",
        "is",
        "enis",
        "eris",
    ],
    "Ins": [
        "iu",
        "u",
        "a",
        "e",
        "imi",
        "umi",
        "eniu",
        "erimi",
        "iais",
        "ais",
        "omis",
        "ėms",
        "ims",
        "umis",
        "enims",
        "erimis",
    ],
    "Loc": [
        "yje",
        "oje",
        "ėje",
        "uje",
        "enyje",
        "eryje",
        "ame",
        "iuose",
        "uose",
        "ose",
        "ėse",
        "yse",
        "enyse",
        "eryse",
        "e",
    ],
    "Nom": [
        "as",
        "is",
        "ys",
        "ias",
        "a",
        "ė",
        "us",
        "uo",
        "iai",
        "ai",
        "os",
        "ės",
        "ys",
        "ūs",
        "enys",
        "erys",
    ],
    "Voc": [
        "ai",
        "e",
        "i",
        "y",
        "a",
        "ė",
        "au",
        "enie",
        "erie",
        "iai",
        "ai",
        "os",
        "ės",
        "ys",
        "ūs",
        "enys",
        "erys",
    ],
    "Ill": ["on", "in", "ėn", "uosna", "ysna", "sna", "n"],
}

DECLENSION_GROUPS = {
    "as": 1,
    "ys": 1,
    "a": 2,
    "ė": 2,
    "us": 4,
    "uo": 5,
}

IS_DECLENSIONS = {
    "io": 1,
    "iu": 1,
    "iams": 1,
    "ius": 1,
    "iais": 1,
    "iai": 1,
    "iouse": 1,
    "ies": 3,
    "imi": 3,
    "ie": 3,
    "ys": 3,
    "ims": 3,
    "imis": 3,
    "yse": 3,
}

PERSONS = {
    "1": "First",
    "2": "Second",
    "3": "Third",
}

TENSES = {
    "Past": "Past",
    "Pres": "Present",
    "Fut": "Future",
}


def process_person(inp):
    if inp:
        print(inp)
        return PERSONS[inp[0]] + " person"
    else:
        return inp


def process_tense(inp):
    if inp:
        return TENSES[inp[0]]
    else:
        return inp


ALL_ENDINGS = []
for i in ENDINGS.values():
    ALL_ENDINGS += i


def analyze(text):

    # TODO: clean up
    res = pe.process(text)
    words_with_accents = []
    for word_details, phrase, normalized_phrase, letter_map in res:
        for word_detail in word_details:
            words_with_accents.append(
                word_detail["utf8_stressed_word"].lower())

    doc = nlp(text)
    final_vals = []
    for token in doc:
        if words_with_accents and token.text.lower() == remove_accents(words_with_accents[0]):
            token_text = match_case(words_with_accents[0], token.text)
            words_with_accents.pop(0)
        else:
            token_text = token.text

        def get_vals(text, ending):
            if token.pos_ == "VERB":
                verb_endings = (
                    str(get_endings(token.lemma_))
                    .lstrip("(")
                    .rstrip(")")
                    .replace("'", "")
                )
                print(token.morph, token.text)
            else:
                verb_endings = ""
            lemma = ""
            for i in pe.process(token.lemma_):
                try:
                    lemma = i[0][0]["utf8_stressed_word"].lower()
                    lemma = lemma[0].upper() + lemma[1:]
                except (TypeError, IndexError):
                    pass

            final_vals.append(
                (
                    text,
                    ending,
                    lemma,
                    token.morph.get("Case"),
                    token.morph.get("Gender"),
                    token.morph.get("Number"),
                    process_tense(token.morph.get("Tense")),
                    process_person(token.morph.get("Person")),
                    get_declension(token),
                    verb_endings,
                    token.lemma_
                )
            )

        if token.morph.get("Case"):
            for i in ENDINGS[token.morph.get("Case")[0]]:
                if remove_accents(token_text).endswith(i):
                    get_vals(
                        token_text[:-len(i)], unicodedata.normalize('NFC', token_text)[-len(i):])
                    break
            else:
                get_vals("", token_text)
        else:
            get_vals(token_text, "")
    return final_vals


def get_declension(token):
    if token.pos_ == "NOUN" or token.pos_ == "PROPN":
        for k, v in DECLENSION_GROUPS.items():
            if token.lemma_.endswith(k):
                return str(v)
        if token.lemma_.endswith("is"):
            if token.morph.get("Gender") == "Fem" or token.lemma_ in THIRD_DECLENSION_IS:
                return "3"
            for k, v in IS_DECLENSIONS.items():
                if token.lemma_.endswith(k):
                    return str(v)

    return ""
