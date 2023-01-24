datas=[]
def insert():
    n=int(input("Enter Your Roll Number:"))
    name=input("Enter Your Name:")
    details=[n,name]
    datas.append(details)

def update():
    pass
def delete():
    pass
def display():
    a=input('Enter your roll number:')
    print(datas)


while True:
    choice=int(input('Enter the Choice:'))
    match(choice):
        case 1:
            insert()
        case 2:
            display()