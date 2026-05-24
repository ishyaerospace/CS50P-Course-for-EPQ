def main():
    x = get_int("what's x?")
    print(f"x is {x}")


def get_int(prompt): # use of parameter
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass # this makes it so an error message is not sent to user


main()
