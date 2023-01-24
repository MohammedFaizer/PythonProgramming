def smaller_number(num1, num2):
    try:
        if num1 < num2:
            raise AssertionError("First number is smaller than the second.")
        else:
            return min(num1, num2)
    except AssertionError as e:
        print(e)
def check(a=10,b=20):
    try:
        if a>b:
            print("Good")
        else:
            raise AssertionError("Hello  study hard:")    
    except AssertionError as e :
        print(e)
check()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Smaller number:", smaller_number(num1, num2))
