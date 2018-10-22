# file to practice some (canta)loop(e)s!

# while loop to output the fibonacci series
def while_fib(limit=100):
    a, b = 0, 1
    while b < limit:
        # print function has default end = \n
        # this will put everything on the same line, delimited by 
        # a comma (and space)!
        print(b, end=', ')  
        a, b = b, a + b  # now a is b, and b is old b plus a!


# creating a multiplication table using a while loop
def while_multiple():
    i = 1
    print("-" * 50)  # a line of dashes!
    while i < 11:
        n = 1
        while n <= 10:
            print(f"{i*n:4d}", end=' ')
            n += 1
        print()
        i += 1
    print("-" * 50)  # a line of dashes!

# a while loop to print asterisks
def while_print():
    r = int(input("Enter the number of rows: "))
    if r <= 10:
        while r >= 0:
            x = "*" * r
            print(x)
            r -= 1
    else:
        print("That's too many rows!")

# lists: comma seperated between square brackets
a = [1, 2, 3, 4, 'Yana', 'Nico']

# access items in a list using square brackets and item position
print(a[0])
print(a[5])

# access items in a list in reverse using negative positions
print(a[-1])
print(a[-2])

# access a portion of the list using : or :: to indicate range
print(a[1:4])
print(a[3:-1])
print(a[1::2])  # s[i:j:k] means slice s from i to j with step k

# check if certain elements are in a list
print('Yana' in a)
print('Home' in a)

# while_fib(limit=1000)
# while_multiple()
# while_print()