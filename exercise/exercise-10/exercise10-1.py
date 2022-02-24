def nested_sum(t):
  sum = 0
  for x in t:
    for n in x:
      sum += n
  return sum

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))