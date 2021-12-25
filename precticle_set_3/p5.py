# 5 write a program to find the revese of given numbers(Example 2564-4652)
a = 2564
rev = 0
while (a > 0):
    b = a % 10
    rev = (rev * 10) + b
    a = a // 10

print(f"Reverse number is {rev}")
