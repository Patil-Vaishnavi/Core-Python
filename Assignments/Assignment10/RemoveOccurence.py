li=[10,20,30,40,50,60,40]
n=int(input("Enter number:"))
new_list=[]
for i in range(0,len(li)):
    if(n!=li[i]):
        new_list+=[li[i]]
print(new_list)
