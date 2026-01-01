"""

answer = input("Do you agree? ").strip().lower()
if answer == "yes" or answer == "y":
    print("Agreed")
else:
    print("Not agreed")

"""
answer = input("Do you agree? ").strip().lower()
if answer.startswith("y"): # ignores all characters after the first character
    print("Agreed")
else:
    print("Not agreed")
