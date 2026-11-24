li=[10,20,30,50,60,100,70,75,76]
m=2
n=5
for i in range(0,len(li)):
    if(li[i]%m==0 and li[i]%n==0):
        print(li[i],end=" ")