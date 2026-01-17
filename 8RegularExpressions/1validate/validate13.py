import re # regular expression

"""
flags
re.IGNORECASE
re.MULTILINE
re.DOTALL
"""
email = input("what's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGONORECASE): # allows all caps 
    print("valid")
else:
    print("invalid")