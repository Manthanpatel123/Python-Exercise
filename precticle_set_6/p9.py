#  cretae list that store only alphabets from given list.
# (1) map/filtter and function

"""def checkalfabet(ch):
    character = str(ch)
    if character.isalpha():
        return True
    else:
        return False


def checkalfaaa(ch):
    alphalistttt = []
    for i in ch:
        i = str(i)
        if i.isalpha():
            alphalistttt.append(i)
        return alphalistttt


print("alphabet from given list using filtter", format(list(filter(checkalfaaa, [123, "d", 4, "ff", "a"]))))
print("alphabet from given list using function", format(checkalfabet([123, "d", 4, "ff", "a"])))"""

# (2) map/filtter lambda using
print("alphabet from given list using lambda",
      list(filter(lambda c: c if str(c).isalpha() else 0, [123, "d", 4, "56", "ff", "a"])))

#(3)
print("alphabet from given list using list comprension",format([c for c in[123,"d",4,"56","ff","a"]if str(c).isalpha()]))