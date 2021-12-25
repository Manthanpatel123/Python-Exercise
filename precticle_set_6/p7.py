# 7 create a list of equvivelent clesius degree from fahrenhit.
# (1) map/filter and function.

def convert_to_feranhit(c):
    return (1.8*c+32)
def calculate_feranhit(c):
    cel=[]
    for i in c:
        cel.append(1.8*i+32)
        return cel
print("conver clesius to fheranhit using map",format(list(map(convert_to_feranhit,[36.7,25.78,18.7]))))

# (2) map/filter using lambda

print("convert clesius to fheranhit using lambda",format(list(map(lambda c:1.8*c+32,[36.7,25.78,18.7]))))

# (3) list comprehension

print("convert clesius to fheranhit using list comprehension",format([1.8*c+32 for c in [36.7,25.78,18.7]]))

