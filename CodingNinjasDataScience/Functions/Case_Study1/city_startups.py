import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("startup_funding.csv")
df["CityLocation"] = df["CityLocation"].str.split("/",expand=True)[0]

df["CityLocation"] = df["CityLocation"].str.strip().str.title()
# print(df["CityLocation"].unique())
df[df["CityLocation"] == "Delhi"] = "New Delhi"
df_city = df["CityLocation"].value_counts(ascending=False)
df_city = df_city[:10]
plt.pie(df_city.values,labels=df_city.index,autopct="%.2f%%")
plt.axis("equal")
plt.show()
for ele in df_city.index:
    print(ele,df_city[ele])

# plt.plot(yrs.index, yrs.values)
# plt.show()
#
