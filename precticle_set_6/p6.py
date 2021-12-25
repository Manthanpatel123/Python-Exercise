""" 6 write python program using
(1) map/filter and functions
(2) map/filter and lambda functions
(3) list comprehesion."""


# 1
def ncube(n):
    return n ** 3




def numcube(nlist):
    cubelist = []
    for i in nlist:
        cubelist.append(i ** 3)
        return cubelist


print("cube of given list using map :", format(list(filter(ncube, range(1, 5)))))
# 2

def ncube(n):
    return n ** 3

print("cube of a given list using lambda", format(list(filter(lambda x: x ** 3, range(1, 5)))))

# 3
print("cube of a given list using string compresions", format([i ** 3 for i in range(1, 5)]))
