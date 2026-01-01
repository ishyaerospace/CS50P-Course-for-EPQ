students = []

with open("students1.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

"""
def get_name(student):
    return student["name"]
"""

for student in sorted(students, key=lambda student: student["name"]): # pass function (lambda) as an arguament. could use key=get_name
    print(f"{student['name']} is in {student['house']}")
