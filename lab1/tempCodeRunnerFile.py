n=11
for i in range(1,n+1):
    for j in range(1,n+1):
        if ( i==j or i+j==n+1):
            print('$',end='\t')
        elif(i==1 or j==1 or i==n or j==n):
            print('*',end='\t')    
        else:
            print(' ',end='\t')    
    print()    