D=int(input("Enter Days:"))

years=D/365

RD=D%365

weeks=RD/7

Days=RD%7

print(f'Years={years} , Weeks={weeks} , Days={Days}')