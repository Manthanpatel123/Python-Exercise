# 8 write a python program to get the largest number from a list
num=int(input("Enter the length of the list"))
ls=[]
for i in range(0,num):
    n=int(input("Enter the number"))
    ls.append(n)
    ls.sort(reverse=True)
print(f"Largest number is in the list{ls[0]}")
