import csv
import math

with open("year2017.csv", "r") as file_obj:
    file_read = csv.reader(file_obj, skipinitialspace=True)
    line = list(file_read)
    line = line[:]
    index_dict = {}
    index_Wounded = 0
    index_country = 0

    total_wounded_india = 0

    wounded_india = []

    i = 0
    for ele in line[0]:
        index_dict[ele] = i
        i += 1
    index_Wounded = index_dict['Wounded']
    index_country = index_dict['Country']

    for r in line[1:]:
        if r[index_Wounded] == "" or r[index_country] != "India":
            continue
        wounded_india.append(math.floor(float(r[index_Wounded])))
        total_wounded_india += wounded_india[-1]
    print(total_wounded_india)

