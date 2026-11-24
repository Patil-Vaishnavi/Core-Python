li = [10, 20, 30, 40, 50]

new_li = []

for i in range(0, len(li)):
    new_li = new_li + [li[i]]

print("Original List:", li)
print("Duplicate List:", new_li)

print(id(li))
print(id(new_li))