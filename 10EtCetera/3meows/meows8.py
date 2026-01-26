def meow(n: int) -> str: 
    return "meow\n" * n

number = int(input("Number: "))
meows: str = meow(number) 
print(meows, end="") 

#mypy does not return error: Success: no issues found in 1 source file