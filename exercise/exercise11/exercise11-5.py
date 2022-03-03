def add_words(fin):
  list = dict()
  for line in fin:
    word = line.strip()
    list[word] = 1
  return list

def rotate_word(word, n):
  res = ''
  for letter in word:
    if letter.isupper():
      start = ord('A')
    elif letter.islower():
      start = ord('a')
    else:
      return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    res += chr(i)
  return res
    

fin = open('words.txt')
list = add_words(fin)
newlist = dict()
for word in list:
  newlist[rotate_word(word, 3)] = 1
print(newlist)
  