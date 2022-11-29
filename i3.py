print("hello")
for i in range(1,6):
    for j in range(1,6):
        if(i==1 or j==1 or j==5 or i==5):
            if(i==j or (j==1 and i==5)or(j==5 and i==1)):
                print("$",end='\t')
            else:
                print("*",end='\t')
        else:
            if(i==j or (j==2 and i==4)or(j==4 and i==2)):
                print("$",end='\t')
            else:
                print(" ",end='\t') 
               
    print('\n')    