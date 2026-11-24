li=[10,20,40,60,89,60]
n=int(input("Enter number:"))
count=0

for i in range(0,len(li)):
    if(n==li[i]):
        count+=1
if(count>0):
    print(f"Number is present {count} times ")
else:
    print("Number is not present")