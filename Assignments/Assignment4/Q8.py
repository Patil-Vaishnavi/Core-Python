n=int(input("Enter number:"))

for num in range(1,n+1):
    if(num%7==0 and num%5==0):
        print(num,end=" ")