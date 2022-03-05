def add_words(fin):
  list = dict()
  for line in fin:
    word = line.strip()
    list[word] = 1
  return list

fin = open('words.txt')
string = 'zoologies'
list = add_words(fin)
print(string in list)