import spacy

nlp = spacy.load("lt_core_news_lg")


def analyze(text):
    doc = nlp(text)
    return [(token.text, token.lemma_, token.morph.get("Case"))
            for token in doc]
