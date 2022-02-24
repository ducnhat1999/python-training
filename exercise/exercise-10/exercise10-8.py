from itertools import count
from random import randint

def random_birthday(n):
  list = []
  i = 0
  while i< 23:
    list.append(randint(1, 365))
    i += 1
  return list

def has_duplicates(t):
  list = t[:]
  i = 0
  while i <= len(list)-1:
    del(list[i])
    for n in list:
      if n == t[i]:
        return True
    i += 1
    list = t[:]
  return False


students = 23
simulation = 500
count = 0
for n in range(simulation):
  list = random_birthday(students)
  if has_duplicates(list):
    count += 1

print(count)

