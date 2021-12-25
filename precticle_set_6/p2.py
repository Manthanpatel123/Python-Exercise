# 2 write a python program to make sum of particular range using reduce.
import functools
list=[11,22,33,44,55]
print(list)
print(functools.reduce(lambda x,y:x+y,list))