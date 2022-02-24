def uses_only(word, available):
  for letter in word:
    if letter not in available:
      return False
  return True

def uses_all(word, required):
  return uses_only(required, word)

fin = open('words.txt')
for line in fin:
  word = line.strip()
  print(uses_all(word, "zymosis"))