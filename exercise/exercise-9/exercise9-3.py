def avoids(word, letters):
  for letter in letters:
    if letter not in word:
      return True
    else:
      return False

count = 0
letters = input("Enter a string of forbidden: ")
fin = open('words.txt')
for line in fin:
  word = line.strip()
  result = avoids(word, letters)
  if result == True:
    count += 1

print(count)
