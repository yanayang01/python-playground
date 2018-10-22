# second practice file for for loops

# simple example to print elements in a list
def loop_print1():
    a = [1, 2, 3, 4, 5]
    for i in a:
        print(i)

# print every other element in list
def loop_print2():
    a = [1, 2, 3, 4, 5, 6, 7]
    for i in a[::2]:
        print(i)

# use range(start, stop, step) function to create a list of numbers
print(list(range(1, 5)))
print(list(range(1, 10, 2)))
print(list(range(10)))

# using continue to skip a part of the loop
def while_continue_loop():
    while True:
        n = int(input("Enter an integer: "))
        if n < 0:
            continue  # execution back to the start of loop
        elif n ==0:
            break  # ends the loop
        print(f"{n} squared is {n ** 2}")
    print("SEE YA!")

# an else statement after any loop will execute when loop is finished
# it will be skipped if break stops the loop
def loop_else():
    for i in range(0, 5):
        print(i ** 2)
    else:
        print("All Done!")


# loop_print1()
# loop_print2()
# while_continue_loop()
# loop_else()