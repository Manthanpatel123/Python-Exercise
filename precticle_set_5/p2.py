""" 2 create  two sets of integers and find their diffrence , intersection , union and symmetric diffrence
also find subset and superset  from these two, apply methods as well as operators
for all operations """

a={0,2,4,6,8}
b={1,2,3,4,5,6}

print(f"Union {a|b}")
print(f"intersection {a&b}")
print(f"diffrence {a-b}")
print(f"symmetric diffrence {a^b}")
print(f"issubset {a.issubset(b)}")
print(f"issuperset {a.issuperset(b)}")
print(a<=b)
print(a>=b)