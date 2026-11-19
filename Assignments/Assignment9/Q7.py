def SumOfDigit(num):
    if(num==0):
        return 0
    
    
    d=num%10
    return d + SumOfDigit(num//10)
    

num=123
res=SumOfDigit(num)
print(res)




