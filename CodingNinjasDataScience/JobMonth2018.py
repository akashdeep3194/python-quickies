import csv

with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))

countCA = 0
jm = dict()
max_month = ""
max_count = 0
for ele in file[:]:
    year = (ele["Posting_date"][-4:])
    if year == "2018":
        month = ele["Posting_date"][:ele["Posting_date"].find(" ")]
        jm[month] = jm.get(month, 0) + 1
        if max_count < jm[month]:
            max_count = jm[month]
            max_month = month
print(max_month, max_count)
