n=9
for i in range(2,n//2+1):
    if n%i==0:
        print('not an prime numbers')
        break
else:
    print('prime number')