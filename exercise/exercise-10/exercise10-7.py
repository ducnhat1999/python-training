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

t = [5, 2, 3, 4, 5]
a = [1, 2, 3, 4, 5]
print(has_duplicates(t))
print(has_duplicates(a))