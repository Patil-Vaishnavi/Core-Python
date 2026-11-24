li=[12,56,75,45,89,36]
max=li[0]
smax=0

for ind in range(1,len(li)):
    if(li[ind]>max):
        smax=max
        max=li[ind]
    elif(li[ind]>smax):
        smax=li[ind]
print("Max=",max)
print("Second largest=",smax)