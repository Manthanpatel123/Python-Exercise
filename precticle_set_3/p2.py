# 2 write a python program to find sum of N scannned numbers
n=int(input("Enter the any number"))
num=0
for i in range(0,n):
    element=int(input())
    num=element+num
    print(num)