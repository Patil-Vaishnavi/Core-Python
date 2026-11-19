start=int(input("Enter starting number:"))
end=int(input("Enter ending of number:"))

for num in range(start,end+1):
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
            print(original,end=" ")