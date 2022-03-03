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

fin = open('book.txt')
fin1 = open('words.txt')
words = add_words(fin)
words1 = add_words(fin1)
words_strip = strip_words(words)
words_strip1 = strip_words(words1)
words_res = all_words(words_strip)
words_res1 = all_words(words_strip1)
print(set(words_res) - set(words_res1))