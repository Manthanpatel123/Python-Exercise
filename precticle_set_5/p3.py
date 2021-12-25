# 3 write a function called find_dups that takes a list of integers as its input argument and returns
# a set of those integers that occur two or more time in list.
list=[46,47,48,46,89,67,67,90]
s=set()
def find_dups(ls):
    for i in ls:
        ls.count(i)>1
        s.add(i)
find_dups(list)
print(s)