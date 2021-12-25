# 4 write a python program to find armstrong number in a specific range using map
def armstrongnumber(n):
    m=n
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum+rem**3
        n=n//10
        return True if sum==m else False

n=[345,674,22,34,123,765]
print(n)

r=map(armstrongnumber,n)
print(list(r))