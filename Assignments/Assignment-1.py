## Assignment 1 ##

# Importing the data #
import pandas as pd
king = pd.read_csv('https://raw.githubusercontent.com/mcanela-iese/' +
    'DataSci_Course/master/Data/king.csv')

# Linear regression model (class) #
from sklearn import linear_model
lm = linear_model.LinearRegression()
y = king['price']
X = king[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
  'waterfront', 'condition', 'sqft_above', 'yr_built', 'yr_renovated',
  'lat', 'long']]
lm.fit(X, y)
king['pred1'] = lm.predict(X)
r1 = king[['price', 'pred1']].corr().iloc[0, 1]
r1.round(3)

# Scatter plot (class) #
plt.figure(figsize=(6,6))
plt.scatter(king['pred1']/10**3, king['price']/10**3, color='0.3', s=1)
plt.title('Figure 1. Actual vs predicted price (class)')
plt.xlabel('Predicted price (thousands)')
plt.ylabel('Actual price (thousands)')
plt.show()

# Linear regression model (log scale) #
import numpy as np
lm.fit(X, np.log(y))
king['pred2'] = np.exp(lm.predict(X))
r2 = king[['price', 'pred2']].corr().iloc[0, 1]
r2.round(3)

# Scatter plot (log scale) #
plt.figure(figsize=(6,6))
plt.scatter(king['pred2']/10**3, king['price']/1000, color='0.3', s=1)
plt.title('Figure 2. Actual vs predicted price (log scale)')
plt.xlabel('Predicted price (thousands)')
plt.ylabel('Actual price (thousands)')
plt.show()

# Rescaling the plot #
plt.figure(figsize=(6,6))
plt.scatter(king['pred2']/10**3, king['price']/10**3, color='0.3', s=1)
plt.title('Figure 2bis. Actual vs predicted price (log scale)')
plt.xlabel('Predicted price (thousands)')
plt.ylabel('Actual price (thousands)')
plt.xlim(0, 5*10**3)
plt.ylim(0, 5*10**3)
plt.show()

# Direct evaluation of the prediction error (absolute terms) #
king['error1'] = king['price'] - king['pred1']
(king['error1']/10**3).describe().round()
king['error2'] = king['price'] - king['pred2']
(king['error2']/10**3).describe().round()

# Direct evaluation of the prediction error (relative terms) #
(king['error1']/king['price']).describe().round(3)
(king['error2']/king['price']).describe().round(3)

# Trimming the data #
trim = (king['price'] > 10**4) & (king['price'] < 10**6)
king = king[trim]
y = king['price']
X = king[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
  'waterfront', 'condition', 'sqft_above', 'yr_built', 'yr_renovated',
  'lat', 'long']]
lm.fit(X, y)
king['pred3'] = lm.predict(X)
r3 = king[['price', 'pred3']].corr().iloc[0, 1]
r3.round(3)
king['error3'] = king['price'] - king['pred3']
(king['error3']/10**3).describe().round()
(king['error3']/king['price']).describe().round(3)
