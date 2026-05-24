email = input("what's your email? ").strip()

username, domain = email.split("@") # split one string into multiple strings where the @ symbol is

if (username) and ("." in domain):
    print("valid")
else:
    print("invalid")

#checks if there is a username that was inputed and if there is '.' in the domain substring 