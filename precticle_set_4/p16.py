# 16 write a python program to transpose given matrix.
x=[[1,2],[3,4],[4,5]]
result=[[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
            result[j][i]=x[i][j]

print(result)