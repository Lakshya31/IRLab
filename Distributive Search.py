# Made by Lakshya

import time
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import os
from multiprocessing import Process

# Global

databases = []
Vocab = []
Vocab_Docs = []
Dict = []
Dict_Docs = []
repository_path = "Repository"
folders = ["f1", "f2", "f3"]
access = [0, 0, 0, 0, 0, 0]
filenames = []

# UDF

def Document_Preprocessing(path,readfile):
    """Reads a document, processes it, and stores it as a new file"""

    f = open(path+"\\"+readfile, "r")
    writefile = path+"_processed_"+readfile
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
    f = open(repository_path+"\\"+path+"\\"+writefile, "w+")
    f.write(processed_file)
    f.close()


def Create_Vocabulary(path):
    """Creates Vocabulary"""

    for a in filenames:
        f = open(repository_path+"\\"+path+"\\"+path+"_processed_"+a, "r")
        line = f.read()
        words = nltk.tokenize.word_tokenize(line)

        for i in range(len(words)):
            if words[i] not in Vocab:
                Vocab.append(words[i])
                Vocab_Docs.append([[path+"_"+a, 1]])
            elif words[i] in Vocab:
                index = Vocab.index(words[i])
                for j in range(len(Vocab_Docs[index])):
                    if Vocab_Docs[index][j][0] == path+"_"+a:
                        Vocab_Docs[index][j][1] += 1
                        break
                else:
                    Vocab_Docs[index].append([path+"_"+a, 1])


def Create_Dictionary(path):
    """Creates Dictionary from vocabulary using insertion sort"""

    visited = [0]*len(Vocab)
    for i in range(len(Vocab)):
        min_index = -1
        min = chr(255)
        temp = []
        for j in range(len(Vocab)):
            if Vocab[j] < min and visited[j] == 0:
                min = Vocab[j]
                min_index = j
        if min_index == -1:
            print("error")
            break
        visited[min_index] = 1
        Dict.append(Vocab[min_index])
        for k in range(len(Vocab_Docs[min_index])):
            temp.append([Vocab_Docs[min_index][k][0], Vocab_Docs[min_index][k][1]])
        Dict_Docs.append(temp)

    f = open(repository_path+"\\"+path+"\\"+"inverted_index.txt", "w")
    temp_dict = []
    for i in range(len(Dict)):
        temp_dict.append([Dict[i],Dict_Docs[i]])
    f.write(str(temp_dict))


def Indexing(path):
    """This function is responsible for indexing a memory location given by path"""

    global filenames
    filenames = os.listdir(path)
    for ind in range(len(filenames)):
        Document_Preprocessing(path, filenames[ind])
    Create_Vocabulary(path)
    Create_Dictionary(path)

def Combine_Indexes():
    """Combines Multiple indexes into one"""

    All_Dicts = []
    Dictionary = []
    Index = []
    f = [None]*len(folders)
    count = [0]*len(folders)
    check = [0]*len(folders)
    max_count = []
    for i in range(len(folders)):
        f[i] = open(repository_path + "\\" + folders[i] + "\\" + "inverted_index.txt", "r")
        All_Dicts.append(eval(f[i].read()))
        max_count.append(len(All_Dicts[i]))

    while 0 in check:

        compare = []

        for i in range(len(folders)):
            if check[i] != 1:
                compare.append(All_Dicts[i][count[i]][0])

        Min = min(compare)

        for i in range(len(folders)):
            if check[i] != 1:
                if Min == All_Dicts[i][count[i]][0]:
                    count[i] += 1
                    min_index = i
                    break

        if Min not in Dictionary:
            Dictionary.append(All_Dicts[min_index][count[min_index]-1][0])
            Index.append(All_Dicts[min_index][count[min_index]-1][1])

        else:
            for j in range(len(All_Dicts[min_index][count[min_index] - 1][1])):
                Index[Dictionary.index(Min)].append(All_Dicts[min_index][count[min_index] - 1][1][j])

        for i in range(len(folders)):
            if count[i] == max_count[i]:
                check[i] = 1

    file = open(repository_path + "\\" + "inverted_index.txt", "w")
    temp_dict = []
    for i in range(len(Dictionary)):
        temp_dict.append([Dictionary[i], Index[i]])
    file.write(str(temp_dict))


# Main

if __name__ == "__main__":

    start = time.time()

    processes = [None]*len(folders)
    for i in range(len(folders)):
        processes[i] = Process(target=Indexing, args=(folders[i],))

    for i in range(len(processes)):
        processes[i].start()

    for i in range(len(processes)):
        processes[i].join()

    Combine_Indexes()

    end = time.time()
    print("\nTotal time Taken =", (end-start)-((end-start)%0.01), "seconds")
