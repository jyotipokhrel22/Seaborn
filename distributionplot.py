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

# Distribution plot

sns.displot(house['MedHouseVal'])
plt.show()

sns.distplot(house['MedHouseVal']) # Gives probability curve
plt.show()