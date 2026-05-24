# slicing is a way to extract a portion of a list, string, etc.
#list[start:end] or list[start:] start is inclusive, end is exclusive
#list[:end] start to (end -1)

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
