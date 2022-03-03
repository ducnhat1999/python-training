import random

def histogram(t):
  b = dict()
  for i in range(len(t)):
    a = random.choice(t)
    if a not in b:
      b[a] = 1
    else:
      b[a] += 1
  return b
t = ['a', 'a', 'b']
print(histogram(t))