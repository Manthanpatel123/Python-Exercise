# 10 write a python program to find given number is palidrome or not.
num = int(input("Enter the any number"))
rev = 0
temp = num
while (temp > 0):
    b = temp % 10
    rev = (rev * 10) + b
    temp = temp // 10

if rev == num:
    print(f"{num} IS PALIDROME NUMBER")
else:
    print(f"{num} IS NOT PLAIDROME NUMBER")
