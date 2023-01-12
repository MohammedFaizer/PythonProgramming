def compute(n):
    if n>1:
        x=lambda a:(a/2)
        print(n)
        return compute(x(n)) 
    else:
        print(">>",n)
        return n+1
        
num=int(input('Enter the number:'))
print(compute(num))