n=int(input("Enter the number of passengers:"))
m=int(input("Enter the ticket price:"))
for i in range(n):
    age=int(input("Enter the age of passenger:"))
    if(age<12):
        price=m-m*(30/100)
        print("Ticket cost:",price)
    elif(age>59):
        price=m-m*(50/100)
        print("Ticket cost:",price)

    else:
        print("Ticket cost is:",m)

