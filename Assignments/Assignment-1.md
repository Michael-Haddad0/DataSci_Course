### Assignment 1

#### Introduction

This assignment is based on the example **House sales in King County**. This example develops a linear regression model for predicting housing prices.

#### Tasks

1. Transformations, such the square root or the logarithm, are recommended in Statistics textbooks in many situations. In particular, the **log transformation** is recommended for variables with skewed distributions, to limit the influence of extreme values. In this case, the transformation can be performed applying the Numpy function `log` to the price (i.e. `np.log(king['price'])`). Develop a model for predicting the price which is based on a linear regression equation that has the logarithm of the price on the left side. Do you get better predictions with this model?

2. It can be argued that having a model based on a linear equation does not make sense on such a wide range of prices. Indeed, in order to cope with the expensive houses, we are spoiling the prediction for some of the nonexpensive houses. So, we could **trim the data set**, dropping the houses beyond a certain threshold of price and/or size. For instance, you can restrict the analysis to the houses whose price falls between 100,000 and 1 million dollars. Is this useful? Have you better ideas?

#### Submission

Submit a `.py` document with your name on top, the Python code and some short comments to clarify. 

#### Deadline

February 5 (Tuesday), 24:00.
