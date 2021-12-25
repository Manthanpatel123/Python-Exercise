# 13 write a python function that takes two lists and return true if they have at least one common number
def fun(l1, l2):
    result = False
    for x in l1:
        for y in l2:
            if x == y:
                result = True
                return result

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
print(fun(l1, l2))
