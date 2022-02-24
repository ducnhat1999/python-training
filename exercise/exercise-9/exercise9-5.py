def uses_all(word, letters):
  count = 0
  for letter in letters:
    if letter in word:
      count += 1
  if count == len(word):
    return True
  return False

count = 0
string = "aeiou"
fin = open('words.txt')
for line in fin:
  word = line.strip()
  if uses_all(word, string):
    count += 1

print(count)