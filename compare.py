# ratio calculator

import requests

iyl = open("sauce", "rb").read()
iyr = requests.get("https://raw.githubusercontent.com/EdgeIY/infiniteyield/master/source").content

print(f"IY File Size: {len(iyr)}")
print(f"IY Lite File Size: {len(iyl)}")
print(f"Ratio: {100 * len(iyl) / len(iyr):.2f}%")
print(f"Smalled by: {100 * (1 - (len(iyl) / len(iyr))):.2f}%")