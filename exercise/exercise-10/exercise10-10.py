def build_lists(fin):
  lists = []
  for line in fin:
    word = line.strip()
    lists.append(word)
  return lists

def sort_lists(lists):
  return sorted(lists)

def in_bisect(lists, string):
  if string in lists:
    return lists.index(string)

fin = open('words.txt')
lists = build_lists(fin)
lists = sort_lists(lists)
a = ["quahog", "gagag", "spalling", "iwahsgas"]
for item in a:
  print(in_bisect(lists, item))

