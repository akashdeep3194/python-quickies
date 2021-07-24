import sys
# Open and read data file as specified in the question
# Print the required output in given format
import time

import numpy as np
import csv

file = open("terrorismData.csv", encoding="utf-8")
ff = csv.DictReader(file)

killed = []
for ele in ff:
    if ele["Country"] == "United States":
        if ele["Killed"] == "":
            killed.append("0.0")
        else:
            killed.append(ele["Killed"])
killed = np.array(killed, dtype=float)
killed = killed.astype("int")
for ele in killed:
    print(ele)

# #
# # for ele in killed:
# #     print(ele)
#
