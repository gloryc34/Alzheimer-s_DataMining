import numpy as np
from matplotlib import pyplot as plt

years = [2015, 2016, 2017, 2018, 2019, 2020]
overallHealth = [11000, 11236, 12416, 11051, 12185, 13805]

z = np.polyfit(years, overallHealth, 2)
p = np.poly1d(z)

years.append(2021)
overallHealth.append(p(2021))

plt.plot(years, p(years), "red")
plt.scatter(years, overallHealth, s=100)

plt.xlabel("Years")
plt.ylabel("Overall Health")

plt.show()
