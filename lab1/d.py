hours=int(input("Enter the hour in"))
min=int(input("Enter the minutes in"))
hourso=int(input("Enter the hour out"))
mino=int(input("Enter the minutes out"))
start=hours*60+min
end=hourso*60+mino
timehr=int((end-start)/60)
timemin=int((end-start)%60)
print(timehr)
print(timemin)
vechicle=input('Enter the vechicle type:')
if(end-start<=180):
    if(vechicle=="truck"):
        print(20*timehr)
    elif(vechicle=="car"):
        print(10*timehr)
    elif(vechicle=="bike"):
        print(5*timehr)
else:
    if(vechicle=="truck"):
        print(30*timehr)
    elif(vechicle=="car"):
        print(20*timehr)
    elif(vechicle=="bike"):
        print(10*timehr)
     
