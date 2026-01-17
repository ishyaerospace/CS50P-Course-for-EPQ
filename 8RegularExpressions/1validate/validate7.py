import re # regular expression

email = input("what's your email? ").strip()

if re.search(r".+@.+\.edu", email): # r = raw data and allows dev to pass through the special characters as a raw data
    print("valid")
else:
    print("invalid")

# a whole sentence with the email inside can be valid