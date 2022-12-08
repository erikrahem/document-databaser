import os
from tkinter import *
import tkinter
import sys
import tkinter as tk

def main():

    counter = int(e1.get())


    #path = r'G:/'
    path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)

    def read_text_file(file_path):

        file = open(file_path, "r", encoding='CP1252', errors='ignore')
        words = []

        dx = {}
        for x in range(1, counter+1):
            dx["frequency{0}".format(x)] = 0

        dy = {}
        for y in range(1, counter+1):
            dy["frequent_word{0}".format(y)] = ""

        for line in file:
            line_word = line.lower().replace(',', '').replace('.', '').replace('\n', '').split(" ");
            for w in line_word:
                if w != "":
                    words.append(w);

        eight = []
        for i in range(0, len(words)):
            count = 1
            if words[i] not in eight:
                for j in range(i + 1, len(words)):
                    if (words[i] == words[j]) and (words[i] not in eight):
                        count = count + 1;
                for k in range(1, counter+1):
                    if count >= dx["frequency" + str(k)] and words[i] not in eight:
                        for z in range(0, counter-k):
                            dx["frequency" + str(counter-z)] = dx["frequency" + str(counter-z-1)]
                            dy["frequent_word" + str(counter - z)] = dy["frequent_word" + str(counter - z - 1)]
                        dx["frequency" + str(k)] = count
                        dy["frequent_word" + str(k)] = words[i]
                        eight.append(words[i])

        myData = " "
        for m in range(1, counter+1):
            myData += str("Frequent word #" + str(m) + ": " + dy["frequent_word" + str(m)] + " (" + str(dx["frequency" + str(m)]) + "x)\n ")
    #    print(myData)

        wordsTemp = words
        myDataTemp = myData

        file.close();
        return(wordsTemp,myDataTemp)

    words = []
    myData = ""

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt") and os.path.getsize(os.path.join(root, file)) <= 1000000:
                file_path = os.path.join(root, file)
                print(file_path)
                wordsTemp, myDataTemp = read_text_file(file_path)
                myData += ((os.path.join(root, file)))
                words += wordsTemp
                myData += "\n" + myDataTemp
                myData += "\n"

    print(myData)

    dx = {}
    for x in range(1, counter+1):
        dx["frequency{0}".format(x)] = 0

    dy = {}
    for y in range(1, counter+1):
        dy["frequent_word{0}".format(y)] = ""

    eight = []
    for i in range(0, len(words)):
        count = 1
        if words[i] not in eight:
            for j in range(i + 1, len(words)):
                if (words[i] == words[j]) and (words[i] not in eight):
                    count = count + 1;
            for k in range(1, counter+1):
                if count >= dx["frequency" + str(k)] and words[i] not in eight:
                    for z in range(0, counter-k):
                        dx["frequency" + str(counter-z)] = dx["frequency" + str(counter-z-1)]
                        dy["frequent_word" + str(counter - z)] = dy["frequent_word" + str(counter - z - 1)]
                    dx["frequency" + str(k)] = count
                    dy["frequent_word" + str(k)] = words[i]
                    eight.append(words[i])

    yourData = "All files\n"
    for m in range(1, counter+1):
        yourData += ("Frequent word #" + str(m) +": " + dy["frequent_word" + str(m)] + " (" + str(dx["frequency" + str(m)]) + "x)\n")
    print(yourData)
    #loop that iterates labeling, instead of iterating printing
    return(myData, yourData)
