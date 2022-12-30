str=input('Enter the string:')
vowel='AEIOUaeiou'
newstr=''
for i in str:
    if i not in vowel:
        newstr+=i
print(newstr)        