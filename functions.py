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

# how to do this properly
def better_function(a, data=None):
    if data is None:
        data = []  # create empty list
    data.append(a)
    return(data)

# keyword arguments
def f(a, b=5, c=10):
    print(f"a is {a}, b is {b}, and c is {c}")

# can create keyword only functions
# forces user to use the correct keyword for each parameter
def hello(*, name='User'):
    print(f"Hello {name}!")

# only works if you do: hello(name='Yana')

# higher order functions
# takes at least one function as an argument
# or returns another function as an output

def high_func(func, value):
    return func(value)

lst = high_func(dir, int)
print(lst[-3:])
# print(lst)

# map function
# takes a function and an iteratoor
# applies the function to each value of the iterator
# returns a list of results
a = list(range(1, 6))

def square(num):
    "returns the square of a given number"
    return num * num

b = list(map(square, a))
print(b)
