# do not need to specify the variable type
# declare a variable and it's type by given it a value

# example with integers and floats
a = 12
b = 21
d = 21.0
c = a + b
e = a + d
print(c)
print(e)

# strings
# use single or double quotes

print("hello")
print('hello')

# how to do apostrophes
print("it's mine")
print('it\'s mine') 

# reading input from the keyboard
number = int(input("Enter an integer: "))

# check if number is less than 100
if number <= 100:
    print("Number is less than or equal 100")
else:
    print("Number is greater than 100")

# check if number is even
n = int(input("Enter a number: "))

if n%2 == 0:
    print("Even Steven")
else:
    print("That's odd")
