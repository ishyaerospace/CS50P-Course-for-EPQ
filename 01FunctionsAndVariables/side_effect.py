emoticon = "-.-"

def main():
    global emoticon # able to change variables outside of the function.
    say("Is anyone there?")
    emoticon = ":D"
    say("hi")

def say(phrase):
    print(f"{phrase} {emoticon}")

main()