def main():
    yell("hello", "world")

def yell(*words):
    uppercased = map(str.upper, words)# iterates over words and runs str.upper on each word.
    print(*uppercased)

if __name__ == "__main__":
    main()