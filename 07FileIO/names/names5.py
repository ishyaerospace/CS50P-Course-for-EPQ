with open("names.txt") as file: #access file
    lines = file.readlines() # read all lines in file and returns it in a list

for line in lines: # iterates through the list
    print("hello,", line.rstrip()) # removes the new line (\n)
