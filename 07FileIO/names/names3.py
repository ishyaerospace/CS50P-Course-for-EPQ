name = input("What's your name? ")

file = open("names.txt", "a") # appends input to the file (does not overwrite content)
file.write(f"{name}\n") # adds a new line
file.close()
