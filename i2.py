print("hello")
n=5
for i in range(n):
    for j in range(n):
        if i==j:
            print('$',end='\t')
        elif i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end='\t')
        else:
            print(' ',end='\t')    
    print()        
