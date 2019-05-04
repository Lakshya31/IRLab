#Made by Lakshya

import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#UDF


def Document_Preprocessing(readfile,writefile):
    f = open(readfile, "r")
    text = f.read()
    f.close()

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
        processed_file += i
        processed_file += " "
    f = open(writefile, "w+")
    f.write(processed_file)
    f.close()

    return 1

def Create_Vocabulary():
    """Creates Vocabulary"""
    
    Vocab = []
    Docs = []

    for a in new_filenames:
        f = open(a, "r")
        line = f.read()
        words = nltk.tokenize.word_tokenize(line)
        
        for i in range(len(words)):
            if words[i] not in Vocab:
                Vocab.append(words[i])
                Docs.append([[a,1]])
            elif words[i] in Vocab:
                index = Vocab.index(words[i])
                for j in range(len(Docs[index])):
                    if Docs[index][j][0] == a:
                        Docs[index][j][1] += 1
                        break
                else:
                    Docs[index].append([a,1])

    f = open("vocab.txt", "w")
    for i in range(len(Vocab)):
        temp = ""
        temp += Vocab[i]
        temp += " -> "
        for j in range(len(Docs[i])):
            temp += Docs[i][j][0]
            temp += ":"
            temp += str(Docs[i][j][1])
            temp += " , "
        temp += "\n"
        print(temp)
        f.write(temp)

#Global

old_filenames = [
        "T1.txt",
        "T2.txt",
        "T3.txt",
        "T4.txt",
        "T5.txt",
        "T6.txt",
        "T7.txt",
        "T8.txt",
        "T9.txt",
        "T10.txt"
        ]
new_filenames = [
        "T1_new.txt",
        "T2_new.txt",
        "T3_new.txt",
        "T4_new.txt",
        "T5_new.txt",
        "T6_new.txt",
        "T7_new.txt",
        "T8_new.txt",
        "T9_new.txt",
        "T10_new.txt"
        ]



#Main
for i in range(len(old_filenames)):
    Document_Preprocessing(old_filenames[i],new_filenames[i])

Create_Vocabulary()
