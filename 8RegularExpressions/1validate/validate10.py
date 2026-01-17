import re # regular expression

email = input("what's your email? ").strip()

if re.search(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.edu$", email): # excepts only a range of values from 'a to 'z', 'A' to 'Z', '0' to '9', and '_'
    print("valid")
else:
    print("invalid")