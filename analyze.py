import spacy

nlp = spacy.load("lt_core_news_lg")


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
}

ALL_ENDINGS = []
for i in ENDINGS.values():
    ALL_ENDINGS += i


def analyze(text):
    doc = nlp(text)
    final_vals = []
    for token in doc:
        print(token.morph.get("Gender"))

        def get_vals(text, ending):
            final_vals.append((text, ending, token.lemma_, token.morph.get(
                "Case"), token.morph.get("Gender"), token.morph.get("Number")))
        if token.morph.get("Case"):
            for i in ENDINGS[token.morph.get("Case")[0]]:
                if token.text.endswith(i):
                    get_vals(token.text.rstrip(i), i)
                    break
            else:
                get_vals("", token.text)
        else:
            get_vals(token.text, "")
    print(final_vals)
    return final_vals
