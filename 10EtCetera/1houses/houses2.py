students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Slytherin"},
    {"name": "padma", "house": "Ravenclaw"},    
]

houses = set() # returns a collection of elements that are not repeated
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)