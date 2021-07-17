import csv
import math

with open("year2017.csv", "r") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))
killedPerCountry = {}
casualties_explosives = 0

for ele in file[:]:
    if ele["Killed"] != '':
        killedPerCountry[ele["Country"]] = killedPerCountry.get(ele["Country"], 0) + math.floor(float(ele["Killed"]))
for key in killedPerCountry.keys():
    print(key,killedPerCountry[key])
