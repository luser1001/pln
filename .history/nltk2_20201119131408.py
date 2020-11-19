import random
import nltk
nltk.download()
from nltk import word_tokenize, sent_tokenize
from random import sample

text = """ la casa del sol donde yo vivia en torremolinos de fiesta """
words = nltk.word_tokenize(text)

print(words)
tamano=len(words)

print(tamano)
print (sample(words, k=tamano))
