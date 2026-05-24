import re # regular expression
"""
^ -> matches the start of the string
$ -> matches the end of the start of just before the newline at the end of the string
"""
email = input("what's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email): 
    print("valid")
else:
    print("invalid")