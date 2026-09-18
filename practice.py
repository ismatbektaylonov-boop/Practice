# TASK K: 

# Shunday function yozing, u string qabul qilsin va string ichidagi unli harflar sonini qaytarsin.
# MASALAN: countVowels("string") return 1;

def countVowels(str):
    lowStr = str.lower()
    count = 0
    for char in lowStr:
        if char == "a" or char == "o" or char == "e" or char == "i" or char == "u" or char == "y":
            count += 1

    return count


result = countVowels("Agentic")
print(result)

"""
Shunday class tuzing tuzing nomi Shop, va uni constructoriga 3 hil mahsulot pass bolsin,
hamda classning 3ta methodi bolsin, biri qoldiq, biri sotish va biri qabul. 
Har bir method ishga tushgan vaqt ham log qilinsin.
MASALAN: const shop = new Shop(4, 5, 2); 
shop.qoldiq() return hozir 20:40da 4ta non, 5ta lagmon va 2ta cola mavjud! shop.sotish('non', 3) & shop.qabul('cola', 4) & shop.qoldiq() 
return hozir 20:50da 1ta non, 5ta lagmon va 6ta cola mavjud!
"""

# # import datetime
# from datetime import datetime
# class Shop():

#     def __init__(self, non, cola, muzqaymoq):
#         self.non = non
#         self.cola = cola
#         self.muzqaymoq = muzqaymoq

#     def qoldiq(self):
#         now = datetime.now()
#         print(f"hozir {now.hour}:{now.minute}da, {self.non}ta non, {self.cola}ta cola, {self.muzqaymoq}ta muzqaymoq")
#     def sotish(self, name, amount):
#         if (name == 'non'):
#             if (self.non > amount):
#                 self.non -= amount
#                 print(f"{name} {self.non}ta qoldi")
#             else:
#                 print(f"{name} not enough")
#         elif (name == 'cola'):
#             if (self.cola > amount):
#                 self.cola -= amount
#                 print(f"{name} {self.cola}ta qoldi")
#             else:
#                 print(f"{name} not enough")
#         elif (name == 'muzqaymoq'):
#             if (self.muzqaymoq > amount):
#                 self.muzqaymoq -= amount
#                 print(f"{name} {self.muzqaymoq}ta qoldi")
#             else:
#                 print(f"{name} not enough")
#         else:
#             print(f"{name} not found")

#     def qabul(self, name, amount):
#         if (name == 'non'):
#             self.non += amount
#             print(f"{name} {amount}ta qushildi")
#             print(f"{name} {self.non}ta mavjud")
#         elif (name == 'cola'):
#             self.cola += amount
#             print(f"{name} {amount}ta qushildi")
#             print(f"{name} {self.cola}ta mavjud")
#         elif (name == 'muzqaymoq'):
#             self.muzqaymoq += amount
#             print(f"{name} {amount}ta qushildi")
#             print(f"{name} {self.muzqaymoq}ta mavjud")
#         else:
#             print(f"{name} not found")


# products = Shop(3, 6, 7)
# products.qoldiq()
# # products.sotish('muzqaymoq', 2)
# products.qabul('pepsi', 2)
# # products.sotish('pepsi', 2)
# # products.qabul('cola', 3)
# products.qoldiq()

# python in use:
'''
1. compiled language
php, java, c++, c#
2. interpreted language
python, js, nodejs

git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

In Python, there are built-in tools:
(1)TYPES -> int, float, str, list, dict, tuple, set, bool
(2)FUNCTIONS -> print(), len(), type(), input(), range(), sum(), min(), max(), sorted()
(3)EXCEPTIONS -> True, False, None

__dunder methods__ (__builtins__, __init__)
'''
# print(dir(__builtins__))
'''

primitive variable types:
1. string (type, tittle, upper, replace)
'''
# message = "Python: everything is an object!"
# print(message)

# result = type(message)
# print("result: ", result)

# result = message.title()
# print("result: ", result)

# result = message.upper()
# print("result: ", result)

# result = message.replace("object", "class")
# print("result: ", result)
# print(message)
'''
2. numbers (int, float)
methods and states:
'''
# import math
# from math import ceil, asin
# import array # package/module
# count = 100
# count_type = type(count)
# print("count: ", count, "count_type: ", count_type)
# print(f"count: {count}, count_type: {count_type}")

# result1 = count.bit_count() # methods
# print(f"result1: {result1}")

# result2 = count.from_number(1) # state
# print(f"result2: {result2}")

# result1 = ceil(97.7)  # CALL
# print("result1:", result1)

# print("=========array=========")
# print(type(array))
# print(type(math))
# print(type(ceil))
# print(type(asin))

'''
3. boolean (type, input, bool)
(isnumeric, )
truthy -> True, 1, -1, "1", "True", " ", [], {} ()
and falsy -> False, 0, "", None

'''

# y = input("Enter your name: ")
# print(y)
# print(type(y))
# print(y.isnumeric())
# print(bool(y))
'''

functions:
1. define vs call (indentation)
2. parameters vs arguments
3. keyword vs default arguments
'''
# def greet(name, age):
#     return f"How do you do {name} , you are {age} years old!"
#     # return True

# # call
# result = greet("Martin", 33)
# print(result)
# '''
# 4. scope
# '''
# b=7 # 3
# def calculator(a, b=5): # 2
#     c = a + b
#     print(f"the c value: {c}")
#     # return c

# # call  
# calculator(2, 3) # 1
'''
objects:
1. what is object (array, math(ceil))
2. iterable objects (for in) & RANGE (range())
(string, dict, tuple, list, range, map, filter)
'''
# object = range(1, 5)
# for letter in "MIT":
#     print(f"the letter: {letter}")
# for ele in object:
#     print(f"the element: {ele}")
'''
3. DICTIONARY (json object)
'''
# person = {"name": "Justin", "age": 25, "single": True}
# # person_obj = dict(name="Justin", age=25, single=True)
# print(f"the person: {person['age']}")
# print(f"the person_obj: {person.get('hobby','football')}")
# del person["single"]
# print(person)
'''
4. Error handling system
'''