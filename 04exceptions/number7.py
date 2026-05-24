def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? ")) # if value error is not raised return the value
        except ValueError:
            print("x is not an integer")


main()
