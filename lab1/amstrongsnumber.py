num=input("Enter the number:")
lenth=len(num)
n=int(num)
rev=0
temp=n
rem=n
while(n>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)

print(lenth)