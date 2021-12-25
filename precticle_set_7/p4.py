"""#4 Write a python program to create a function that
returns smallest value from the given text file"""


def smallvaluecalc(txt):
    txt = [int(i) for i in txt[0].split()]
    return min(txt)


file = open("p7_4.txt", "r")
txt = file.readlines()
print("small value of the list are : ", smallvaluecalc(txt))
file.close()
