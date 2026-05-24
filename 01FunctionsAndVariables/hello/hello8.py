def main(): # using main function to run main code
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main() # calls main function
