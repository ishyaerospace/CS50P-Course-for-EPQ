def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n
#   return n + n #gives errors in the test


if __name__ == "__main__": # only called if the script is run.
    main()
