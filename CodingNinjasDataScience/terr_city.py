# Open and read data file as specified in the question
# Print the required output in given format
import numpy as np
import csv

file = open("terrorismData.csv", encoding="utf8")
ff = csv.DictReader(file)

city = dict()
# city_count = dict()
for ele in ff:
    if ele["Country"].upper() == "INDIA" and ele["City"].upper() != "UNKNOWN":
        if ele["Wounded"] == "":
            ele["Wounded"] = "0.0"
        if ele["Killed"] == "":
            ele["Killed"] = "0.0"

        city[ele["City"].title()+"\n"+ele["State"].title()] = city.get(ele["City"].title()+"\n"+ele["State"].title(), 0) + float(ele["Killed"]) + float(ele["Wounded"])
        # city_count[ele["City"]] = city_count.get(ele["City"], 0) + 1

ans = {k: v for k, v in sorted(city.items(), key=lambda item: item[1], reverse=True)}
# ans_count = {j: x for j, x in sorted(city_count.items(), key=lambda item: item[1], reverse=True)}

i = 1
for key in ans.keys():
    print(key.partition("\n")[0], end=" ")
    print(int(ans[key]))
    if i == 5:
        break
    i += 1

# for key in ans_count.keys():
#     print(key, int(ans_count[key]))
#     #    if i == 5:
#     #        break
#     i += 1
