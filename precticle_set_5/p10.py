# 10 write a python program script to check if a given key alredy exists in a dictionary
ls={1:12,2:50,3:66,4:2222,5:00,6:88}
k=input("enter the number")
if eval(k) in ls:
    print("key exists")
else:
    print("key not exists")