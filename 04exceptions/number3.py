while True: #loop until value entered is correct datatype
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break # if value inputed is correct data type then break out of while loop

print(f"x is {x}")
