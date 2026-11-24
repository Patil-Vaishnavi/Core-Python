li1=[34,56,3,2,6,87,56]
li2=[45,78,24,89,2,4,6,79]
li3=[]

for i in li1:
    li3.append(i)
for j in li2:
    if(j not in li3):
        li3.append(j)
print(li3)