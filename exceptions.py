# examples of exception handling

# a few types of common errors
# print(yana)  # NameError
# print(1 + 'yana')  #TypeError

# handle errors using "try...except" blocks
"""
    try:
        statements
        ...
    except ExceptionName:
        statements evaluated in case ExceptionName happens
"""

# an example
def get_number():
    "returns a float number"
    number = float(input("Enter a decimal value: "))
    return number

"""
while True:  # ctrl+c to interrupt
    try:
        print(get_number())
    except ValueError:
        print("That's not a decimal, try again!")
"""

# an empty except statement can catch any exception
"""
try:
    input()
except:
    print("Unknown Exception")
"""

# ask ilija about raise...
"""
try:
    raise ValueError("A value error occurred")
except ValueError:
    print("ValueError in code")
"""

# using finally
# statements that must be executed under all circumstances, use
# the finally clause

import os
os.chdir("/home/yana/Documents/python/python-playground")

try:
    file = open("sample.txt", "w")
    d = 1 / 0
except ZeroDivisionError:
    print("Stop trying to divide by zero!")
finally:
    file.close()
    print("File is closed")