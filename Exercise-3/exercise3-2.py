def do_twice(f, a):
  f(a)
  f(a)
  print_twice("spam")

def print_spam(text):
  print(text)

def print_twice(bruce):
  print(bruce)
  print(bruce)

def do_four(f, b):
  f(b)
  print_twice("spam")

# do_twice(print_spam, "nhat")

do_four(print_spam, "nguyen")
do_four(print_spam, "nguyen")
do_four(print_spam, "nguyen")
do_four(print_spam, "nguyen")