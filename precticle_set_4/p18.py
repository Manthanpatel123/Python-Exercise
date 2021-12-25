# 18 write a python program to split a list every Nth element.
c=['a','b','c','d','e','f','g','h','i','j','k','l']
def list_slice(s,step):
    return [s[i::step] for i in range(step)]
print(list_slice(c,3))