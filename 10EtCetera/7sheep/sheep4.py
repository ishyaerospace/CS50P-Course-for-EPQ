def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)
        
def sheep(n):
    for i in range(n):
        yield "s" * i #return one value at a time -> in case the number is large like 10000 the program will not hang as it will return a small amount at a time

if __name__ == "__main__":
    main()