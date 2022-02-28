def build_lists(fin):
  lists = []
  for line in fin:
    word = line.strip()
    lists.append(word)
  return lists

def revert(word):
  return word[::-1]

fin = open('words.txt')
lists = build_lists(fin)
i = 0
for word in lists:
  word_revert = revert(word)
  if word_revert in lists:
    print(word, word_revert)