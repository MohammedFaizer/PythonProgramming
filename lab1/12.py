str1='hello world'
print(str1.capitalize())
a=str1.split()
for i in a:
    print(i.capitalize(),end=' ')
print()    
str2='HeLlO wOrLd'   
k=0
inverstr=''
for i in str2:
    if k%2==0 and i!=' ':
        inverstr+=i.lower()
        k+=1
    elif i!=' ':
        inverstr+=i.upper()
        k+=1    
    else:
        inverstr+=' '
print(inverstr)  
ster='hello world'
replace='friend'
print(ster.replace('world',replace))