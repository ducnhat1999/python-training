import random

def add_words(fin):
  new_word = list()
  for line in fin:
    word = line.strip()
    if word != "":
      new_word.append(word)
  return new_word

def strip_words(words):
  words_strip = list()
  for word in words:
    a = word.strip()
    a1 = a.split(" ")
    words_strip.append(a1)
  return words_strip

def all_words(words):
  words_res = list()
  for word in words:
    for item in word:
      words_res.append(item)
  return words_res

def cumsum(t):
  return len(t)

def random_index(t):
  list_index = list()
  for i in range(100):
    index = random.randint(0, t)
    list_index.append(index)
  return list_index

def convert_words(list_index, words):
  string = ""
  for i in list_index:
    string += words[i] + " " + words[i+1] + " "
  print(string)



fin = open('book.txt')
list1 = add_words(fin)
list_strip = strip_words(list1)
words = all_words(list_strip)
count_list = cumsum(words)
list_index = random_index(count_list)
convert_words(list_index, words)
