# Open and read data file as specified in the question
# Print the required output in given format# Open and read data file as specified in the question
# Print the required output in given format
import numpy as np
import pandas as pd

df = pd.read_csv("terrorismData.csv")

dfjkcyear = dfredyear = len(df["Year"].unique())
df["Cas"] = df["Killed"] + df["Wounded"]

df_JK = df[(df["State"] == "Jammu and Kashmir")]
df_red = df[(df["State"] == "Jharkhand") | (df["State"] == "Odisha") | (df["State"] == "Andhra Pradesh") | (df["State"] == "Chhattisgarh")]

dfjkc = df_JK["Cas"].sum()


dfredc = df_red["Cas"].sum()


dfredsum = int(dfredc.sum())

dfjkcsum = int(dfjkc.sum())

print(dfredsum//dfredyear, dfjkcsum//dfjkcyear)
