# Importing the Libraries

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Setting a theme for the plots

sns.set_theme()

# House price dataset

from sklearn.datasets import fetch_california_housing
california_housing = fetch_california_housing()

house = pd.DataFrame(california_housing.data, columns= california_housing.feature_names)
house['MedHouseVal'] = california_housing.target

print(house.head())

# Correlation: Positive and Negative

correlation = house.corr()

# Constructing a Heat Map
plt.figure(figsize= (10, 10))
sns.heatmap(correlation, cbar= 'True', square= 'True', fmt= '.1f', annot= True, annot_kws= {'size': 8}, cmap = 'Greens')
plt.show()


