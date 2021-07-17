import csv

with open("year2017.csv", "r") as file_obj:
    file_read = csv.reader(file_obj)
    line = list(file_read)
    line = line[:]
    index_Killed = 0
    total_Killed = 0
    for ele in line[0]:
        if ele == "Killed":
            break
        index_Killed += 1
    for r in line[1:]:
        if r[index_Killed] == "":
            r[index_Killed] = 1
        total_Killed+=float(r[index_Killed])
    print(int(total_Killed))
