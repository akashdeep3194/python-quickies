# Open and read data file as specified in the question
# Print the required output in given format


import pandas as pd

df = pd.read_csv("terrorismData.csv")
df = df[(df["Country"] == "India") & (df['Year'] >= 2014)]
df["YMD"] = df['Year'] * 10000 + df['Month'] * 100 + df['Day']
df = df[(df["YMD"] >= 20140526)]
df_grp_ctr = df.count().max()
df =df[df['Group'] != "Unknown"]
df_grp = df.groupby('Group')['Group'].count().idxmax()
print(df_grp_ctr, df_grp)
