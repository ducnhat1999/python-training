def build_lists(fin):
  lists = []
  for line in fin:
    word = line.strip()
    lists.append(word)
  return lists

fin = open('words.txt')
lists = build_lists(fin)
for item in lists:
  a = item[::2]
  b = item[1::2]
  print(item, a, b)