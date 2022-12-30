unit=float(input('Enter the number of units consumed:'))
if(unit>0 and unit<=150):
    unit=unit*3
    print(unit)
elif(unit>150 and unit<=350):
    unit*=3.75+100
    print(unit)
elif(unit>350 and unit<=450):
    unit*=4+250
    print(unit)
elif(unit>450 and unit<=600):
    unit*=4.25+450
    print(unit)
elif(unit>600):
    unit*=5+600
    print(unit)
else:
    print("Invalid input")


