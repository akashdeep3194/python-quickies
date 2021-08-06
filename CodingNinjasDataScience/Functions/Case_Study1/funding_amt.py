import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("startup_funding.csv")
df["CityLocation"] = df["CityLocation"].str.split("/",expand=True)[0]
df["CityLocation"] = df["CityLocation"].str.strip().str.title()
df.loc[df["CityLocation"] == "Delhi", "CityLocation"] = "New Delhi"
df["AmountInUSD"] = df["AmountInUSD"].str.replace(",","")
df["AmountInUSD"] = df["AmountInUSD"].fillna(0)
df["AmountInUSD"] = pd.to_numeric(df["AmountInUSD"])

df_city = df.groupby("CityLocation")["AmountInUSD"].sum()
df_city.sort_values(inplace=True,ascending=False)
df_city = (df_city[:10])
total = df_city.sum()
for ele in df_city.index:
    print("{} {:.2f}".format(ele,(df_city[ele]*100)/total))


