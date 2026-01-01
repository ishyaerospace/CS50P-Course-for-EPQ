def main():
    x = int(input("What's x? "))
    print("x squared is", square(x)) # function used within another function


def square(n): # function to multiply number (parameter) by it self
    return n * n


main() # calls main function to run
