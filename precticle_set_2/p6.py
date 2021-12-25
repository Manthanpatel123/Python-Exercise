# 6 write a program to calculate the salary of an employee based on following conditions
degree = str(input("Enter your degree"))
year = int(input("Enter your experience of year in our job"))
if degree == "BE" and year < 5:
    print("SALARY IS 30000")
elif degree == "BE" and year >= 5:
    print("SALARY IS 40000")
elif degree == "ME" and year < 5:
    print("SALARY IS 50000")
elif degree == "ME" and year >= 5:
    print("SALARY IS 60000")
else:
    print("Please enter valid details")
