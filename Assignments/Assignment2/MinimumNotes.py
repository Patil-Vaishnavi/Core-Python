A=int(input('Enter the Amount:'))

N2000=A//2000
A=A%2000

N500=A//500
A=A%500

N200=A//200
A=A%200

N100=A//100
A=A%100

N50=A//50
A=A%50

N20=A//20
A=A%20

N10=A//10
A=A%10

Total=N2000+N500+N200+N100+N50+N10

print(f'Minimum Number Of notes are {Total}')

