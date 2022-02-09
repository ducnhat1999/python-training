def input_number():
  a = input("Input a: ")
  b = input("Input b: ")
  c = input("Input c: ")
  is_triangle(int(a), int(b), int(c))

def is_triangle(a, b, c):
  if a > b + c or b > c + a or c > a + b:
    print("No")
  else:
    print("Yes")

input_number()