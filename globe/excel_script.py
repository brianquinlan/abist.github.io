import csv
import json

lines = csv.reader(open("nobel.csv", "rU"))
nob = []
for ctry, lat, lon, num in lines:
    nob = nob + [float(lat),float(lon), float(num)]
output = [
    ["Nobel Prize Winners", nob]
]
print json.dumps(output)