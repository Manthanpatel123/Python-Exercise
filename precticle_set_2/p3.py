# 3 write a python program to quadratic equations if roots are real
import math


def findroots(a, b, c):
    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form))

    if (dis_form > 0):
        print("Real and Diffrent roots")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif (dis_form == 0):
        print("Real And Same Roots")
        print(-b / (2 * a))

    else:
        print("Complex Roots")
        print(-b / (2 * a), "+i", sqrt_val)
        print(-b / (2 * a), "+i", sqrt_val)


a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

if a == 0:
    print("Input Correct Quadratic Equations")
else:
    findroots(a, b, c)
