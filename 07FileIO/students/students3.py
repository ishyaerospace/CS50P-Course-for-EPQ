students = []

with open("students1.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {} # dictionary
        #student["name"] = name
        #student["house"] = house
        student = {"name": name, "house": house}
        students.append(student) # append student name and house to list

for student in students: # iterate through list
    print(f"{student['name']} is in {student['house']}") # single quote is used as double quotes is already used in the f string
