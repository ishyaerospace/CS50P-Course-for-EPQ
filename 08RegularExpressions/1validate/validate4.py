email = input("what's your email? ").strip()

username, domain = email.split("@") # split one string into multiple strings where the @ symbol is

if (username) and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")

#checks if there is a username that was inputed and if the domain substring ends with .edu