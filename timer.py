import time
def countdown(t):
    while t:
        hours, mins = divmod(t,60)
        timer = '{:02d}:{:02d}:'.format(hours,mins)
        print(f'the exam will end in :{timer}', end="\r")
        time.sleep(60)
        t -= 1
    print('Time is over Exam Finished')
 
hr = int(input("Enter the hour: "))
min= int(input("Enter the min: "))
hr=hr*60
min+=hr
countdown(int(min))
