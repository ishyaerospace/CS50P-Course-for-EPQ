while True:
    n = int(input("What's n? "))
    if n <= 0:
        continue # skips the rest of the code in the current iteration and jumps directly to the next iteration
    else:
        break # break out of the while true loop

for _ in range(n):
    print("meow")
