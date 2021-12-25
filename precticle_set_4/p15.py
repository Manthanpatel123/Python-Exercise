# 15 write a python program to add two matrix
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[11,22,33],[44,55,66],[77,88,99]]
result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]

print(result)