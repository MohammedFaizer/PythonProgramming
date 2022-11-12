num=int(input('enter the year to check wether the year is leap year or not'))
if(num%400==0):
    print('leap year')
elif(num%4==0):
    print('leap year')
else:
    print('not a leap year')
