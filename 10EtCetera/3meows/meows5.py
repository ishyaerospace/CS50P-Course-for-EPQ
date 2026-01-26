# pip install mypy

def meow(n: int):
    for _ in range(n):
        print("meow")

number = int(input("Number: "))
meow(number)

#same error comes up unless the command used in terminal is:
#python -m mypy meows4.py

#this source: https://github.com/mypyc/mypyc/issues/1056 states that Currently Python 3.13 isn't supported. Python 3.13 removed some non-public APIs we rely on, among other things.
#which is most likely the reason the program takes long to be analysed by mypy

#mypy checks type hints
# mypy should now not throw an error