def digits(d):
    sum=0
    while(d>0):
        num=d%10
        sum+=num
        d=d//10
    return sum
d=456
res=digits(d)
print(res)
