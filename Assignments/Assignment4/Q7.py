n=int(input("Enter number:"))

for num in range(1,n+1):
    if(num%2!=0 and num%7!=0):
        print(num,end=" ")
