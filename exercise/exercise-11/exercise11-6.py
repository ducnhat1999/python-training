from __future__ import print_function, division

from pronounce import read_dictionary

def add_words(fin):
  list = dict()
  for line in fin:
    word = line.strip()
    list[word] = word
  return list

def homephones(a, b, phonetic):
  if a not in phonetic or b not in phonetic:
    return False
  return phonetic[a] == phonetic[b]

def check_word(word, list, phonetic):
  word1 = word[1:]
  word2 = word[0]+word[2:]
  if word1 not in list:
    return False
  if not homephones(word1, word2, phonetic):
    return False
  return True

fin = open('words.txt')
list = add_words(fin)
phonetic = read_dictionary()
for word in list:
  if check_word(word, list, phonetic):
    print(word, word[1:], word[0] + word[2:])
