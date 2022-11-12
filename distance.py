x1=int(input('Enter the x1:'))
y1=int(input('Enter the y1:'))
x2=int(input('Enter the x2:'))
y2=int(input('Enter the y2:'))
import math
ans=math.sqrt((x2-x1)**2+(y2-y1)**2)
print('the distance between two point is {}'.format(ans))