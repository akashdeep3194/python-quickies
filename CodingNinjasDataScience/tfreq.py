# Open and read data file as specified in the question
# Print the required output in given format# Open and read data file as specified in the question
# Print the required output in given format


import pandas as pd

df = pd.read_csv("terrorismData.csv")

df_JK = df[(df["State"].str.lower() == "jammu and kashmir")]
df_red = df[(df["State"] == "Jharkhand") | (df["State"] == "Odisha") | (df["State"] == "Andhra Pradesh") | (df["State"] == "Chhattisgarh")]

dfjkc = df_JK.groupby("Year")["Killed"].sum() + df_JK.groupby("Year")["Wounded"].sum()
dfredc = df_red.groupby("Year")["Killed"].sum() + df_red.groupby("Year")["Wounded"].sum()
dfredsum = dfredc[dfredc > 0].sum()
dfredyear = dfredc[dfredc > 0].count()

dfjkcsum = dfjkc[dfjkc > 0].sum()
dfjkcyear = dfredc[dfredc > 0].count()

print(int(dfredsum / dfredyear), int(dfjkcsum / dfjkcyear))
