def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=fact(i)
    return sum
n=5
res=sum(n)
print(res)