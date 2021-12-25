# 8 create a  list that store only positive numbers from given list
# (1) map/filter and function
def pos(c):
    if c>0:
        return True
    else:
        return False
def posn(c):
    list=[]
    for i in c:
        if i>0:
            list.append(i)
            return list

print("positive number from given list using filter",format(list(filter(pos,[20,-10,-25,78,6,0,777]))))
print("positive number from given list using function",format(posn([20,-10,-25,78,6,0,777])))

# (2) map/filtter and lambda
print("positive number from given list using lambda",format(list(filter(lambda x:x>0,[20,-10,-25,78,6,0,777]))))

# (3) list comprension
print("positive number from given list using list comprension",format([x for x in [20,-10,-25,78,6,0,777] if x>0]))
