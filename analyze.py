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
        if token.morph.get("Case"):
            for i in ENDINGS[token.morph.get("Case")[0]]:
                if token.text.endswith(i):
                    final_vals.append((
                        token.text.rstrip(
                            i), i, token.lemma_, token.morph.get("Case")
                    ))
                    break
            else:
                final_vals.append(
                    ("", token.text, token.lemma_, token.morph.get("Case"))
                )
        else:
            final_vals.append(
                (token.text, "", token.lemma_, token.morph.get("Case")))
    return final_vals
