def x(a,b):
    if(b.isdigit() and a.isalpha()):
        print('UserName:',a)
        print('Pan Number:',b) 
    else:
        print('Please enter correctly')    
user_name=input('Enter the user name:')
pan=input('Enter the pan number:')
x(user_name,pan)