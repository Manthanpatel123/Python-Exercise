# 14 write a python program to check if all dictionries in a list are empty or not.
list=[{1},{},{}]
ans=all(not x for x in list)
if ans==True:
    print("all dictiories are empty")
else:
    print("all dictories are not empty")