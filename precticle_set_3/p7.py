# 7 write a python program to print all even numbers between 1 to n except the numbers divisible by 6.
n=int(input("Enter the any number"))
for i in range(1,n):
    if(i%2==0):
        if i%6!=0:
            print(i)