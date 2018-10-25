# conjunction junction, what's your function?

# simple function to add two numbers together
def add_together(a, b):
    return a + b

print(add_together(1, 3))

# palindrome function
def is_palindrome(s):
    return s == s[::-1]  # is s the same as s reverse?
"""
if __name__ == '__main__':  
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("Palindrome!")
    else:
        print("Not a palindrome :(")
"""

# local and global variables
def change(s):
    a = 90
    print(a)

a = 10

print(f"Before function call {a}")
print(f"Inside change function", end=' ')
change(a)
print(f"After function call {a}")

def change(s):
    global a
    a = 90
    print(a)

a = 10

print(f"Before function call {a}")
print(f"Inside change function", end=' ')
change(a)
print(f"After function call {a}")

# define default values for function
def greater_than(a, b=-100):
    return a > b

print(greater_than(1))
print(greater_than(1, 2))

# default values are evaluated only once
# a mutable object like list will behave differently
def some_function(a, data=[]):
    data.append(a)
    return(data)
# ask ilija what is going on here...
# data as a list exists when the function is created first time 
# so it is not re-evaluated when the function is called
# that's why it keeps adding values to the list data

# keyword arguments

