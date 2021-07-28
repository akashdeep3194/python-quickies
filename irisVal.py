import numpy as np
import pandas as pd

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=["sl", "sw", "pl", "pw", "Flower Type"])

print(df.head())
ftype = [df.iloc[:, -1].unique()][0]
for z in range(3):
    for j in range(3):
        for i in range(4):
            if j == 0:
                print(round(df[df.iloc[:, -1] == ftype[z]].iloc[:, i].min(), 2), end=" ")
            if j == 1:
                print(round(df[df.iloc[:, -1] == ftype[z]].iloc[:, i].max(), 2), end=" ")
            if j == 2:
                print(round(df[df.iloc[:, -1] == ftype[z]].iloc[:, i].mean(), 2), end=" ")
        print(ftype[z])

# print(df[df.iloc[:, -1] == "Iris-setosa"].iloc[:, 1].mean())
# print(df[df.iloc[:, -1] == "Iris-setosa"].iloc[:, 2].mean())
# print(df[df.iloc[:, -1] == "Iris-setosa"].iloc[:, 3].mean())
