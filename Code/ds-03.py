## Code for note DS-03Py ##

# NumPy arrays #
import numpy as np
x = np.array(range(0,10))
x
y = np.array([[0, 7, 2, 3], [3, 9, -5, 1]])
y
y.shape
np.sqrt(x)
x[:3]
y[:1, 1:]

# Plotting with Matplotlib #
import matplotlib.pyplot as plt
x = np.linspace(0, 2, 100)
plt.figure(figsize=(4,4))
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.legend()
# plt.savefig('C:/Users/mcanela/Dropbox (Personal)/DataSci material/TeX files/Figures/fig 03.1.pdf')
plt.show()

# Pandas series and data frames #
import pandas as pd
s = pd.Series(range(0, 10))
s
s1 = pd.Series([1, 5, 'Messi'])
s1
s1.index
s1.index = np.array(['a', 'b', 'c'])
s1
df = pd.DataFrame({'v1': range(0, 5),
    'v2': ['a', 'b', 'c', 'd', 'e'],
    'v3': np.repeat(-1.3, 5)})
df
df.dtypes
df.columns
df.values
df.sort_values(by='v1', ascending=False)

# Selection #
df[['v1', 'v2']]
df[1:3]
expr = df['v1'] > 2
df[expr]
df.loc[1:2]
df.loc[:2, :'v2']
df.iloc[:3, :2]

# Exploring a data set #
df.shape
df.head(2)
df.info()
df.describe()

# Missing values #
df.iloc[0, 0] = np.nan
df.isna()
df.isna().sum()
df.dropna()

# Duplicates #
df['v3'].drop_duplicates()
df.drop_duplicates()
df['v3'].duplicated()
df.duplicated()
