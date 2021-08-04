import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("amazon_jobs_dataset.csv")
location_split = df["location"].str.split(",", expand=True)

df["ctry"] = location_split[0]
df["city"] = location_split[2]

df = df[df["ctry"] == "IN"]
total = df["ctry"].count()
city = df.city.value_counts(ascending=False)

plt.pie(city.values, labels=city.index, autopct="%.2f%%")
plt.axis("equal")

for cty in city.index:
    print("{}{:.2f}".format(cty.lstrip(), round(city[cty] * 100 / total, 2)), sep="")
plt.show()
