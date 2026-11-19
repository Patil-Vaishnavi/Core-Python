n=int(input("Enter number : "))

a=n%10
num=n//10
b=num%10
num=num//10
c=num%10
d=num//10

reverse=a*1000+b*100+c*10+d
print(reverse)