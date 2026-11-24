li=[12,24,56,78,23,67,89,56,37,36,78,25,90,62]
li1=[]
li2=[]

for i in li:
    if(i%2==0):
        li1.append(i)
    else:
        li2.append(i)
print("List of even numbers:",li1)
print("List of odd numbers:",li2)