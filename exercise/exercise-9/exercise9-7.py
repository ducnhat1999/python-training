from itertools import count


def three_consecutive_double_letter(word):
  count = 0
  i = 0
  j = 1
  while j <= len(word)-1:
    if word[i] != word[j]:
      i += 1
      j += 1
      count = 0
    else:
      i += 2
      j += 2
      count += 1
      if count == 3:
        print(word)

fin = open('words.txt')
for line in fin:
  word = line.strip()
  three_consecutive_double_letter(word)
