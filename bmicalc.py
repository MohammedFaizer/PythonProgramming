weight=float(input('Enter your Weight only in kg:'))
height=float(input('Enter your height only in cm:'))
if(height>=60 and height<=300 and weight>=4 and weight<=300):
    bmi=weight/((height/100)**2)
    if(bmi<18.5):
        print('UNDER WEIGHT')
    elif(bmi>=18.5 and bmi<25):
        print('NORMAL')
    elif(bmi>=25 and bmi<30):
        print('OVER WEIGHT')
    else:
        print('OBESE')
    print('{:.2f}'.format(bmi))                

else:
    print('invalid input')    
