# write a python program to find maximum from a list using reduce.
import functools
list=[12,4444,678,3,45,23444]
print(list)
print(functools.reduce(lambda x,y: x if x>y else y,list))