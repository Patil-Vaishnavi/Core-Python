li=[1,2,3,4,5,6,7,8,9]
sq_li=[]
cube_li=[]

for i in range(0,len(li)):
    sq_li+=[li[i]**2]
    cube_li+=[li[i]**3]
print("Original list:",li)
print("Square of elements:",sq_li)
print("Cube of elements:",cube_li)