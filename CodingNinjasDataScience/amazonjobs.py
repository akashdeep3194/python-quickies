import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
file_obj = open('amazon_jobs_dataset.csv',encoding='utf-8')
data = pd.read_csv(file_obj)
date = data['Posting_date']
year = date.str.split(', ', expand = True)[1]
freq = year.value_counts(ascending = True)
freq.sort_index(inplace=True)
x = freq.index
y = freq
plt.plot(x, y, marker = 'o')
plt.title('Year vs No. of Job Openings')
plt.xlabel('Year')
plt.ylabel('No. of Job Openings')
for i in range(len(x)):
    print(x[i],y[i])
