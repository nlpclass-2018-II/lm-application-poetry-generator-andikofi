
import nltk
import random
import collections
from collections import Counter


poem = open('_poetry_khairil_anwar.txt')
poem1 = poem.read()	

poem = open('_poetry_test.txt')
test_text = poem.read()

def unigram(a):
	jum_kata= 0
	model = collections.defaultdict(lambda: 0.01)
	for p in a:
		if(p in model):
			model[p] +=1
		else:
			model[p] =0.01
		jum_kata +=1
	for word in model:
		model[word] =model[word]/jum_kata
	return model

def perplexity(test, model):
	test = nltk.word_tokenize(test)
	perplexity = 1
	n=0
	for word in test:
		perplexity = perplexity*(1/model[word])

		n+=1
	perplexity = pow(perplexity, 1/float(n))
	return perplexity


tokens = nltk.word_tokenize(poem1)
model = unigram(poem1)
print (perplexity(test_text, model))