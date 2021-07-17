import csv

with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))

countCA = 0
for ele in file[:]:
    country_Code = (ele["location"][:2])
    if country_Code == "CA":
        countCA += 1
print(countCA)
