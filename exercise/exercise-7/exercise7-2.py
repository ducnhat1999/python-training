def eval_loop():
  while True:
    a = input("Enter value: ")
    if a == "done":
      return b
    print(eval(a))
    b = a

print(eval_loop())