students = [
    {"name": "hermione", "house": "Gryffindor"},
    {"name": "harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students) # (function, applied to iterable element)

for gryffindor in gryffindors:
    print(gryffindor["name"])