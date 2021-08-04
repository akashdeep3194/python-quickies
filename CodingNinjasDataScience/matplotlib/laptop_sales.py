## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np
import matplotlib.pyplot as plt

company = ['HP', 'Dell', 'Lenovo', 'Asus', 'Apple', 'Acer']
sold = [20000, 43000, 15000, 17000, 22000, 13000]

x = np.array(sold)
t = x.sum()

plt.pie(sold, labels=company, autopct="%.1f%%")
plt.title("Laptop Sales")
for i in range(len(company)):
    z = sold[i]*100/t
    print(company[i], "{:.1f}".format(z))
plt.show()



