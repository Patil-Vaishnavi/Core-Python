li=[10,20,30,40,50,60,70]
max=li[0]
min=li[0]

for ind in range(1,len(li)):
    if(li[ind]>max):
        max=li[ind]
print("Max=",max)

for ind in range(1,len(li)):
    if(li[ind]<min):
        min=li[ind]
print("Min=",min)