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

# def get_formatted_user_info(name, age):
#   output = 'Name: {name}, Age: {age}'.format(name=name, age=age)
#   return output

# print(get_formatted_user_info("Nhat", 22))

# list_a = [1, 2, 3, 0, 4]
# # print(all(list_a))
# (first, second, *rest) = list_a
# print(rest)

# import operator as op
# def apply_operator(left_operator, operator, right_operator):
#   operator_mapper = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
#   return operator_mapper[operator](left_operator, right_operator)

# print(apply_operator(5, '+', 10))

# configuration = {"severity": 123, "abc": 456, "xyz": 789}
# log_severity = configuration.get('severity', 'info')
# print(configuration)
# print(log_severity)

# a = [1, 2, 3, 5]
# b = [5, 6, 7, 8, 1]
# print(set(a)|set(b))
# print(set(a)&set(b))
# print(set(a)-set(b))
# print(set(a)^set(b))

# a = set()
# print(a)

# list_one = ['Manny', 'Moe', 'Jack']
# list_two = ['Larry', 'Moe', 'Curly']
# def has_duplicate(list_one, list_two):
#   return set(list_one) & set(list_two)

# print(has_duplicate(list_one, list_two))

# from collections import namedtuple



# Person = namedtuple("Person", "name age")
# john = Person("John", 23)
# print(john)
# info = 'Name: {name}, Age: {age}'
# print(info)

# class Blog():
#   __tablename__ = 'blog'

#   def table_name(self):
#    return self.__tablename__

#   @classmethod
#   def other_table_name(cls):
#     return cls.__tablename__

# class DerivedBlog(Blog):
#   __tablename__ = 'derived_blog'
# b = DerivedBlog()
# print(b.table_name())

# from datetime import date

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return 'Name: %s, Age: %d' % (self.name, self.age)

#   @classmethod
#   def fromBirthYear(cls, name, year):
#     return cls(name, date.today().year- year)

# john = Person("John", 23)
# print(john.fromBirthYear('John', 1990))

# def get_size(some_object):
#   try:
#     return len(some_object)
#   except TypeError:
#     if some_object in (True, False, type(None)):
#       return 1
#     else:
#       return int(some_object)
# print(get_size('hello'))
# print(get_size([1, 2, 3, 4, 5]))
# print(get_size(10.0))

# def get_size(some_object):
#   if isinstance(some_object, (list, dict, str, tuple)):
#     return len(some_object)
#   elif isinstance(some_object, (bool, type(None))):
#     return 1
#   elif isinstance(some_object, (int, float)):
#     return int(some_object)

# print(get_size('hello'))
# print(get_size([1, 2, 3, 4, 5]))
# print(get_size(10.0))

# class Foo:
#   def __init__(self):
#     self.id = 8
#     self.value = self.get_value()

#   def get_value(self):
#     pass

#   def should_destroy_earth(self):
#     return self.id == 42

# class Baz(Foo):
#   def get_value(self, some_new_parameter):
#       pass

# class Qux(Foo):
#   def __init__(self):
#     super(Qux, self).__init__()
#     self.id = 42

# q = Qux()
# # b = Baz()
# q.should_destroy_earth()
# print(q.id ==42)

# class Foo:
#   def __init__(self):
#     self.__id = 8
#     self.value = self.__get_value()

#   def get_value(self):
#     pass

#   def should_destroy_earth(self):
#     return self.__id == 42

#   def __str__(self):
#     return '%d' % __id

#   __get_value = get_value

# class Baz(Foo):
#   def get_value(self, some_new_parameter):
#     pass

# class Qux(Foo):
#   def __init__(self):
#     self.id = 42
#     super(Qux, self).__init__()

# a = Foo()
# q = Qux()
# b = Baz() # Works fine now
# print(a)
# print(q.id) 
# print(b.id)

# class Person:
#   __address = "Da nang"

#   def __init__(self, name, age):
#     self.__name = name
#     self.__age = age
#   def print_name(self):
#     print(self.__name)

# john = Person("John", 23)
# print(john.__name)
# print(john.__age)
# print(john.__address)
# john.print_name()
# tax = 3

# class Product():
#   def __init__(self, name, price):
#     self.name = name
#     self._price = price

#   @property
#   def price(self):
#     return self._price * tax

#   @price.setter
#   def price(self, new_name):
#     (name, price) = new_name.split(' ')
#     self.name = name
#     self._price = int(price)

# prd1 = Product('table', 50)
# print(prd1.name)
# print(prd1.price)
# prd1.price = "apple 40"
# print(prd1.name)
# print(prd1.price)


