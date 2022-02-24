def is_anagram(string1, string2):
  str1 = sorted(string1)
  str2 = sorted(string2)
  if(str1 == str2):
    return True
  else:
    return False
print(is_anagram("stop", "pots"))
print(is_anagram("stop", "pwos"))