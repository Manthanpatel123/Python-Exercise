# 1 write a program to find the prime numbers in a specif range using filter.
def primenumber(x):
    for n in range(2,x):
        if x%2==0:
            return  False
        else:
            return True

filterobj=filter(primenumber,range(50))
print(f"prime number between 1 - 50 {list(filterobj)}")