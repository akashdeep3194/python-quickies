import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("startup_funding.csv")
yrs = df["Date"].str.slice(start=-4)
yrs = yrs.value_counts()
yrs.sort_index(inplace=True)
for ele in yrs.index:
    print(ele, yrs[ele])

plt.plot(yrs.index, yrs.values)
plt.show()
