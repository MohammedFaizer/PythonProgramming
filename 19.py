str1="aASSaasin@#$$"
up=0
low=0
spec=0
for i in str1:
    if i.isupper()!=0:
        up+=1
    elif i.islower()!=0:
        low+=1
    elif i.isalnum()==0:
        spec+=1
print(f'upper:{up},lower:{low},spec:{spec}')        