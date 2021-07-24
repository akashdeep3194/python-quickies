## Open and read data file as specified in the question
## Print the required output in given format
import pandas as pd

df = pd.read_csv("https://files.codingninjas.in/iris-8116.csv?_ga=2.219237339.396115884.1627134877-1216722654.1627057973")
# print(df[df[df.iloc[:, -1] == "Iris-virginica"].iloc[:, 2] > 1.5])
df_V = df[df.iloc[:, -1] == "Iris-virginica"]
df_V = df_V[df_V.iloc[:, 2] > 1.5]
for index, row in df_V.iterrows():
    for i in range(5):
        print(row[i], end=" ")
    print()
