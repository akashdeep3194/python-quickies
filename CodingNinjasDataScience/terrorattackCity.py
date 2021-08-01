# Open and read data file as specified in the question
# Print the required output in given format


import pandas as pd
import numpy as np
import csv

df = pd.read_csv("terrorismData.csv")
df = df[df['State'] == "Jammu and Kashmir"]
df_city_ctr = df.groupby('City')['City'].count().max()
df_cityname = df.groupby('City')['City'].count().idxmax()
df_city = df[(df['Group'] != "Unknown") & (df['City'] == df_cityname)]
df_city_grp = df_city.groupby('Group')['Group'].count().idxmax()
print(df_cityname, df_city_ctr, df_city_grp)
