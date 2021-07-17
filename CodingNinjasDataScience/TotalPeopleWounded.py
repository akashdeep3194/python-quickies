import csv
import math

with open("year2017.csv", "r") as file_obj:
    file_read = csv.reader(file_obj, skipinitialspace=True)
    line = list(file_read)
    line = line[:]
    index_Wounded = 0
    total_Wounded = 0
    for ele in line[0]:
        if ele == "Wounded":
            break
        index_Wounded += 1
    for r in line[1:]:
        if r[index_Wounded] == "":
            continue
        total_Wounded += math.floor(float(r[index_Wounded]))
    print(total_Wounded)
