import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Colin\Downloads\healthRelated.csv', low_memory=False)
data.columns=['Issue','Counts']
df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
plt.bar(X, Y, color='g')
plt.title("Health Related Issue Counts")
plt.xlabel("Health Issue")
plt.ylabel("Counts")
plt.xticks(fontsize=12)
plt.show()