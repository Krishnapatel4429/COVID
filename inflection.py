import spacy
import pyinflect
import nltk
from pyinflect import getAllInflections, getInflection
# nltk.download('wordnet')
from nltk.corpus import wordnet as wn

from read_csv import spread_list


def getInflections(spread_list):
    all_inflections = []
    for spread in spread_list:
        print(spread)
        for key in spread.keys():
            all_inflections.append(spread[key][0])
    return list(set(all_inflections))

spread_list = [getAllInflections('spread'), getAllInflections('transmission'), getAllInflections('widespread')]
inflections = getInflections(spread_list)
print(spread_list)
print('/n')

spread_inflection = []
transmission_inflection = []
widespread_inflection = []

print(getInflections(spread_list))
print("/n")
