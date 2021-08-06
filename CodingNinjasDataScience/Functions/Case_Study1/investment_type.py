import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("startup_funding.csv")

# df["CityLocation"] = df["CityLocation"].str.split("/",expand=True)[0]
# df["CityLocation"] = df["CityLocation"].str.strip().str.title()
# df.loc[df["CityLocation"] == "Delhi", "CityLocation"] = "New Delhi"
df = df[df.InvestmentType.notna()]
df["AmountInUSD"] = df["AmountInUSD"].str.replace(",", "")
df["AmountInUSD"] = df["AmountInUSD"].fillna(0)
df["AmountInUSD"] = pd.to_numeric(df["AmountInUSD"])
df.loc[df["InvestmentType"] == "PrivateEquity", "InvestmentType"] = "Private Equity"
df.loc[df["InvestmentType"] == "Crowd funding", "InvestmentType"] = "Crowd Funding"
df.loc[df["InvestmentType"] == "SeedFunding", "InvestmentType"] = "Seed Funding"
df_funding = df.groupby("InvestmentType")["AmountInUSD"].sum()
df_funding.sort_values(inplace=True, ascending=False)
total = df_funding.sum()
for ele in df_funding.index:
    print("{} {:.2f}".format(ele, (df_funding[ele] * 100) / total))
x = (len(df_funding.index))
plt.pie(df_funding.values, labels=df_funding.index, autopct="%.2f")
plt.axis("equal")
plt.show()
