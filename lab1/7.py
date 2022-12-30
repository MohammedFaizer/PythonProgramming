str=input('Enter the string:')
searchar=input('Enter the character to be searched:')
k=0
for i in str:
    if i in searchar:
        k+=1    
print(f'Occurance of {searchar} is :{k}')