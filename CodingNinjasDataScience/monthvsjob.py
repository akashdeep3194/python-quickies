import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("amazon_jobs_dataset.csv")
df["Month"] = df["Posting_date"].str.split(" ", expand = True)[0]
month_freq = df.Month.value_counts(ascending= True)
plt.bar(month_freq.index,month_freq.values)
for mth in month_freq.index:
    print(mth,month_freq[mth])
plt.show()


