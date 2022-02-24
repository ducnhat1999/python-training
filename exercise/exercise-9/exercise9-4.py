def uses_only(word, letters):
  if word == letters:
    return True
  else:
    return False

fin = open('words.txt')
for line in fin:
  word = line.strip()
  print(uses_only(word, "zymes"))

