# 3 write a python program to find n!
num = int(input("Enter the any number"))
fact = 1
for i in range(1, num + 1):
    fact = fact * i

print(fact)
