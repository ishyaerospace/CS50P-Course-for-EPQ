import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()# contains the information of what the user typed after "-n"

for _ in range(int(args.n)):
    print("meow")

#if user hasnt typed -n then it throws a typeerror