from typing import List, Any

import spacy
import pyinflect
import nltk
nltk.download("wordnet")
from pyinflect import getAllInflections, getInflection
# nltk.download('wordnet')
from nltk.corpus import wordnet as wn
#from nltk.corpus import wordnet

spread_list = ["spread", "widespread", "transmission"]
all_inflections =[]


def get_all_inflections(spread_list):
    for word in spread_list:
        inflections = getAllInflections(word)
        print(f'{word} and its inflections; {inflections}')
        if not inflections.keys():
            all_inflections.append(word)

        for key in inflections.keys():
            all_inflections.append(inflections[key][0])
    return list(set(all_inflections))

    print(get_all_inflections(spread_list))

    #synonyms for temperature

def getSynonyms(words):
    synonymList1 = []
    for temperature_list in words:
        wordnetSynset1 = wn.synsets(temperature_list)
        temperature_list = []
        for synset1 in wordnetSynset1:
            for synwords in synset1.lemma_names():

                if synwords not in temperature_list:
                    temperature_list.append(synwords)
        synonymList1.append(temperature_list)
    return synonymList1

temperature_list = ["cold", "hot", "warm", "weather"]
humidity_list = ["humid", "humidity", 'precipitation']
latitude_list = ["equator", "southern hemisphere", "northern hemisphere"]

print(getSynonyms(temperature_list))
print(getSynonyms(humidity_list))
print(getSynonyms(latitude_list))

