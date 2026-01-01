import sys

from sayings2 import hello # import the hello function

if len(sys.argv) == 2:
    hello(sys.argv[1])
