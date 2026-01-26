def meow(n: int):
    for _ in range(n):
        print("meow")

number = int(input("Number: "))
meows: str = meow(number)
print(meows) # will return none as there is no return value