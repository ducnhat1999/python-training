def cumsum(t):
  sum = 0
  i = 0
  list = []
  while i <= len(t)-1:
    list.append(t[i]+sum)
    sum += t[i]
    i += 1
  return list