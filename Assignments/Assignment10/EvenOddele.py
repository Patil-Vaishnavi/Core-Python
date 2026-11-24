li=[1,2,3,4,5,6,7,8,9]
even_li=[]
odd_li=[]

for i in range(0,len(li)):
    if(li[i]%2==0):
        even_li+=[li[i]]
    else:
        odd_li+=[li[i]]
print("Even list :",even_li)
print("Odd list :",odd_li)
print(li)