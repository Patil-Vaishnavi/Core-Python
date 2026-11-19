age=int(input("Enter age : "))
ticket=500

if(age<12):
    ticket=500*(30/100)
    print(ticket)
elif(age>59):
    ticket=500*(50/100)
    print(ticket)
else:
    print(ticket)