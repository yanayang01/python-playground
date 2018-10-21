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
        


def loop_test2(n, x):
    # geometric sum of 1/x + 1/(x+1) + 1/(x+2) + ... + 1/n
    sum = 0.0
    if x < n:
        print(f"For x = {x} and n = {n} the geometric sum is:")
        for i in range(x, n):
            sum += 1.0 / i
            print(f"{i} and {sum:.4f}")
    else:
        print("x must be less than n!!!")


def input_into_loop_test2():
    n = int(input("Enter an integer: "))
    print(f"n = {n}")
    x = int(input(f"Enter an integer less than {n}: "))
    print(f"x = {x}")
    loop_test2(n, x)


# loop_test1()
# loop_test2(10, 1)
# input_into_loop_test2()