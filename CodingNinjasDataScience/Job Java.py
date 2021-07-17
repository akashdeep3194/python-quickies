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
    if "Java" in BasicQualifications:
        jm[country_Code] = jm.get(country_Code,0)+1
        if count<jm[country_Code]:
            count=max(count,jm[country_Code])
            ans = country_Code
print(ans,count)
