import re # regular expression
"""
[] -> set of characters
[^] -> complementing the set
"""
email = input("what's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email): # match from start of the string, to left all characters accepted 
    # except "@", then "@", then all characters are accepted axcept "@" then .edu then matches the end of the string.
    print("valid")
else:
    print("invalid")