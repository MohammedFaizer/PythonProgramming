num=88676
def compute(n,rev):
    if n<1:
        return rev
    else:
        rem=n%10
        rev=rev*10+rem
        n=n//10
        return compute(n,rev)
reverse=compute(num,0)
print(reverse)            