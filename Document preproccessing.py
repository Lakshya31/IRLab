#Made by Lakshya

import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

f = open("f1\\agora.txt","r")
text = f.read()

words = nltk.tokenize.word_tokenize(text)
for i in range(0, len(words)):
    words[i] = words[i].lower()

i = 0
while i < len(words):
    if words[i].isdigit():
        words.remove(words[i])
        i -= 1
    i += 1

i = 0
while i < len(words):
    if words[i] in string.punctuation:
        words.remove(words[i])
        i -= 1
    i += 1

for i in range(len(words)):
    words[i] = re.sub(r'\d+|\W+|_', '', words[i])

stop_words = set(stopwords.words('english'))
i = 0
while i < len(words):
    if words[i] in stop_words:
        words.remove(words[i])
        i -= 1
    i += 1

lemmatizer = WordNetLemmatizer()
lemma = []
for i in words:
    lemma.append(lemmatizer.lemmatize(i))

processed_file = ""
for i in lemma:
    processed_file+=i
    processed_file+=" "
print("\nProcessed Successfully")
