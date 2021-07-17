import csv

with open("year2017.csv", "r") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))
casualitiesPerCountry = {}
casualties_explosives = 0

for ele in file[:]:
    if ele["casualities"] == '':
        ele["casualities"] = 0
    casualitiesPerCountry[ele["Country"]] = casualitiesPerCountry.get(ele["Country"], 0) + int(float(ele["casualities"]))

for x in casualitiesPerCountry.keys():
    print(x, casualitiesPerCountry[x])
