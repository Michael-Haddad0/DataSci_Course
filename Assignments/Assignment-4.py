## Assignment 4 ##

# Importing the data#
import pandas as pd
spam = pd.read_csv('https://raw.githubusercontent.com/iese-bad/' +
    'DataSci/master/Data/spam.csv')
N = spam.shape[0]

# Random split #
import math
n = math.floor(N/2)
import numpy as np
train = np.random.choice(range(0, N), n, replace=False)

# General setting #
y = spam.iloc[:, 51]
X = spam.iloc[:, 0:51]
y1 = y.iloc[train]
y2 = y.drop(train)
X1 = X.iloc[train, :]
X2 = X.drop(train)

# Logistic regression model (train) #
from sklearn.linear_model import LogisticRegression
logis = LogisticRegression()
logis.fit(X1, y1)
lscore1 = logis.predict_proba(X1)[:, 1]
lconf1 = pd.crosstab(lscore1 > 0.5, y1 == 1)
ltp1 = lconf1.iloc[1, 1]/(lconf1.iloc[0, 1] + lconf1.iloc[1, 1])
ltp1.round(3)
lfp1 = lconf1.iloc[1, 0]/(lconf1.iloc[0, 0] + lconf1.iloc[1, 0])
lfp1.round(3)

# Logistic regression model (test) #
lscore2 = logis.predict_proba(X2)[:, 1]
lconf2 = pd.crosstab(lscore2 > 0.5, y2 == 1)
ltp2 = lconf2.iloc[1, 1]/(lconf2.iloc[0, 1] + lconf2.iloc[1, 1])
ltp2.round(3)
lfp2 = lconf2.iloc[1, 0]/(lconf2.iloc[0, 0] + lconf2.iloc[1, 0])
lfp2.round(3)

# Decision tree (train) #
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor(min_impurity_decrease=0.001)
tree.fit(X1, y1)
tscore1 = tree.predict(X1)
tconf1 = pd.crosstab(tscore1 > 0.5, y1==1)
ttp1 = conf3.iloc[1, 1]/(tconf1.iloc[0, 1] + tconf1.iloc[1, 1])
ttp1.round(3)
tfp1 = tconf1.iloc[1, 0]/(tconf1.iloc[0, 0] + tconf1.iloc[1, 0])
tfp1.round(3)

# Decision tree (test) #
tscore2 = tree.predict(X2)
tconf2 = pd.crosstab(tscore2 > 0.5, y2==1)
ttp2 = tconf2.iloc[1, 1]/(tconf2.iloc[0, 1] + tconf2.iloc[1, 1])
ttp2.round(3)
tfp2 = tconf2.iloc[1, 0]/(tconf2.iloc[0, 0] + tconf2.iloc[1, 0])
tfp2.round(3)
