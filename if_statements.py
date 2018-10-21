# file to mess around with if statements in python

# multiple if else example
def if_else_test():
    x = int(input("Enter a number: "))
    if x < 0:
        print("Your number is negative :(")
    elif x > 0:
        print("Your number is positive :D")
    else:
        print("Your number is zero!")

if_else_test()