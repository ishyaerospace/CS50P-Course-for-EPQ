import re

name = input("what's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name) # use of parenthesis for capturing purposes

if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

print(f"hello, {name}")