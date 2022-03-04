from dbm import dumb

from simplejson import load
import pickle


def string_to_list(word):
  t = list(word)
  t.sort()
  t = ''.join(t)  
  return t

def store_anagrams(t):
  fin = open("dictionary.txt", 'w')
  for x in t:
    fin.write(pickle.dumbs(x))
    fin.write("\n")

def read_anagrams(string):
  fin = open("dictionary.txt")
  list_words = list()
  for line in fin:
    word = line.strip()
    word = pickle.loads(word)
    print(word)
    
    

d= {}
fin = open('words.txt')
for line in fin:
  word = line.strip().lower()
  list1 = string_to_list(word)
  if list1 not in d:
    d[list1] = [word]
  else:
    d[list1].append(word)

t = []
for v in d.values():
  if len(v) > 1:
    t.append((len(v), v))

t.sort()
read_anagrams("Nhat")
