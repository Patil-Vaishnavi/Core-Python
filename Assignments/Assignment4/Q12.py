num=int(input("Enter number:"))
original=num
sum=0
digits=len(str(num))

while(num>0):
    d=num%10
    num=num//10

    power=1
    for i in range(digits):
        power=power*d
    sum+=power
if(sum==original):
    print(f"{original} is an armstrong number")
else:
    print(f"{original} is not an Armstrong number")