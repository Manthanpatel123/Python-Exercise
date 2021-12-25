# 14 writea python program to print  the number of a specificed list after removing even number from it.
li=[1,2,3,4,5,6,7,8,9,10]
for x in li:
    if x%2==0:
        li.remove(x)

print(li)