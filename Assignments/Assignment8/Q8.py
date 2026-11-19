def reverse(d):
    
    while(d>0):
        num=d%10
        print(num,end="")
        d=d//10
    
d=456
reverse(d)

