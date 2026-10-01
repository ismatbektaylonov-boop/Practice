'''Comprehension
    (1) What is comprehension & list comp
    (2) set and dict compr
    '''

print("what is comprehension and list comprehension")
# comp acts like spread operator!
'''Comprehension general syntax:
    A) *iterable
    B) <expression> for item in iterable    
    C) <expression> for item in iterable <condition>
'''
#  list comp
numbers = [1, 2, 3, 4, 5, 6, 1, 3, 41]
# shunday yozsak ichidagi narsalarni olib referenceni yani locationni olmaydi va ikkisi ikki xil obj boladi
list_num = [*numbers]  # a version
print("list_number", list_num)
print(numbers is list_num)  # False
print(id(numbers), id(list))

print("="*10)
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]  # b version
print("list_people", list_people)

print("="*10)
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]
list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("carlist", list_cars)

print("============= Set and Dict comps============")
set_nums = {*numbers}
print("set_numbers", set_nums)

dict_people = {person[0]: person[1] for person in people}  # b version
print("dict-people", dict_people)

dict_people = {person[0]: person[1]
               for person in people if person[1] >= 20}  # c version
print("dict-people", dict_people)