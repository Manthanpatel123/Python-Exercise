# 3 write a python program to Fibonacci series upto n items
# from typing import ValuesView
num=int(input("Enter the any number"))
x=0
y=1
if num>=1:
    if num==1:
        print(f"The Fibonacci series is {x}")
    else:
        print("The Fibonacci series is")
        print(x)
        print(y)
        for i in range(2,num):
            z=x+y
            x=y
            y=z
            print(z)
else:
    print("Plz Enter the valid number")
