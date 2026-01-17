url = input("URL: ").strip()

username = url.removeprefix("https://twiter.com/")
print(f"username: {username}")