li1=[10,20,30,40,60,70,80]
li2=[1,34,60,23,40,30,10]

li3=[]

for i in li1:
    if(i in li2):
        li3.append(i)
print(li3)