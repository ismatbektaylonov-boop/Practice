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

