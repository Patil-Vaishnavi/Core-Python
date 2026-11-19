def Armstrong(n,digits,sum=0):
    if(n==0):
        return sum
    d=n%10
    sum=sum+d**digits
    return Armstrong(n//10,digits,sum)
    
n=153
res=Armstrong(n,len(str(n)))
if(res==n):
    print("Armstrong")
else:
    print("Not Armstrong")