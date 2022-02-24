def middle(t):
  list = t[:]
  del(list[0])
  del(list[len(list)-1])
  return list

t = [1, 2, 3, 4]
print(middle(t))
print(t)