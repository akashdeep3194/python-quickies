# Open and read data file as specified in the question
# Print the required output in given format# Open and read data file as specified in the question
# Print the required output in given format


import pandas as pd

df = pd.read_csv("terrorismData.csv")

k = df["Killed"].idxmax()
klv = df.loc[k]["Killed"]
grp = df.loc[k]["Group"]
ctry = df.loc[k]["Country"]

print(int(klv),ctry,grp)





