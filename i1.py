print("hello")
for i in range(1,6):
    for j in range(1,6):
        if(i==1 or j==1 or j==5 or i==5):
            print("*",end='\t')
        else:
            print(" ",end='\t')    
    print('\n')    
