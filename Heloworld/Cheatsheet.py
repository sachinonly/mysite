#From tuple to list:
data = (1, 2, 3)
print (list(data))


# #From list to tuple:
data = [1, 2, 3]
print (tuple(data))
#
# data = [["name", "John"], ["surname", "smith"]]
# dict(data)
# #{'name': 'John', 'surname': 'smith'}
# #Note that the original data type needs to have the data structured in a way that can be understood by the new data type. For example, the following would not work:
#
# >>> data = [1, 2, 3]
# >>> dict(data)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
#
#
# Cheatsheet (Operations with Data Types)
# In this section, you learned that:
#
# Lists, strings, and tuples have a positive index system:
#
# ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# 0      1      2      3      4      5      6
# And a negative index system:
#
# ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# -7     -6     -5     -4     -3     -2     -1
# In a list, the 2nd, 3rd, and 4th items can be accessed with:
#
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# days[1:4]
# Output: ['Tue', 'Wed', 'Thu']
# First three items of a list:
#
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# days[:3]
# Output:['Mon', 'Tue', 'Wed']
# Last three items of a list:
#
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# days[-3:]
# Output: ['Fri', 'Sat', 'Sun']
# Everything but the last:
#
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# days[:-1]
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
# Everything but the last two:
#
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# days[:-2]
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# A single in a dictionary can be accessed using its key:
#
# phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
# phone_numbers["Marry Simpsons"]
# Output: '+423998200919'





# Cheatsheet (List Comprehensions)
# In this section, you learned that:
#
# A list comprehension is an expression that creates a list by iterating over another container.
#
# A basic list comprehension:
#
# [i*2 for i in [1, 5, 10]]
# Output: [2, 10, 20]
#
# List comprehension with if condition:
#
# [i*2 for i in [1, -2, 10] if i>0]
# Output: [2, 20]
#
# List comprehension with an if and else condition:
#
# [i*2 if i>0 else 0 for i in [1, -2, 10]]
# Output: [2, 0, 20]
#
# Cheatsheet (More on Functions)
# In this section, you learned that:
#
# Functions can have more than one parameter:
#
# def volume(a, b, c):
#     return a * b * c
# Functions can have default parameters (e.g. coefficient):
#
# def converter(feet, coefficient = 3.2808):
#     meters = feet / coefficient
#     return meters
#
# print(converter(10))
# Output: 3.0480370641306997
#
# Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10):
#
# def volume(a, b, c):
#     return a * b * c
#
# print(volume(1, b=2, c=10))
# An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:
#
# def find_max(*args):
#     return max(args)
# print(find_max(3, 99, 1001, 2, 8))
# Output: 1001
#
# An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:
#
# def find_winner(**kwargs):
#     return max(kwargs, key = kwargs.get)
#
# print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
# Output: Sim
#


# In this section, you learned that:
#
# You can read an existing file with Python:
#
# with open("file.txt") as file:
#     content = file.read()
# You can create a new file with Python and write some text on it:
#
# with open("file.txt", "w") as file:
#     content = file.write("Sample text")
# You can append text to an existing file without overwriting it:
#
# with open("file.txt", "a") as file:
#     content = file.write("More sample text")
# You can both append and read a file with:
#
# with open("file.txt", "a+") as file:
#     content = file.write("Even more sample text")
#     file.seek(0)
#     content = file.read()