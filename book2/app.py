# def for_console_output(func):
#   def wrapper(*args, **kwargs):
#     print('--------------------------------')
#     print(str(func(*args, **kwargs)))
#     print('--------------------------------')
#   return wrapper
# @for_console_output
# def add(x, y):
#   return x + y
# add(3, 2)

# name = 23
# age = "nhat"

# (name, age) = (age, name)
# print(name)
# print(age)

# book_info = ' The Three Musketeers: Alexandre Dumas'
# formatted_book_info = book_info.strip().upper().replace(':', ' by')
# print(formatted_book_info)

# result_list = ["Nguyen", "Van", "Duc", "Nhat"]
# result_string = ' '.join(result_list)
# print(result_string)

# name = "Nhat"
# age = 121
# for letter in name:
#   print(ord(letter))
# print(chr(age))

# user = {"authors": "nhat", "name": "nguyen"}
# print(user["name"])

def get_formatted_user_info(name, age):
  output = 'Name: {name}, Age: {age}'.format(name=name, age=age)
  return output

print(get_formatted_user_info("Nhat", 22))
