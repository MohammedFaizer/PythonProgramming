str=input('Enter the string:')
searchar=input('Enter the character to be searched')
k=0
for i in str:
    if i in searchar:
        print(f'"{searchar}" is in the {k} index')
    k+=1
        