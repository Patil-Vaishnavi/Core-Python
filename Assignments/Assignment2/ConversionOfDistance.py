feet=int(input('Enter feet: '))
inches=int(input('Enter inches: '))

TotalInches=feet*12 + inches
Centimeters=TotalInches*2.54

Meter=Centimeters/100

RemainingCentimeter=Centimeters%100

print(f'Meter is {Meter} and Cm is {RemainingCentimeter}')