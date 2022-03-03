import string

def add_words(fin):
  new_word = list()
  for line in fin:
    word = line.strip()
    new_word.append(word)
  return new_word

def strip_words(words):
  words_strip = list()
  for word in words:
    a = word.strip()
    a1 = ""
    for letter in a:
      if letter != " ":
        a1 += letter
    words_strip.append(a1)
  return words_strip

def remove_punctuation(words):
  new_words = list()
  for word in words:
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


fin = open('words.txt')
words = add_words(fin)
words_strip = strip_words(words)
words_result = remove_punctuation(words_strip)
words_res = words_lower(words_result)
print(words_res)