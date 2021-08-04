# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import numpy as np

x1 =[0,1,2,3,4,5,6,7,9,10]
y1=[1,2,5,10,17,26,37,50,82,101]
x2 = np.arange(0,40,2)
y2 = 2*x2
plt.plot(x1,y1,label = "y1", linewidth = 1)
plt.plot(x2,y2, label = "2*x2", linewidth = 1)
plt.title("Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
