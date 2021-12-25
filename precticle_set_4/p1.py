# 1 write a python program which covers all methods (functions)of list.
ls=["abc","def","ghi"]
#COPY list
new_ls=ls.copy()
print(new_ls)
#COUNT list
print(ls.count("abc"))
#APPEND list
ls.append("jkl")
print(ls)
#EXTEND list
ls.extend(["mno","pqr"])
print(ls)
#GET INDEX OF VALUE IN LIST
print(ls.index("jkl"))
#INSERT list
print(ls.insert(3,"mmm"))
#pop list
print(ls.pop())
#REMOVE list
print(ls.remove("mmm"))
#REVERSE list
print(ls.reverse())
