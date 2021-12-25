# 9 write a python program to check whether given number is armstrong or not .
num = int(input("Enter the any number"))
sum = 0
temp = num
while (temp > 0):
    b = num % 10
    sum = sum + b ** 3
    temp = temp // 10
if num == sum:
    print(f"{num} is armstrong number")
else:
    print(f"{num} not a armstrong number")
