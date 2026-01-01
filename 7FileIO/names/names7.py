names = []

with open("names.txt") as file: # no need to sepecify r as r is default
    for line in file:
        names.append(line.rstrip()) # append to list in memory

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
