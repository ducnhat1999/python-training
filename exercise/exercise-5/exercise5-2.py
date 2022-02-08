def check_fermat(a, b, c, n):
  check_params = check_number(a, b, c, n)
  if check_params == True:
    if ((a**n)+(b**n)) == c**n:
      print("Holy smokes, Fermat was wrong!")
    else:
      print("No, that doesn't work.")

def check_number(a, b, c, n):
  if a <= 0 or b <= 0 or c <= 0:
    print("a, b, c is positive intergers")
    return False
  elif n <= 2:
    print("n greater than 2")
    return False
  else: 
    return True

check_fermat(1, 1, 2, 3)