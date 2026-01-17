import re

url = input("URL: ").strip()

matches = re.search(r"^(https?:)?(//www\.)?//twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"username: {matches.group(3)}") # gets the username (.+) at the end

