
def sed(string1, string2, file1, file2):
  fin2 = open(file2)
  fin1 = open(file1, 'a+')
  for line in fin2:
    word = line.strip()
    if word == string1:
      fin1.write(string2)
      fin1.write("\n")
    else:
      fin1.write(word)
      fin1.write("\n")
  fin1.close()
  fin2.close()
      

sed("aasvogels", "Nhat", "words1.txt", "words.txt")
