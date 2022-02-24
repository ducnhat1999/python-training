def has_no_e(word):
    if("e" in word):
      return True
    else:
      return False

fin = open('words.txt')
n = 0
n_no_e = 0
for line in fin:
  word = line.strip()
  n = n + 1
  no_e = has_no_e(word)
  if no_e == False:
    n_no_e = n_no_e + 1

percentage_no_e = (n_no_e * 100) / n
print(percentage_no_e)


  