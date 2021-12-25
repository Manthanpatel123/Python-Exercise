# 7 write a python program to multiply all the items in list.
num=int(input("Enter the length of the list"))
ls=[]
for i in range(0,num):
    n=int(input("Enter the number"))
    ls.append(n)
    mul=1
    for i in range(0,len(ls)):
        mul=mul*ls[i]

print(f"Multiplication of the list elemts is {mul}")