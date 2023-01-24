import math

def find_square_root(num):
    try:
        if num < 0:
            raise ValueError("Square root of negative numbers is not defined.")
        return math.sqrt(num)
    except ValueError as e:
        print(e)

num = float(input("Enter a number: "))
print("Square root of {} is: {}".format(num, find_square_root(num)))
