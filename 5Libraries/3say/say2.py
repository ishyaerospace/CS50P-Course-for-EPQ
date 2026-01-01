import sys

from sayings1 import hello # own module

if len(sys.argv) == 2:
    hello(sys.argv[1])
