import csv
with open("year2017.csv", "r") as file_obj:
    file_read = csv.reader(file_obj)
    line = list(file_read)
    line = line[:4]
    index_country = 0
    for ele in line[0]:
        if ele == "Country":
            break
        index_country+=1
    for r in line[1:]:
        print(r[index_country])
