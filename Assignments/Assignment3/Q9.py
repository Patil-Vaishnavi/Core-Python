s1=int(input("Enter Subject 1 marks : "))
s2=int(input("Enter Subject 2 marks : "))
s3=int(input("Enter Subject 3 marks : "))
s4=int(input("Enter Subject 4 marks : "))
s5=int(input("Enter Subject 5 marks : "))

total=s1+s2+s3+s4+s5
percentage=total/5
print("Marks:",total)
print("percentage:",percentage)

if(percentage>=80):
    print("First Class")
elif(percentage>=60):
    print("Second Class")
elif(percentage>=40):
    print("Third Class")
else:
    print("Fail")

