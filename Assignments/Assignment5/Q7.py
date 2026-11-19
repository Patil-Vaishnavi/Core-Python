#1.Sum of factorial series
# n=int(input("Enter n :"))
# sum=0
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     sum+=fact
# print("Sum:",sum)


#2.Sum of power series
# n=int(input("Enter n :"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+n**i
# print("Sum:",sum)


#3.Sum of geometric series
# n=int(input("Enter n:"))
# sum=0
# term=1
# for i in range(n):
#     sum=sum+term
#     term=term*2
# print("Sum",sum)


#4.Sum of series
# a=int(input("Enter a:"))
# sum=0
# for i in range(1,11):
#     sum=sum+(a**i)/i
# print("Sum:",sum)

#5.Sum of the series 

x=int(input("Enter x:"))
n=int(input("Enter n:"))
sum=0
for i in range(1,n+1):
    if i %2 ==1:
        sum=sum+(x**i)/(2*i-1)
    else:
        sum=sum-(x**i)/(2*i-1)
print("Sum:",sum)