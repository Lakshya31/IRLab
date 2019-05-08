import os
from shutil import copyfile
import time

path = "C:\\Users\\Lakshya Sharma\\Downloads\\Sample"
copypath = "C:\\Users\\Lakshya Sharma\\PycharmProjects\\InfoRetrieval\\"
folders = ["f1", "f2", "f3"]


def reader():
    filenames = os.listdir(path)
    try:
        for i in range(len(filenames)):
            f = open(path+"\\"+filenames[i], "r")
            string = f.read()
            print(string[0])
            f.close()
        print(i, len(filenames))
    except:
        f.close()
        os.remove(path+"\\"+filenames[i])
        if i+1 != len(filenames):
            print("Recalling:")
            reader()
        else:
            print("Yaee")


def copier():
    filenames = os.listdir(path)

    for i in range(300,7500,12):
        copyfile(path+"\\"+filenames[i], copypath+folders[(i//12)%3]+"\\"+filenames[i])
    print("Copied")

start = time.time()
#reader()
copier()
end = time.time()
print("Done in", end-start, "seconds")
