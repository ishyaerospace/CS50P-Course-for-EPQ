def main():
    x = get_int() #calls function and stores return value into x variable
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break # break out of while true loop if no value error occurs
    return x 


main()
