def is_sorted(t):
  i = 0
  while i < len(t)-1:
    if t[i] > t[i+1]:
      return False
    i += 1
  return True
t = [1,2,3]
a = ["b", "a"]
print(is_sorted(t))
print(is_sorted(a))