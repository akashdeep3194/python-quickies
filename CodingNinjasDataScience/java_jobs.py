import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("amazon_jobs_dataset.csv")
location_split = df["location"].str.split(",", expand=True)

df["year"] = df["Posting_date"].str.split(', ', expand=True)[1]

df_Java = df[(df["BASIC QUALIFICATIONS"].str.find("Java") > -1) | (df["BASIC QUALIFICATIONS"].str.find("java") > -1)]

freq = df_Java["year"].value_counts(ascending=True)
freq.sort_index(inplace=True)
i = 0
for yr in freq.index:
    print(yr, freq.values[i], sep=" ")
    i += 1

plt.scatter(freq.index, freq.values)
plt.show()
