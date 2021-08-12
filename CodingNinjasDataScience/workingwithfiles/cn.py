file_obj = open("Sample.txt", "r")
file_read = file_obj.read(100)
print(file_read)


########################################
file_obj = open("Sample.txt", "r")
file_read = file_obj.readlines()
i = 0
for line in file_read:
    print(line)
    i += 1
    if i == 5:
        break

########################################


file_obj = open("Sample.txt", "r")
file_read = file_obj.readlines()
i=0
for line in file_read:
    print(line)
    i+=1
    if i==5:
        break
########################################
import csv
with open("year2017.csv", "r") as file_obj:
    file_read = csv.reader(file_obj)
    line = list(file_read)
    line = line[1:4]
    for r in line:
        for ele in r:
            print(ele,end=" ")
        print()
########################################

import csv
with open("year2017.csv", "r") as file_obj:
    file_read = csv.reader(file_obj)
    line = list(file_read)
    line = line[:1]
    for r in line:
        for ele in r:
            print(ele)
########################################


import csv
with open("year2017.csv", "r") as file_obj:
    file_read = csv.reader(file_obj)
    line = list(file_read)
    line = line[:11]
    index_country = 0
    for ele in line[0]:
        if ele == "Country":
            break
        index_country+=1
    for r in line[1:]:
        print(r[index_country])

########################################

import csv

with open("year2017.csv", "r") as file_obj:
    file_read = csv.reader(file_obj)
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
            r[index_Wounded] = 0
        total_Wounded+=float(r[index_Wounded])
    print(int(total_Wounded))



########################################


import csv
import math

with open("year2017.csv", "r") as file_obj:
    file_read = csv.reader(file_obj, skipinitialspace=True)
    line = list(file_read)
    line = line[:]
    index_dict = {}
    index_Wounded = 0
    index_country = 0

    total_wounded_india = 0

    wounded_india = []

    i = 0
    for ele in line[0]:
        index_dict[ele] = i
        i += 1
    index_Wounded = index_dict['Wounded']
    index_country = index_dict['Country']

    for r in line[1:]:
        if r[index_Wounded] == "" or r[index_country] != "India":
            continue
        wounded_india.append(math.floor(float(r[index_Wounded])))
        total_wounded_india += wounded_india[-1]
    print(total_wounded_india)


########################################
import csv
import math

with open("year2017.csv", "r") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))

casualties_explosives = 0

for ele in file[:]:
    if ele["Weapon_type"] == "Explosives" and ele["casualities"] != '':
        casualties_explosives += math.floor(float(ele["casualities"]))

print(casualties_explosives)


########################################


import csv
import math

with open("year2017.csv", "r") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))
killedPerCountry = {}
casualties_explosives = 0

for ele in file[:]:
    if ele["Killed"] != '':
        killedPerCountry[ele["Month"]] = killedPerCountry.get(ele["Month"], 0) + math.floor(float(ele["Killed"]))
for key in killedPerCountry.keys():
    print(key, killedPerCountry[key])
########################################


import csv

with open("year2017.csv", "r") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))
casualitiesPerCountry = {}
casualties_explosives = 0

for ele in file[:]:
    if ele["casualities"] == '':
        ele["casualities"] = 0
    casualitiesPerCountry[ele["Country"]] = casualitiesPerCountry.get(ele["Country"], 0) + int(float(ele["casualities"]))

for x in casualitiesPerCountry.keys():
    print(x, casualitiesPerCountry[x])


########################################



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


########################################


## Open and read data file as specified in the question
## Print the required output in given format
import csv

with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))

countCV = 0

for ele in file[:]:
    if "computer vision" in ele["Title"].lower():
        countCV += 1
print(countCV)



########################################
import csv

with open("amazon_jobs_dataset.csv", encoding="utf8") as file_obj:
    file = list(csv.DictReader(file_obj, skipinitialspace=True))

countCA = 0
for ele in file[:]:
    country_Code = (ele["location"][:2])
    if country_Code == "CA":
        countCA += 1
print(countCA)


########################################

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



########################################

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




########################################

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




########################################


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
