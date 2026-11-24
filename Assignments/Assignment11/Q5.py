li = ["apple", "cat", "banana", "dog", "kiwi"]

for i in range(0, len(li)):
    for j in range(i+1,len(li)):
        if(len(str(li[i])) > len(str(li[j]))):
               li[i], li[j] = li[j], li[i]
print(li)