import array as arr
a=arr.array('i',[1,1,2,1,2,0])
eve_count=0
odd_count=0
for i in a:
    if i%2==0:
        eve_count+=1
    else:
        odd_count+=1    
print(f'{odd_count}-odd Numbers and {eve_count}-even Numbers')
    
