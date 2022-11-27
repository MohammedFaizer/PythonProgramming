import time 
hr=int(input('Enter the hour'))
min=int(input('Enter the min'))
sec=int(input('Enter the sec'))
print('Exam started.....')
i=0
while i==0:
    
    time.sleep(1)
    print("{:02d}:{:02d}:{:02d}".format(hr,min,sec),end='\r')
    if sec==0 and min==0 and hr==0:
        i=1
        print('00:00:00')
    else:
        if(sec==0):
            if (hr!=0 and min==0):
               hr=hr-1
               min=60
            sec=60   
            min=min-1 
        sec=sec-1
print("Time's Out.....")        