# 1 create a set of integers as follow.

# initilize the set
s = {15, 25, 35, 45, 55}

# initilize the empty set and add the value
sets =set()
sets.add(51)
sets.add(52)
sets.add(53)
sets.add(54)
sets.add(55)
print(sets)

# from a list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(set(list1))

# from another set
s1 = set([22, 33, 44])
s2 = set()
s2.update(s1)
print(s2)

# using for loop
s = set()
for i in range(5):
    s.add(i)
print(s)

# update and existing set using set
s1 = {11, 22, 33, 44, 55}
s2 = {66, 77, 88, 99, 00}
s1.update(s2)
print(s1)

# print the elements of the set interctivily
s1 = {90, 89, 78, 67, 56, 45, 34, 23, 12}
for i in s1:
    print(i, end="")

# chechk the functionality of remove and discard.
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
s1.remove(2, )
print(s1)
s1.discard(7)
print(s1)
