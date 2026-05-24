"""
with open("students1.csv") as file: # Reads a CSV file
    for line in file:
        row = line.rstrip().split(",") # csv is comma seperated value. able to split into substring by using comma.
        print(f"{row[0]} is in {row[1]}")
"""

with open("students1.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") # each substring is given a variable
        print(f"{name} is in {house}")