def is_abecedarian(word):
  index = 0
  while index < len(word) - 1:
    if word[index] > word[index + 1]:
      return False
    index += 1
  return True

count = 0
fin = open('words.txt')
for line in fin:
  word = line.strip()
  if is_abecedarian(word):
    count += 1

print(count)