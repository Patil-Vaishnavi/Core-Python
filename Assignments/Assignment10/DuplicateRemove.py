li = [10, 20, 10, 30, 20, 40]
new_li=[]

for i in range(0,len(li)):
    if li[i] not in new_li:
        new_li.append(li[i])
    else:
        print("Duplicates elements",li[i])

print("List after removing duplicates:",new_li)