import numpy as np
import csv

file = open("terrorismData.csv", encoding="utf8")
ff = csv.DictReader(file)
day_arr = []
for ele in ff:
    day_arr.append(ele["Day"])
day_arr = np.array(day_arr)
day = np.unique(day_arr)
max_count = 0
for i in day:
    index = np.where(day_arr == i)[0]
    if max_count < np.size(index):
        max_day = i
        max_count = np.size(index)
print(max_day, max_count)