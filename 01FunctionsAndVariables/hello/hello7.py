# Demonstrates defining a function with a parameter with a default value


def hello(to="world"): # functions can have parameters with default values
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name) #if varaible wasnt used as parameter then it would print "hello, world"
