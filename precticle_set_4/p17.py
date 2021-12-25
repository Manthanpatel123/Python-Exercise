# 17 flatten a nested list structure

def flattenlist(nestedlist):
    if not(bool(nestedlist)):
        return nestedlist
    if isinstance(nestedlist[0],list):
        return flattenlist(*nestedlist[:1]+flattenlist(nestedlist[1:]))
    return nestedlist[:1]+flattenlist(nestedlist[1:])


nestedlist=[1,[2,3,[4,5,[6,7]]]]
print(nestedlist)
print(flattenlist(nestedlist))

