# Importing the Libraries

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Setting a theme for the plots
sns.set_theme()

# Titanic Dataset
titanic = sns.load_dataset('titanic')
print(titanic.head())

# Count plot
sns.countplot(x= 'class', data=titanic)
plt.show()

sns.countplot(x= 'survived', data=titanic)
plt.show()