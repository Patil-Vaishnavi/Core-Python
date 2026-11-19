def FactorialOfNumber(n):
    if(n<=0):
        return 1
    else:
        return n*FactorialOfNumber(n-1)
n=5
res=FactorialOfNumber(n)
print(res)