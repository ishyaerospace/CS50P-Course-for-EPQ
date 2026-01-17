import re # regular expression

"""
A|B -> either A or B
(...) -> a group
(?:...) non-capturing version
"""
email = input("what's your email? ").strip()

if re.search(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(edu|org|com)$", email): 
    print("valid")
else:
    print("invalid")