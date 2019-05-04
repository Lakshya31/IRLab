from nltk.corpus import stopwords
words = ["a", 'a', "an", "the"]
stop_words = set(stopwords.words('english'))
i=0
while i < len(words):
    if words[i] in stop_words:
        words.remove(words[i])
        i -= 1
    i += 1
print(words)
