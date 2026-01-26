def meow(n: int) -> None: # none is not a return value hint
    for _ in range(n):
        print("meow")

number = int(input("Number: "))
meows: str = meow(number) # mypy will now throw an error stating that there is no return value
print(meows) 