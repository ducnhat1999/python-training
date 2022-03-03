def string_to_list(word):
  t = list(word)
  t.sort()
  t = ''.join(t)  
  return t

d= {}
fin = open('words.txt')
for line in fin:
  word = line.strip().lower()
  list1 = string_to_list(word)
  if list1 not in d:
    d[list1] = [word]
  else:
    d[list1].append(word)

t = []
for v in d.values():
  if len(v) > 1:
    t.append((len(v), v))

t.sort()
for x in t:
  print(x)
