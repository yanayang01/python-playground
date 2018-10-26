# simple example

class MyClass(object):
    a = 90
    b = 88
    
p = MyClass()
# print(dir(p))

# __init__ method
# the constructor method for a class
name = "Ilija"
class Student(object): 
    """
    returns a student object with name, major, year
    """
    
    def __init__(self, name, major, year):
        self.name = name
        self.major = major
        self.year = year
        print("A student object has been created.")
    
    def print_details(self):
        print(f"Student Name: {self.name}")
        print(f"Major: {self.major}")
        print(f"Graduating Year: {self.year}")

# __init__ is called whenever an object of the class is created
# self is a special variable that points to the current object

# this will give an error, need to specify the arguments
"""
std1 = Student()
"""

std1 = Student("Yana", "Math", "2010")
std2 = Student("Ilija", "Ninja", "2010")
std1.print_details()
std2.print_details()