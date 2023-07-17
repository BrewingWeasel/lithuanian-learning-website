import time
import spacy


SENTENCE = """Kiek vėliau dėl atakos Rusija apkaltino Ukrainą, Kremliaus atstovas Dmitrijus Peskovas tikino, kad tai „teroro aktas“, kuriam „bus duotas atsakas“.

„Jei įvertinsime ilgalaikę perspektyvą, atsakas bus pasiekti specialiosios karinės operacijos tikslus“, – aiškino D. Peskovas.

Tuo metu kariuomenės „Pietinės“ vadavietės atstovė spaudai Natalija Humeniuk į Maskvos kaltinimus atsakė, kad šis incidentas galėjo būti Maskvos provokacija, skirta nutraukti Juodosios jūros grūdų susitarimą.

„Tokių provokacijų kūrimas, apie kurias mums labai garsiai ir greitai praneša okupacinė Krymo valdžia, yra tipinis Rusijos ir okupantų valdžios problemų sprendimo būdas“, – tikino N. Humeniuk.

Ir iš tiesų pirmadienį po pietų Kremliaus atstovas D. Peskovas pranešė, kad Rusija stabdo savo dalyvavimą susitarime, o į jį grįš, „jei bus įgyvendintos sąlygos“, tiesa, jis nepatikslino, apie kokias sąlygas yra kalbama. Kiek vėliau Turkijos prezidentas Recepas Tayyipas Erdoganas tikino, kad Rusija nori išlaikyti grūdų susitarimą nepaisant priešingų Kremliaus komentarų.
Krymo tilto ataka
Krymo tilto ataka / AP nuotr.

Tuo metu Ukrainos žvalgybos atstovas Andrijus Jusovas televizijos kanalui „Suspline“ komentavo, kad žvalgyba šio incidento nekomentuos.

„Dabar visas pasaulis mato kilometrines transporto kamšatis ir tilto konstrukcijų pažeidimus. Priežasčių mes nekomentuojame. Galime tik pacituoti Ukrainos gynybos ministerijos Vyriausiosios žvalgybos valdybos vadovo Kyrylo Budanovo žodžius, kad Krymo tiltas – nereikalinga konstrukcija“, – teigė jis transliacijos metu.

Ukraina ne kartą pabrėžė, kad Kerčės tiltas – neteisėtas Rusijos statinys, o Ukrainos pareigūnai ne kartą įspėjo, kad „anksčiau ar vėliau jis susprogs“.

Įtarimus, kad tai galėjo būti ukrainiečių ataka sustiprina ir „RBK-Ukraine“ šaltiniai iš Ukrainos saugumo tarybos, kurie teigia esą sprogimai įvyko Kyjivo kariuomenės karinių jūrų pajėgų ir Ukrainos saugumo tarnybos operacijos metu.

„Tiltas buvo atakuojamas virš vandens plaukiančiais dronais. Pasiekti tiltą buvo sudėtinga, bet galiausiai pavyko tai padaryti“, – sakė šaltinis.

Ukrainos žvalgybos valdybai esą artimas „Meduza.io“ šaltinis taip pat patvirtino Ukrainos žiniasklaidos skelbiamą informaciją ir pridūrė, kad šiai atakai buvo naudojami tie patys dronai, kurie naudoti ir atakai Sevastopolyje prieš 3 mėnesius."""

start_time = time.time()
nlp = spacy.load("output/model-best")
doc = nlp(SENTENCE)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
nlp2 = spacy.load("lt_core_news_lg")
doc2 = nlp2(SENTENCE)
print("--- %s seconds ---" % (time.time() - start_time))


for (mine, spacies) in zip(doc, doc2):
    if mine.lemma_ != spacies.lemma_:
        print(mine.text)
        print(f"Mine: {mine.lemma_}")
        print(f"Spacy's: {spacies.lemma_}")
    else:
        print("good")

# print([(w.text, w.lemma_, w.morph) for w in doc])
