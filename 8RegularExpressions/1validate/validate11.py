import re # regular expression

email = input("what's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email): # \w -> any word character 1 or more
    print("valid")
else:
    print("invalid")

"""
\d -> decimal digit
\D -> not a decimal digit
\s -> whitespace characters
\S -> not a whitespace character
\w -> word character as well as numbers and the underscore
\W -> not a word character
"""