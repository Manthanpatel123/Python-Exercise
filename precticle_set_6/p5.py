# 5 write a python program to apply two functions (square and cube) simulataneosuly on aspecific range using map
def squareclac(num):
    return (num*num)
def cubeclac(num):
    return (num*num*num)
li1=map(squareclac,[10,20,30])
li2=map(cubeclac,[10,20,30])
print(list(li1))
print(list(li2))