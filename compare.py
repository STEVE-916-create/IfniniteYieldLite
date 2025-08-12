# ratio calculator

import requests

iyl = requests.get("https://raw.githubusercontent.com/STEVE-916-create/IfniniteYieldLite/main/sauce")
iyr = requests.get("https://raw.githubusercontent.com/EdgeIY/infiniteyield/master/source")

print(f"IY File Size: {len(iyr.content)}")
print(f"IY Lite File Size: {len(iyl.content)}")
print(f"Ratio: {100 * len(iyl.content) / len(iyr.content):.2f}%")