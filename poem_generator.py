import nltk
import random
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

file_khairil=open('_poetry_khairil_anwar.txt')
file=file_khairil.read()
tokens=nltk.word_tokenize(file)
bigram = ngrams(tokens,2)
cfd=nltk.ConditionalFreqDist(bigram)
word = random.choice(tokens)
for i in range(10):
	print (word),
	if word in cfd:
		word = random.choice(list(cfd[word].keys()))
	else:
		break