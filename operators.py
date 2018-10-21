# shorthand operators
a = 12
a += 1  # equivalent to a = a + 1
print(a)

b = 12
b /= 2  # equivalent to b = b / 2
print(b)

# try this out in a while loop
def loop_test1():
    N = 10000
    a = int(input("Enter an integer: "))
    print("Behold the power of squares!")
    while a < N:
        print("%d" % a)
        a *= a  # equivalent tp a = a * a

# geometric sum of 1/x + 1/(x+1) + 1/(x+2) + ... + 1/n
def loop_test2(n, x):
    sum = 0.0
    if x < n:
        print(f"For x = {x} and n = {n} the geometric sum is:")
        for i in range(x, n):
            sum += 1.0 / i
            print(f"{i} and {sum:.4f}")
    else:
        print("x must be less than n!!!")

# function to get the user input for the geometric loop calculation
def input_into_loop_test2():
    n = int(input("Enter an integer: "))
    print(f"n = {n}")
    x = int(input(f"Enter an integer less than {n}: "))
    print(f"x = {x}")
    loop_test2(n, x)


# function to evaluate the quadratic equation
def quadratic_test(a, b, c):
    import math
    d = b * b - 4 * a * c
    print(f"For a = {a}, b = {b}, and c = {c}:")
    if d < 0:
        print("Your roots are imaginary gurl!")
    else:
        root1 = (-b + math.sqrt(d)) / (2.0 * a)
        root2 = (-b - math.sqrt(d)) / (2.0 * a)
        print(f"Your roots are: {root1:.4f} and {root2:.4f}!")

# loop_test1()
# loop_test2(10, 1)
# input_into_loop_test2()
# quadratic_test(30, 4, 1)