names = []# list are stored in program memory. 

for _ in range(3):
    names.append(input("What's your name? ")) # append input to list

for name in sorted(names): # sort names
    print(f"hello, {name}")
