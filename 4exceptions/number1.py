try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError: # catches ValueErrors
    print("x is not an integer")
