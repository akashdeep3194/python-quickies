## Open and read data file as specified in the question
## Print the required output in given format
height = [189, 185, 195, 149, 189, 147, 154, 174, 169, 195, 159, 192, 155, 191, 153, 157, 140, 144, 172, 157]
## Weight
weight = [87, 110, 104, 61, 104, 92, 111, 90, 103, 81, 80, 101, 51, 79, 107, 110, 129, 145, 139, 110]

import matplotlib.pyplot as plt
import numpy as np

plt.hist(weight, bins=5, edgecolor="black")
w = (max(weight) - min(weight)) / 5
plt.hist(height, bins=5, edgecolor="black")
h = (max(height) - min(height)) / 5

print(round(min(height) + h * 4), round(min(weight) + w * 2))
plt.xticks(range(40, 200, 5))
plt.show()
