num=int(input("Enter number:"))
original=num
sum=0
while(num>0):
    d=num%10
    num=num//10

    fact=1
    for i in range(1,d+1):
        fact*=i
    sum+=fact
if(sum==original):
    print(f"{original} is a strong number")
else:
    print(f"{original} is not a strong number")