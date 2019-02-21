## Assignment 3 ##

# Importing the data#
import pandas as pd
spam = pd.read_csv('https://raw.githubusercontent.com/iese-bad/' +
    'DataSci/master/Data/spam.csv')

# Logistic regression model (1) #
y = spam.iloc[:, 51]
X1 = spam.iloc[:, 0:51]
from sklearn.linear_model import LogisticRegression
logis = LogisticRegression()
logis.fit(X1, y)
score1 = logis.predict_proba(X1)[:, 1]
conf1 = pd.crosstab(score1 > 0.5, spam['spam'] == 1)
conf1
tp1 = conf1.iloc[1, 1]/(conf1.iloc[0, 1] + conf1.iloc[1, 1])
tp1.round(3)
fp1 = conf1.iloc[1, 0]/(conf1.iloc[0, 0] + conf1.iloc[1, 0])
fp1.round(3)

# Binarization #
X2 = spam.iloc[:, 0:48] > 0
# X2 = X2.astype('int')

# Logistic regression model (2) #
logis.fit(X2, y)
score2 = logis.predict_proba(X2)[:, 1]
conf2 = pd.crosstab(score2 > 0.5, spam['spam'] == 1)
conf2
tp2 = conf2.iloc[1, 1]/(conf2.iloc[0, 1] + conf2.iloc[1, 1])
tp2.round(3)
fp2 = conf2.iloc[1, 0]/(conf2.iloc[0, 0] + conf2.iloc[1, 0])
fp2.round(3)

# Decision tree #
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor(min_impurity_decrease=0.001)
tree.fit(X2, y)
score3 = tree.predict(X2)
conf3 = pd.crosstab(score3 > 0.5, spam['spam']==1)
conf3
tp3 = conf3.iloc[1, 1]/(conf3.iloc[0, 1] + conf3.iloc[1, 1])
tp3.round(3)
fp3 = conf3.iloc[1, 0]/(conf3.iloc[0, 0] + conf3.iloc[1, 0])
fp3.round(3)
