#Take input

P=int(input('Enter Principle:'))
T=int(input('Enter Time:'))
R=int(input('Enter Rate:'))

Amount=P*(1+R/100)**T

CI=Amount-P

print(f'The Compound Intrest is {CI}')