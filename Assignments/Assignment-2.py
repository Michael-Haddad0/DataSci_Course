## Assignment 2 ##

# Importing the data #
import pandas as pd
churn = pd.read_csv('https://raw.githubusercontent.com/mcanela-iese/' +
    'DataSci_Course/master/Data/churn.csv', index_col=0)

# Logistic regression model #
y = churn['churn']
X1 = pd.get_dummies(churn['datagb'])
X1.head()
X2 = churn[['aclength', 'intplan', 'ommin', 'omcall',
    'otmin', 'otcall', 'ngmin', 'ngcall', 'imin', 'icall', 'cuscall']]
X = pd.concat([X1, X2], axis=1)
X.head()
from sklearn.linear_model import LogisticRegression
logis = LogisticRegression()
logis.fit(X, y)

# Predictive scores #
score = logis.predict_proba(X)[:, 1]

# Confusion matrices #
conf1 = pd.crosstab(score > 0.5, churn['churn'] == 1)
conf1
conf2 = pd.crosstab(score > 0.2, churn['churn'] == 1)
conf2

# Cost-benefit analysis #
benefit1 = 80*conf1.iloc[1,1] - 20*conf1.iloc[1,0]
benefit1
benefit2 = 80*conf2.iloc[1,1] - 20*conf2.iloc[1,0]
benefit2

# Benefit function #
def benefit(cutoff):
    conf = pd.crosstab(score > cutoff, churn['churn'] == 1)
    benefit = 80*conf.iloc[1,1] - 20*conf.iloc[1,0]
    return benefit
benefit(0.2)

# Optimization #
from scipy.optimize import minimize_scalar
def f(x):
    return -benefit(x)
minimize_scalar(f, bounds=(0, 1), method='bounded')

# Graphical solution #
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.1, 0.9, 90)
benefit = np.vectorize(benefit)
y = benefit(x)
plt.figure(figsize=(6,6))
plt.plot(x, y)
plt.show()
