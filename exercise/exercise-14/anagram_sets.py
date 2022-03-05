import string
import os


def string_to_list(word):
    t = list(word)
    t.sort()
    t = "".join(t)
    return t


def store_anagrams(t):
    d = {}
    fin = open(t)
    for line in fin:
        word = line.strip().lower()
        list1 = string_to_list(word)
        if list1 not in d:
            d[list1] = [word]
        else:
            d[list1].append(word)

    t1 = []
    for v in d.values():
        if len(v) > 1:
            t1.append(v)

    t1.sort()
    fin = open("dictionary.txt", "w")
    for x in t1:
        fin.write(str(x))
        fin.write("\n")


def walk(dirname, name1):
    for name in os.listdir(dirname):
        if name == name1:
            return True
    return False


def read_anagrams(string1):
    cws = os.getcwd()
    if walk(cws, "dictionary.txt"):
        fin = open("dictionary.txt")
        list_words = list()
        for line in fin:
            word2 = ""
            word = line.strip()
            for letter in word:
                if letter not in string.punctuation:
                    word2 += letter
            word1 = word2.split(" ")
            list_words.append(word1)
        for items in list_words:
            for item in items:
                if item == string1:
                    return items
        return "Word not on the list"
    else:
        return "Please run store_anagrams before run read_anagrams"
