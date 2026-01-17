email = input("what's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")

# a single @ can be a valid email