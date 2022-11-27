import time
import datetime
hour=int(input('Enter the hour:'))
min=int(input('Enter the minute:'))
sec=int(input('Enter the seconds:'))
sec=hour*3600+min*60+sec
while sec:
    print(datetime.timedelta(hours=0,minutes=0,seconds=sec),end='\r')
    time.sleep(1)
    sec-=1
print('Times Out')   