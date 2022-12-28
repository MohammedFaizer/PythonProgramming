str=input('Enter the string:')
key=int(input('Enter the key:'))
encoded=''
for i in str:
    encoded+=chr(ord(i)+key)  
print('Encoded string is:',encoded)    