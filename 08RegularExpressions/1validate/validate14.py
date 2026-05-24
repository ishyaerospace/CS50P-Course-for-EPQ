import re # regular expression

email = input("what's your email? ").strip()

if re.search(r"^\w+@(\w\.)?\w+\.edu$", email, re.IGNORECASE): #? 1 or no repetitions
    print("valid")
else:
    print("invalid")