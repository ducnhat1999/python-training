import random
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

def all_words(words):
  words_res = list()
  for word in words:
    for item in word:
      words_res.append(item)
  return words_res

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

def analysis_words(words):
  list_words = dict()
  for i, word in enumerate(words):
    if word in list_words:
      if i+1 < len(words):
        if words[i+1] not in list_words[word]:
            list_words[word].append(words[i+1])
    else:
      if i+1 < len(words):
        list_words[word] = [words[i+1]]
  return list_words

def cumsum(t):
  return len(t)

def random_index(t):
  list_index = list()
  for i in range(100):
    index = random.randint(0, t)
    list_index.append(index)
  return list_index

def convert_words(list_index, words_analysis, words):

  string = ""

  for i in list_index:
    word = words[i]
    list_words = words_analysis[word]
    string2 = random.choice(list_words)
    string += word + " " + string2 + " "
  return string



fin = open('emma.txt')
list1 = add_words(fin)
list_strip = strip_words(list1)
# words = all_words(list_strip)
words = remove_punctuation(list_strip)
words_analysis = analysis_words(words)
count_list = cumsum(words_analysis)
list_index = random_index(count_list)
string = convert_words(list_index, words_analysis, words)
print(string)
