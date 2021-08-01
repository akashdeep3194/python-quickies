# Open and read data file as specified in the question
# Print the required output in given format# Open and read data file as specified in the question
# Print the required output in given format


import pandas as pd

df = pd.read_csv("terrorismData.csv")

k = df.groupby("Country")["Country"].count().idxmax()
kco = df[df["Country"] == k].count().max()

kyr = df[df["Country"] == k].groupby("Year")["Year"].count().idxmax()
# kcy = df[df["Country"] == k].groupby("Year")["Year"].count().max()

print(k,kco,kyr)










