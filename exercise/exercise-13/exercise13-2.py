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


fin = open('book.txt')
words = add_words(fin)
words_strip = strip_words(words)
words_result = remove_punctuation(words_strip)
words_res = words_lower(words_result)
count_word = dict()
for word in words_res:
  if word in count_word:
    count_word[word] += 1
  else:
    count_word[word] = 1
print(count_word)