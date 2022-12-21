import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Colin\Downloads\surveyeeDescription.csv', low_memory=False)
data.columns=['Gender/Race','Counts By Description']
df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
plt.bar(X, Y, color='g')
plt.title("People Surveyed")
plt.xlabel("Gender/Race")
plt.ylabel("Counts By Description")
plt.xticks(fontsize=12)
plt.show()
