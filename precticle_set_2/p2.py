# 2 write a program to check whether enterred number is nagative positive or zero
num = int(input("Enter the any number"))
if num < 0:
    print(f"{num} IS NEGATIVE")
elif num > 0:
    print(f"{num} IS POSITIVE")
else:
    print(f"{num} IS ZERO")
