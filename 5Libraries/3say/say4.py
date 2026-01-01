import sys

from sayings2 import goodbye #import the goodbye function

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
