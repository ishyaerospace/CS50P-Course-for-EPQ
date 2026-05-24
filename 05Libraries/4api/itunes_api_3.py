import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1]
)
output = response.json()
for result in output["results"]: #iterating through json dictionary
    print(result["trackName"])
