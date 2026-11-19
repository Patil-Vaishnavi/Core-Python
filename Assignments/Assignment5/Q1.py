userid="admin"
pwd=123

for i in range(3):
    id=input("Enter user id:")
    password=int(input("Enter password:"))

    if(userid==id and pwd==password):
        print("Successfully login")
        break
    else:
        print("Incorrect userid and pwd")

else:
    print("your 3 attempts are over")