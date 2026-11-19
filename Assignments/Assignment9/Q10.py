def ReverseDigit(num,rev=0):
    if (num==0):
        return rev
    
    d=num%10
    rev=rev*10+d 
    return ReverseDigit(num//10,rev)
                                 
num=123
res=ReverseDigit(num)
print(res)
