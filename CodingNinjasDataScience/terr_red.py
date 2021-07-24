# Open and read data file as specified in the question
# Print the required output in given format
import numpy as np
import csv

file = open("terrorismData.csv", encoding="utf8")
ff = csv.DictReader(file)

max_count = 0
cas_count = 0

for ele in ff:
    if ele["Year"] == "1999" and 5 <= int(ele["Month"]) <= 7:
        if ele["Killed"] == "":
            ele["Killed"] = "0.0"
        if ele["Wounded"] == "":
            ele["Wounded"] = "0.0"
        cas_count = int(float(ele["Killed"])) + int(float(ele["Wounded"]))
        if max_count < cas_count:
            max_count = cas_count
            max_city = ele["City"]
            max_tg = ele["Group"]

print(int(max_count), max_city, max_tg)
