import random

uid =input("Enter userid: ")
pwd=input("Enter password: ")

if uid == "admin" and pwd=="1234":
    n=random.randint(1000,9999)
    x=int(input("Enter number: "))

    if x==n:
        print("Success")
    else:
        print("Failed")

else:
    print("Wrong userid or password")