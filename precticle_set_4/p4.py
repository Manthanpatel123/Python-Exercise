# 4 write a python program to store string in list and then print them.
n=int(input("Enter the number of string would you like to add"))
ls=[]
for i in range(0,n):
    str=str(input("ENTER THE STRING"))
    ls.append(str)
    print(ls)