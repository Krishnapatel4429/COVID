import nltk
nltk.download('punkt')
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("/Users/krishnap/PycharmProjects/REUCOVID/all_paper.csv")
data = fp.read()
print('\n-----\n'.join(tokenizer.tokenize(data)))