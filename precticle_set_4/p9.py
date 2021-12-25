# 9 write a python program to second smallest number in list
num=int(input("Enter the number of list"))
li=[]
for i in range(0,num):
        element=int(input("Enter the number"))
        li.append(element)
        li.sort(reverse=True)

        print(f"Second smallest number is upon the list is {li[1]}")