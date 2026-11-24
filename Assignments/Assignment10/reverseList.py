li=[10,20,30,40,50,60]


#Slicing
# rev=li[::-1]
# print(rev)

rev=[]
for i in range(len(li)-1,-1,-1):
    rev.append(li[i])
print(rev)
