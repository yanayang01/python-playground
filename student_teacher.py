# an example to illustrate inheritance of classes

class Person(object):
    """
    returns a person object with a given name
    """
    
    def __init__(self, name):
        self.name = name
    
    def get_details(self):
        "returns the name of person as a string"
        return self.name


class Student(Person):
    """
    returns a student object given a name, major, and year
    """

    def __init__(self, name, major, year):
        Person.__init__(self, name)
        self.major = major
        self.year = year

    def get_details(self):
        "returns the student details as a string"
        return "%s is studying %s and is graduating %s." % (self.name, self.major, self.year)
    

class Teacher(Person):
    """
    returns a teacher object, takes a list of strings (subjects)
    """

    def __init__(self, name, subjects):
        Person.__init__(self, name)
        self.subjects = subjects
    
    def get_details(self):
        return "%s teaches %s" % (self.name, ", ".join(self.subjects))


person1 = Person("Yana")
student1 = Student("Nico", "Math", 2020)
teacher1 = Teacher("Ilija", ["Math", "CS", "Physics"])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
