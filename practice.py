'''TASK S:

Shunday function yozing, u numberlardan tashkil topgan array qabul qilsin va osha numberlar orasidagi tushib qolgan sonni topib uni return qilsin
MASALAN: missingNumber([3, 0, 1]) return 2'''

def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


print(missingNumber([4, 0, 1, 2]))  # 3

# TASK K: 

# Shunday function yozing, u string qabul qilsin va string ichidagi unli harflar sonini qaytarsin.
# MASALAN: countVowels("string") return 1;

# def countVowels(str):
#     lowStr = str.lower()
#     count = 0
#     for char in lowStr:
#         if char == "a" or char == "o" or char == "e" or char == "i" or char == "u" or char == "y":
#             count += 1

#     return count


# result = countVowels("Agentic")
# print(result)

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
# class Student:
# 	# constructor
# 	def init(self, name, age, gpa):
# 		self.__name = name
# 		self.__age = age
# 		self.__gpa = gpa

# 	# method
# 	def get_info(self):
# 		print(f"Name: {self.__name} \n Age: {self.__age} \n GPA: {self.__gpa}")

# 	# getter for name

# 	@property
# 	def name(self):
# 		return f"Name: {self.__name} \n GPA: {self.__gpa}"

# 	# setter for name
# 	@name.setter
# 	def name(self, new_name):
# 		if new_name == "":
# 			print("Name cannot be empty")
# 		else:
# 			self.__name = new_name


# student = Student("Jam", 20, 3.7)

# student.get_info()

# print("_____")

# print("Student name:", student.name)

# print("_____")

# from array import array

# # 1. Dastlabki ma'lumotlar
# group_a_array = array("i", [101, 102, 103, 104, 105])
# group_b_set = {103, 104, 106, 107}

# # --- 1-qadam: Array ustida amallar ---
# group_a_array.append(99)        # Oxiriga 99 qo'shish
# group_a_array.insert(0, 10)      # Boshiga 10 qo'shish
# del group_a_array[0:2]           # Birinchi 2 ta elementni o'chirish

# print("O'zgartirilgan Array:", group_a_array)

# # --- 2-qadam: Array-ni Set-ga o'girish ---
# group_a_set = set(group_a_array)
# print("Set ga o'tkazilgan Group A:", group_a_set)

# # --- 3-qadam: Specific Operators (| , & , - , ^) ---

# # Barcha xodimlar ID si (Union)
# all_employees = group_a_set | group_b_set
# print("Barcha noyob ID lar (|):", all_employees)

# # Ikkala guruhda ham bor xodimlar (Intersection)
# common_employees = group_a_set & group_b_set
# print("Ikkala guruhda ham bor ID lar (&):", common_employees)

# # Faqat Group A da bor ID lar (Difference)
# only_group_a = group_a_set - group_b_set
# print("Faqat Group A dagi ID lar (-):", only_group_a)

# # Faqat bitta guruhda bor ID lar (Symmetric Difference)
# unique_to_each = group_a_set ^ group_b_set
# print("Bir vaqtda ikkala guruhda bo'lmagan ID lar (^):", unique_to_each)

# from array import array

# # ==========================================
# # 1. ADVANCED ARRAY & SET PRACTICE
# # ==========================================

# # Ikkita har xil ma'lumotlar to'plami
# array1 = array("i", [1, 2, 3, 4, 5, 6])
# array2 = array("i", [4, 5, 6, 7, 8, 9])

# # Array amallari
# array1.append(10)
# array1.insert(0, 0)
# del array1[0:2]  # Boshidagi 2 ta elementni o'chirish

# # Set ga o'tkazish va operatorlar bilan ishlash
# set1 = set(array1)
# set2 = set(array2)

# print("--- Set Operatorlari ---")
# print("Barchasi (Union |):", set1 | set2)
# print("Umumiylari (Intersection &):", set1 & set2)
# print("Faqat 1-to'plamdagilar (Difference -):", set1 - set2)
# print("Takrorlanmaganlar (Symmetric Difference ^):", set1 ^ set2)


# # ==========================================
# # 2. DICTIONARY & OBJECT TRANSFORMATIONS
# # ==========================================

# # Dict -> Nested Array o'g'irish va Filtrlash
# def filter_and_convert(data_dict, min_value):
#     # Faqat qiymati min_value dan katta bo'lganlarini [key, value] ko'rinishida qaytaradi
#     return [[key, val] for key, val in data_dict.items() if isinstance(val, (int, float)) and val >= min_value]

# sample_dict = {"apple": 50, "banana": 20, "orange": 100, "is_fresh": True}
# print("\n--- Dict Transformation ---")
# print("Filtered Array:", filter_and_convert(sample_dict, 30))


# # ==========================================
# # 3. STRING EXPRESSIONS & DYNAMIC CALCULATION
# # ==========================================

# # Massiv ichidagi matematik ifodalarni hisoblash
# def evaluate_list(expressions):
#     results = {}
#     for idx, expr in enumerate(expressions):
#         try:
#             results[f"calc_{idx + 1}"] = eval(expr)
#         except Exception as e:
#             results[f"calc_{idx + 1}"] = f"Error: {e}"
#     return results

# expr_list = ["10 + 20 * 2", "100 - 45", "50 / 2"]
# print("\n--- Expression Evaluation ---")
# print("Calculated Dict:", evaluate_list(expr_list))