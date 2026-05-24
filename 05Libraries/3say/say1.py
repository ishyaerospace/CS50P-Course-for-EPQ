import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1]) # creates a trex saying the message hello, {second arguament}
