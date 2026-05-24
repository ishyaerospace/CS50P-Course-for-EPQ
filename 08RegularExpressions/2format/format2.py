import re

name = input("what's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name) # use of parenthesis for capturing purposes

if matches:
    last, first = matches.groups() # get return values of groups from parenthesis
    name = f"{first} {last}"

print(f"hello, {name}")