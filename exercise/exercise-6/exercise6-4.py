def is_power(a, b):
  if a == 0 or b == 0:
    return "a and b != 0"
  elif a % b == 0:
    return True
  else:
    return False

print(is_power(8, 2))