def has_duplicate(t):
  list = dict()
  for n in t:
    if n in list:
      return True
    list[n] = True
  return False

t = [1,2,2,4,5]
print(has_duplicate(t))