n=3
for i in range(1,n+1):
    var=i
    for j in range(1,i*2):
        if(j<i):
            print(var,end='\t')
            var-=1
        else:
            print(var,end='\t')
            var+=1
    print()    
        