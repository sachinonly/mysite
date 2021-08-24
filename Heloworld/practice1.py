# Part 1
# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean
# print(mean([2, 2, 2]))

# Part 2
# def mean(keyvalue):
#     if type(keyvalue) == dict:
#         the_mean = sum(keyvalue.values()) / len(keyvalue)
#     else:
#         the_mean = sum(keyvalue) / len(keyvalue)
#     return the_mean
# mylist = {"Hyderabad": 10, "Chennai": 30, "Pune" :20}
# print (mean(mylist))

# Part 3
# def warmorcold(temperature):
#     if temperature > 7:
#         return "Warm"
#     else
#         return "Cold"
#
# user_input = int(input("Enter Temperature"))
# print(warmorcold(user_input))

# Part 4
# import winsound
# import datetime
# now = datetime.datetime.now()
# while True:
#     user_input = input("Enter username")
#     if user_input == "Go":
#         print(now.minute)
#         continue
#     else:
#         winsound.Beep(500, 1000)
#         break

# Part 5 - Multi User Inputs and then concatenating them and also search text in user input and take action
# def sentensemaker(phrase):
#     capitalized = phrase.capitalize()
#     searchstring = ("How", "What" , "Why" , "When")
#     if phrase.startswith(searchstring):
#         return "{}?.".format(capitalized)
#     else:
#         return "{}".format(capitalized)
#
# sentence = []
# while True:
#     user_input = input("Say something:")
#     if user_input =="\end":
#         break
#     else:
#         sentence.append(sentensemaker(user_input))
#         continue
# print(" ".join(sentence))

# Part 6
# Divide the number s by 10 to get the Float values as list
# #
# mynumbers = [251,310,410,420,430]
# myfloat   = []
#
# for list in mynumbers:
#     myfloat.append(list/10)
# print (myfloat)
#
# Part 7
# Divide the number s by 10 to get the Float values as list
# mynumbers = [251,310,410,420,430]
# myfloat = [ temp/10 for temp in mynumbers]
# print (myfloat)


# with open("C:\\Personals\\Learnings\\Python\\fruits.txt") as myfile:
#     content = myfile.read()
# print (content)

# with open("files/fruits.txt") as myfile:
#     content = myfile.read()
#     myfile.close()
# print(content[:12])


# inputstr = 'a2b2z4'
#
# def myconvertor(inputstr):
#     outstring =''
#     for i,item in enumerate(inputstr):
#         if  not item.isnumeric():
#             outstring += item
#         else:
#             #a = int(item)
#             #b = inputstr[i-1]
#             #print (a,b)
#             outstring += int(item) * inputstr[i-1]
#     return outstring
# print (myconvertor(inputstr))

# Working with Class and Object
#=================================#
# class human:
#     name = None
#     age = None
#
#     def get_name(self):
#         print("Enter your name")
#         self.name = input()
#
#     def put_name(self):
#         print("Your Name is: ", self.name)
#
#
# person1 = human()
# person1.get_name(), person1.put_name()

# Connecting to Snowflake from Python
# With try
import snowflake.connector


print("Script to  insert data into snowflake table from python ....")
print("Starting")
snowflake.connector.paramstyle = 'qmark'

cnn = snowflake.connector.connect(
    user='practice',
    password='Practice123#',
    account='za80685.ap-south-1.aws'
)

cs = cnn.cursor()

try:
    cs.execute('Select current_version()')
    row= cs.fetchone()
    print(row[0])
finally:
    cs.close()
cnn.close()

# Connecting to Snowflake from Python
# With If Else For loop on results

import snowflake.connector as sf
import os
import pandas

cnn = sf.connect(
    user='practice',
    password='Practice123#',
    account='za80685.ap-south-1.aws',
    warehouse='COMPUTE_WH',
    database='MYDB_PRACTICE',
    schema='MYDB_PRACTICE_SCHEMA')

print("Started ...")

query =" select current_version() "

cs = cnn.cursor()
result = cs.execute(query)
results = cs.fetchone()
#print(results[0])
#Optional Looping on Results either with above print or below if else results
if results:
    for result in results:
        print(result)
else:
    print("No word found!")