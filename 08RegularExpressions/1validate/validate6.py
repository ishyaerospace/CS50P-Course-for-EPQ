import re # regular expression
"""
special symbols:
. -> any character except a newline
* ->0 or more repetitions
+ -> 1 or more repetitions
? -> 0 or 1 repetitions
{m} -> m repetitions
{m,n} -> m-n repetitions
"""
email = input("what's your email? ").strip()

if re.search(".+@.+", email): # .+ (something to the left) @ .+ (something to the right), ..* does the same thing as .+
    print("valid")
else:
    print("invalid")