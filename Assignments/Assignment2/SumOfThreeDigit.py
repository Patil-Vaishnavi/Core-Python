N=int(input('Enter Three Digit Number:'))

A=N//100 #To find first digit
R=N%100 #To find last two digit
B=R//10 #To find Second digit
C=R%10 #To find third digit

TotalSum=A+B+C

print(f'The Total Sum is {TotalSum}')

