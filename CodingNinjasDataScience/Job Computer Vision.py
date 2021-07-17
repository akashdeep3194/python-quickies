import csv

with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))

countCV = 0

for ele in file[:]:
    if "computer vision" in ele["Title"].lower():
        countCV += 1
print(countCV)
