import re
with open('output.txt','w')as output_file: 
    text='hello this is me faizer .the rest is my 23 hr of the world'
    text=re.sub(r'(^|[.?!])\s*([a-zA-Z])',lambda m:m.group(0).upper(),text)
    text=re.sub(r'\d+',lambda m:f'({m.group()})',text)
    output_file.write(text)    