import csv

with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))

countCA = 0
jm = dict()
count = 0
for ele in file[:]:
    BasicQualifications = (ele["BASIC QUALIFICATIONS"])
    if "BS" in BasicQualifications or "Bachelor" in BasicQualifications or "BA" in BasicQualifications:
        count += 1
print(count)
