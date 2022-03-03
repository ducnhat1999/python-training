def build_lists(fin):
  lists = []
  for line in fin:
    word = line.strip()
    lists.append(word)
  return lists

def build_lists1(fin):
  lists = []
  for line in fin:
    word = line.strip()
    lists = lists + [word]
  return lists

fin = open('words.txt')
print(build_lists1(fin))
