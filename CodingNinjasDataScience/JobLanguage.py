import csv

with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))

countCA = 0

countPy = 0
countJava = 0
countCpp = 0

jm = dict()

count = 0
for ele in file[:]:
    BasicQualifications = (ele["BASIC QUALIFICATIONS"])
    country_Code = (ele["location"][:2])
    if country_Code == "IN":
        if "BS" in BasicQualifications or "Bachelor" in BasicQualifications or "BA" in BasicQualifications:
            if "Python" in BasicQualifications:
                countPy += 1
            if "C++" in BasicQualifications:
                countCpp += 1
            if "Java" in BasicQualifications:
                countJava += 1
if countPy > countJava and countPy > countCpp:
    print("Python", countPy)
if countCpp > countJava and countCpp > countPy:
    print("C++", countCpp)
if countJava > countPy and countJava > countCpp:
    print("Java", countJava)
