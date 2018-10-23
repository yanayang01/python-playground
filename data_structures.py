# file to mess around with different data structures

# lists - methods to manipulate lists

# add to an existing list
a = [1, 1, 1, 2, 3, 4, 5]
a.append(6)  # append adds to the end of a list
print(a)

a.insert(0, 0)  # insert adds (position, value) to the list
print(a)

a.insert(0, 100)
print(a)

# counting
print(a.count(1))  # how many times '1' appears in list a

# removing items from list
a.remove(0)  # remove 0's from the list 
print(a)

# can also use key word 'de' to remove items from a list
del a[-1]
print(a)

# reverse the list!
a.reverse()
print(a)

# another way to add to an exisiting list
b = [20, 21, 22]

# when b is a list, append will append the list b as a single element
a.append(b)  
print(a)
print(a[-1])

# to add list b to list a, use extend()
a.extend(b)
print(a)

# sorting a list
# a.sort() this will not work since not all elements are of the same type

# remove b first
a.remove(b)
print(a)
a.sort()
print(a)

# pop method - pop() removes last element or pop(i) to take out i-th element
print(a.pop())
print(a)

print(a.pop(0))  # removes the first element
print(a)

print(a.pop(1))  # removes the second element
print(a)

# list comprehensions - evaluates elements in a list
a = [1, 2, 3]
print([i ** 2 for i in a])  # squares each element in a
print([j + 1 for j in [i ** 2 for i in a]])  # squares + 1 

# tuples - separated by comma, immutable (cannot add, del, edit)
a = 'Yana', 'Nico', 'Ilija'
print(a)

# unpack values of a tuple like this:
x, y, z = a
print(x)
print(y)
print(z)

# you can have a tuple with only one element, create using a trailing comma
a = 123, 
print(type(a))

# sets - no duplicate items, can use set operations
a = set('yana')
print(a)  # unique elements in a

b = set('ilija')
print(b)  # unique elements in b

print(a - b)  # in a but not in b
print(a | b)  # in a or b
print(a & b)  # in a and b
print(a ^ b)  # in a or b, but not both

# use add() or pop() to add or delete items from sets
a.add('s')
print(a)
print(b.pop())

# dictionaries - unordered set of key:value pairs
# keys are unique, mutable objects (such as lists) cannot be keys
data = {'name': 'Yana',
        'gender': 'f', 
        'language': 'Python'}
print(data)
print(data['name'])

# add to dictionaries
data['hobby'] = 'yoga'
print(data)

# delete any key:value pair
del data['hobby']
print(data)

# check if a KEY is in the dictionary
print('hobby' in data)

# use dict() to create dictionaries from tuples
b = dict((('Canada', 'Ottawa'), ('China', 'Beijing')))
print(b)

# loop through items in a dictionary using items()
for i, j in b.items():
    print(f"{j} is the capital of {i}")

# the setdefault() method gets the value from the dictionary
# based on the provided key, if the key does not exist, it will
# return some "default" value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

y = car.setdefault("brand", "NA")
x = car.setdefault("colour", "NA")

print(y)
print(x)

# how to handle if the key does not exist
# print(data.get('foo', 0))  # return 0 if 'foo' gives a key error

# enumerate() and zip()
# enumerate prints element number from a list or any sequence
a = ['a', 'b', 'c', 'd']
for i, j in enumerate(a):
    print(i, j)

# zip can iterate through two sequences
countries = ['Canada', 'China', 'Macedonia']
capitals = ['Ottawa', 'Beijing', 'Skopje']

for i, j in zip(capitals, countries):
    print(f"{i} is the capital of {j}")