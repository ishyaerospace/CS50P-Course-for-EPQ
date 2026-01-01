name = input("What's your name? ")

file = open("names.txt", "w") # creates a file/ access a file in write mode. (overwrites content inside)
file.write(name)
file.close()
