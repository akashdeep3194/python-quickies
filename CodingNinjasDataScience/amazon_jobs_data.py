import csv

with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))

countBangalore = 0
countSeattle = 0

for ele in file[:]:
    if "Bangalore" in ele["location"]:
        countBangalore += 1

    if "Seattle" in ele["location"]:
        countSeattle += 1
print(countBangalore, countSeattle)
