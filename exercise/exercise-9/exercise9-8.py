def has_palindrome(str):
  str1 = str[::-1]
  if str1 == str:
    print(str1)

def convert_str(n):
  n_str = str(n) 
  has_palindrome(n_str)

n = 100000
while n <= 999999:
  convert_str(n)
  n += 1