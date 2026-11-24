li=[1,2,3,4,5,6]
new_li=[]

for i in range(0,len(li)):
    # new_li.append(li[i]**3)
    new_li=new_li+[li[i]**3]
print("List having cubes:",new_li)