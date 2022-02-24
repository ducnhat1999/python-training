def first(word):
  return word[0]

def last(word):
  return word[-1]

def middle(word):
  return word[1: -1]

print("first", first(""))
print("last", last(""))
print("middle", middle(""))