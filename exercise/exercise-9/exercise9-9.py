def convert_str(text):
  return str(text)

def check_diffs(daughter_str, mother_str):
  if daughter_str[::-1] == mother_str:
    print("daughter", "mother")
    print(daughter_str, mother_str)


daughter = 0
mother = 18
while mother < 100:
  daughter_str = convert_str(daughter).zfill(2)
  mother_str = convert_str(mother)
  check_diffs(daughter_str, mother_str)
  daughter +=1 
  mother +=1