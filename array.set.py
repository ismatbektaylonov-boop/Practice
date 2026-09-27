'''Array & Set
    (1) Array
    (2) Set
    (3) Specific operators with set
    '''

from array import array
#  i >> int, f >> float >>> arraylarni faqat int va floatdan yasasak boladi pastda "i" >> int,
# pythonda array strict data type hisoblanadi
numbs_set = array("i", [1, 2, 3, 4, 5, 41])
print(numbs_set)

numbs_set.append(100)
numbs_set.insert(0, 14)
print(numbs_set, "=======")

numbs_set.remove(5)
numbs_set.pop()
print(numbs_set, "=======")

del numbs_set[0:2]
print(numbs_set, "=======")

new_numbers = array("i", [1, 4,  5,  7, 8, 41])
numbs_set = set(new_numbers)


print(f" the numbs set: {numbs_set} and type: {type(numbs_set)}")


# SET ni ozini Method lari bor ekan.


# add(). bu oxiridan value qoshib berar ekan
numbs_set.add(200)
print("numbs_set(1)", numbs_set)

numbs_set.add(7)
print("numbs_set(2)", numbs_set)


print("========== Specific Operators with set. |,&,-,^")

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union
# union degani har 2-ikkala toplamdagi qiymatlarni bir
# set ga toplab berar ekan.va albatta 2-marta takrorlangan qiymatlarni takrorlamas ekan. va natija {50, 20, 40, 10}
print("result1:", result1)

result2 = a & b  # intersection
# intersection degani "a" ning va "b" ning ichida mujassam bolgan degani.
# yani "a" va "b" ni ichida takrorlangan sonni korsat degan mantiqni bajaradi. va natija {20}
print("result2:", result2)

result3 = a - b  # deferance
# "a" va b da bolgan qiymatlar olib tashlanadi va "b" ni qoymati otmaydi. va natija: {10, 50}
print("result3:", result3)

result4 = a ^ b  # symetric deference
# symetrix deference bu dgani, bir birda qatnashgan qiymatlarni olib tashlayi, yani 20-ma chuni 2-marta qatnashgan
# va qatnashmagan qiymatlarni olib beradi. yani {40, 10, 50}

print("result4:", result4)