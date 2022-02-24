def cumsum_lists(t):
  sum = 0
  i = 0
  j = 0
  list = []
  while i <= len(t)-1:
    list1 = []
    while j <= len(t[i]) -1:
      list1.append(t[i][j] + sum)
      sum += t[i][j]
      j += 1
    list.append(list1)
    list1 = []
    j = 0
    i += 1
  return list

def cumsum(t):
  sum = 0
  i = 0
  list = []
  while i <= len(t)-1:
    list.append(t[i]+sum)
    sum += t[i]
    i += 1
  return list

t = [[1, 2], [3], [4, 5, 6]]
a = [1, 2, 3]
print(cumsum_lists(t))
print(cumsum(a))