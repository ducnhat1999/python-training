from itertools import count
import string

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

def remove_punctuation(words):
  new_words = list()
  for line in words:
    for word in line:
      a = ""
      for letter in word:
        if letter not in string.punctuation:
          a += letter
      new_words.append(a)
  return new_words

def words_lower(words):
  new_words = list()
  for word in words:
    new_words.append(word.lower())
  return new_words

def count_words(words):
  count_word = dict()
  for word in words_res:
    if word in count_word:
      count_word[word] += 1
    else:
      count_word[word] = 1
  return count_word

def sort_words(words):
  words_res = list()
  list_sort = sorted((value, key) for (key,value) in words.items())
  for word in list_sort:
    if word[1] != "":
      words_res.append(word)
  return words_res    
     

fin = open('book.txt')
words = add_words(fin)
words_strip = strip_words(words)
words_result = remove_punctuation(words_strip)
words_res = words_lower(words_result)
words_count = count_words(words_res)
words_sort = sort_words(words_count)
print(words_sort[:-21:-1])

