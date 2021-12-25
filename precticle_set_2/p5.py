# 5 write a python program to find maximum of three numbrs
num1=int(input("Enter the any number"))
num2=int(input("Enter the any number"))
num3=int(input("Enter the any number"))

if num1>num2 and num1>num3:
    print(f"{num1} IS MAXIMUM")
elif num2>num3:
    print(f"{num2} IS MAXIMUM")
else:
    print(f"{num3} IS MAXIMUM")