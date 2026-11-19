n=int(input("Enter the number of students:"))
sum_per=0
for i in range(n):

    total=0
    for j in range(5):
        marks=int(input("Enter marks:"))
        total+=marks

    per=total/5
    print("Percentage:",per)
    sum_per+=per

print("Average marks of students:",sum_per/n)