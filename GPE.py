import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("/Users/krishnap/PycharmProjects/REUCOVID/all_paper.csv")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)