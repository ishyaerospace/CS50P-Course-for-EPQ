try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else: # if a valueError does not occur
    print(f"x is {x}")
