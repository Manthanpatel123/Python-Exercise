# 3 write a python program to check whether the given list is palidrome or not
ls=[1,2,2,1]
ls1=ls.copy()
ls1.reverse()
if ls==ls1:
    print(f"{ls} IS PALIDROME NUMBER")
else:
    print(f"{ls} NOT A PALIDROME NUMBER")