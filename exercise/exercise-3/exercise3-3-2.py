from __future__ import print_function, division

def print_twice(f):
  f()
  f()

def print_row_plus():
  print("+ - - - -", end=" ")

def print_plus():
  print("+")

def print_post():
  print("|        ", end=" ")

def print_dash():
  print("|")

def print_posts():
  print_three(print_post)
  print_dash()

def print_four(f):
  print_twice(f)
  print_twice(f)

def print_three(f):
  f()
  f()
  f()

def print_rows_plus():
  print_three(print_row_plus)
  print_plus()

def print_row():
  print_rows_plus()
  print_four(print_posts)
def print_grid():
  print_three(print_row)
  print_rows_plus()
print_grid()