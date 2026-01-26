import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n",default=1, help="number of times to meow", type=int) # no longe throws an error and sets meows number to 1
args = parser.parse_args() # contains the information of what the user typed after "-n"

for _ in range(int(args.n)):
    print("meow")

#python meows12.py -h
# returns a help message with a message about -n N      number of times to meow

#python meows12.py -h  
#usage: meows12.py [-h] [-n N]

#options:
#  -h, --help  show this help message and exit
#  -n N        number of times to meow