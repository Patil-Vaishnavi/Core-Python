H=int(input('Enter Number of hours:'))
M=int(input('Enter Number of minutes:'))
S=int(input('Enter Number of seconds:'))

HourSeconds=H*60*60

MinutesSeconds=M*60

TotalSeconds=HourSeconds+MinutesSeconds+S

print(f'Toatl Seconds {TotalSeconds}')