import spacy
from verb_endings import get_endings
from phonology_engine import PhonologyEngine
from accentuation import match_case, remove_accents
import unicodedata

pe = PhonologyEngine()

nlp = spacy.load("data/better_lithuanian_model")


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
    "Ill": ["on", "in", "ėn", "uosna", "ysna", "sna", "n"],
}

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
            # print(text, ending)
            if token.pos_ == "VERB":
                verb_endings = (
                    str(get_endings(token.lemma_))
                    .lstrip("(")
                    .rstrip(")")
                    .replace("'", "")
                )
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
                    verb_endings,
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

