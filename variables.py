# do not need to specify the variable type
# declare a variable and it's type by given it a value

# example with integers and floats
def test_1():
    a = 12
    b = 21
    d = 21.0
    c = a + b
    e = a + d
    print(c)
    print(e)

# strings
# use single or double quotes
def test_2():
    print("hello")
    print('hello')

    # how to do apostrophes
    print("it's mine")
    print('it\'s mine') 

# reading input from the keyboard
def integer_test():
    number = int(input("Enter an integer: "))

    # check if number is less than 100
    if number <= 100:
        print("Number is less than or equal 100")
    else:
        print("Number is greater than 100")

    # check if number is even
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        print("Even Steven")
    else:
        print("That's odd")

# try out a while loop with some floats
def investment_test():
    amount = float(input("Enter investment amount: "))
    rate = float(input("Enter interest rate: "))
    period = int(input("Enter number of years of investment: "))

    # initialize values
    value = 0
    year = 1

    if period <= 10:
        print("Future value: %.2f" % (amount * (1 + rate) ** period))
        print("Your yearly returns are: ")
        while year <= period:
            value = amount * (1 + rate)
            print("Year %d Total Value: %.2f" % (year, value))
            amount = value
            year = year + 1
    else:
        print("Too many periods to print individually, you maniac!")
        print("Future value: %.2f" % (amount * (1 + rate) ** period))

# tuple unpacking
def tuple_test():    
    data = ("Yana Yang", "Canada", "Python")
    name, country, language = data
    print(name)
    print(country)
    print(language)


# formatting strings
# older way to add expressions into a string
def string_test1():
    name = "Yana (is so cool)"
    language = "Python"
    
    # using .format
    message = "{0} is learning {1}.".format(name, language)
    print(message)

# PEP 498 a newer and simple way to embed expressions in a string
# using "f"
def string_test2():
    name = "Yana"
    adjective = input("Enter adjective: ")
    message = f"{name} is so {adjective}!"
    print(message)
    
# f-strings and dates!
def date_test():
    import datetime
    print("What day of the week is it?!")
    # d = datetime.date(2019, 8, 1)
    d = datetime.datetime.now()
    print(f"{d:%F} is a {d:%A}!") #standard formats



# test_1()
# test_2()
# integer_test()
# investment_test()
# tuple_test()
# string_test1()
# string_test2()
# date_test()
