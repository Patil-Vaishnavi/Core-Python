N=int(input('Enter Three Digit Number :'))

A=N%10
N=N//10
B=N%10
C=N//10


Reverse=A*100+B*10+C

print(f'The Reverse Number is {Reverse}')