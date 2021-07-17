import csv
import math

with open("year2017.csv", "r") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))
killedPerCountry = {}
casualties_explosives = 0

for ele in file[:]:
    if ele["Weapon_type"] == "Explosives" and ele["casualities"] != '':
        casualties_explosives += math.floor(float(ele["casualities"]))

print(casualties_explosives)
