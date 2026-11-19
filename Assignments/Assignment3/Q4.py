S1=float(input("Enter first side:"))
S2=float(input("Enter second side:"))
S3=float(input("Enter third side:"))

if(S1+S2>S3 and S1+S3>S2 and S2+S3>S1):
    print("Valid")
else:
    print("Not Valid")