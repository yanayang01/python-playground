# to open a file use open(path, mode)
# modes are: "r" read only, "w" write, "a" append
# default is read only
import os

# change directory (defaults to /mu_code)
os.chdir("/home/yana/Documents/python/python-playground")
print(os.getcwd())

file = open("sample.txt")
file.close()
# should explicitly close each opened file
# there is an upper limite to number of files a program can open

# read a file to actually use the content
file = open("sample.txt")
print(file.read())
file.close()

file = open("sample.txt")
print(file.readline())  # reads one line
print(file.readline())
file.close()

file = open("sample.txt")
print(file.readlines())  # gets all lines, puts into list
file.close()

# loop through the lines of the file
file = open("sample.txt")
for f in file:
    print(f, end='')
file.close()

# using with statement
# it will close the file for you!
with open("sample.txt") as file:
    for f in file:
        print(f, end='')

# writing to a file
file = open("sample.txt", "w")
file.write("i wrote this into the file through python!\n")
file.close()

with open("sample.txt") as file:
    print(file.read())
    
# a function to count spaces, tabs, new lines in your file
import os
import sys

def parse_file(path):
    """
    parses a file in the path and returns the count of spaces, tabs,
    and lines as a tuple
    """
    
    file = open(path)
    i = 0
    spaces = 0
    tabs = 0
    
    for i, line in enumerate(file):
        spaces += line.count(' ')
        tabs += line.count('\t')
    
    file.close
    
    return spaces, tabs, i+1

