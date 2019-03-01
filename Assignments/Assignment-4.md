### Assignment 4

#### Introduction

This assignment is based on the example **The spam filter**. The objective is to explore a simple approach to the **validation** of a predictive model.

The objective of the validation is to dismiss the concerns about **overfitting** that are raised by the use of complex machine learning models. Broadly speaking, validation consists in checking that the model being validated works as expected on data which have not been used to develop it.

In the simplest approach to validation, we develop the model in a **training set**, trying it on a **test set**. The training and test sets can be predefined (e.g. training with first ten months of the year and testing with the last two months) or can be obtained from a **random split** of a unique data set.

#### Tasks

1. Develop and validate a spam classifier based on a **logistic regression model** using a 50-50 split. In Python, a random selection of one half of the rows of a data set `df` with `N` rows can be done with
`train = np.random.choice(range(0, N), n, replace=False)`.
Then, the training set would be `df.iloc[train, :]` and the test set would be `df.drop(train)`.

2. The same for classifier based on a **decision tree** with a low value of the parameter `min_impurity_decrease`.

#### Submission

Submit either a `.py` document with your code and short comments, or a full report in a Jupyter notebook, integrating the code, the Python output and your comments.

#### Deadline

February 27 (Wednesday), 24:00.
