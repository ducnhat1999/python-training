import random

def add_words(fin):
  new_word = list()
  for line in fin:
    word = line.strip()
    if word != "":
      new_word.append(word)
  return new_word

def cumsum(t):
  return len(t)

def random_index(t):
  index = random.randint(0, t)
  return index

fin = open('words.txt')
list = add_words(fin)
count_list = cumsum(list)
index = random_index(count_list)
print(list[index])
