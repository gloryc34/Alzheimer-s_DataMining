import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Colin\Downloads\alzArea.csv', low_memory=False)
data.columns=['Area','Counts By Area']
df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
plt.bar(X, Y, color='g')
plt.title("Area Surveyed")
plt.xlabel("Area")
plt.ylabel("Counts By Area")
plt.xticks(fontsize=9)
plt.show()
