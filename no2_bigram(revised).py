import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

filter = RegexpTokenizer(r'(\w+)')

poem_khairil=open('_poetry_khairil_anwar.txt')
poem_1=poem_khairil.read()
token = filter.tokenize(poem_1.lower())

poem_sapardi=open('_poetry_sapardi_darmono.txt')
poem_2=poem_sapardi.read()
token = filter.tokenize(poem_2.lower())

tokens_1=nltk.word_tokenize(poem_1)
tokens_2=nltk.word_tokenize(poem_2)

bigram_1 = ngrams(tokens_1,2)
bigram_2 = ngrams(tokens_2,2)

print (Counter(bigram_1))
print('                  ')
print (Counter(bigram_2))


