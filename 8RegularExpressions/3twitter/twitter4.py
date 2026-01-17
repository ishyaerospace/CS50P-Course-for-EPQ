import re

url = input("URL: ").strip()

# re.sub(pattern, replace, string, count=0, flags=0)

username = re.sub(r"^(https?:)?(//www\.)?//twitter\.com/", "", url)
print(f"Username: {username}")
