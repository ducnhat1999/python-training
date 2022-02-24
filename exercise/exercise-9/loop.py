def is_reverse(word1, word2):
  i = 0
  j = len(word2) - 1
  while j>=0:
    if word1[i] != word2[j]:
      return False
    i += 1
    j -= 1
  return True

def is_palindrome(word):
  return is_reverse(word, word)

fin = open('words.txt')
for line in fin:
  word = line.strip()
  print(is_palindrome(word))
