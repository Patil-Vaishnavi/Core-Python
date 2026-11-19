def power(n):
    pow=1
    for i in range(1,n+1):
        pow*=n
    return pow
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=power(i)
    return sum
n=5
res=sum(n)
print(res)