# file to practice strings and string manipulation

# creating multi-lined strings using triple single or double quotes

a = """I am writing
on multiple lines. 
Look at me!"""

print(a)

# you can have two string literals side by side, it will be treated
# like a single string

a = "why " "is " "this " "like " "this"
print(a)

# use len() to find the length of the string
print(len(a)) 

# title, upper, and lower
print(a.title())  # capitalizes beginning of every word
print(a.lower())  # all lowercase
print(a.upper())  # all uppercase

# checking the string using isalnum, isalpha, isdigit
b = "abcd123"
c = "abc 123"
d = "abc"
e = "123"

print(b.isalnum())  # is the string only alpha numeric?
print(c.isalnum()) 

print(d.isalpha())  # is the string only alpha?
print(d.isdigit())  # is the string only numeric?
print(e.isdigit())
# other methods: islower(), istitle(), isupper()

# splitting strings
a = "Yana is awesome"
b = a.split(" ")  # splits the string based on the delimiter and returns a list
c = a.split("a")
print(a)
print(b)
print(c)

# joining strings, takes a list containing strings and joins them
d = " ".join(b)
e = "-".join(b)

print(d)
print(e)

# strip strings using strip(), lstrip(), or rstrip()
# strips leading or trailing characters specified, otherwise white space
s = "   xox abcd oxox"
print(s.strip())
print(s.strip("ox"))
print(s.strip(" xo"))

print(s.lstrip(" "))
print(s.lstrip(" x"))

print(s.rstrip("x"))
print(s.rstrip("xo"))
print(s.rstrip("ox"))

# find text in a string
s = "faulty for a reason"
print(s.find("for"))  # position of the first occurrence
print(s.find("x"))  # if not found, returns -1

# check if strings starts or end with something using 
# startswith() and endswith()

# use [::-1] to reverse a string
s = "abcd"
print(s[::-1])

# iterate over a string
for i in "yana":
    print(i)
