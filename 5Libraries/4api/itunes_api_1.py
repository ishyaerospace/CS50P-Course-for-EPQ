import sys # allow script to access command-line arguments
import requests # http requests

if len(sys.argv) != 2: # argv[0] = script name, argv[1] = user input
    sys.exit()# if user doesnt provide exactly one argument then script exits

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1] # limit=1 gives only first item in search
)
print(response.json()) # converts API JSON response into a python dictionary. then outputs to terminal

#in cli type python3 itunes0.py {song name}

