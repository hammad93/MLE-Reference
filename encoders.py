# In this exercise we'll load the iris dataset from sklearn,
# Then we'll perform one-hot encoding on the target names.


#
# In this and the following exercises, you'll be adding train test splits to the data
# to see how it changes the performance of each classifier
#
# The code provided will load the Titanic dataset like you did in project 0, then train
# a decision tree (the method you used in your project) and a Bayesian classifier (as
# discussed in the introduction videos). You don't need to worry about how these work for
# now. 
#
# What you do need to do is import a train/test split, train the classifiers on the
# training data, and store the resulting accuracy scores in the dictionary provided.

import numpy as np
import pandas as pd

# Load the dataset
X = pd.read_csv('titanic_data.csv')
# Limit to categorical data
X = X.select_dtypes(include=[object])

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# TODO: create a LabelEncoder object and fit it to each feature in X.
# The label encoder only takes a single feature at a time!
'''
Hammad Usmani
1) We first create our encoder
2) Next, we use the `fit_transform` function in the encoder and `apply` the function to all X
    -We use `apply` because the Label Encoder only takes in one vector. `apply` performs the function one column at a time
3) `fit_transform` gives us the result that we store for further processing
'''

le = LabelEncoder()
X = X.apply(le.fit_transform)

# TODO: create a OneHotEncoder object, and fit it to all of X.
'''
1) We create our encoder
2) The `OneHotEncoder` is different because it can take in more than one vector, but it needs to be in the correct type
3) We use `as_matrix()` to get our dataframe into the right format and pass it into `fit_transform` which returns an encoded array
4) We store what the output from our encoder
'''

enc = OneHotEncoder()
X = enc.fit_transform(X.as_matrix())

#TODO: transform the categorical titanic data, and store the transformed labels in the variable `onehotlabels`
'''
-The labels are within our stored parameter `X` after applying `LabelEncoder` to its columns and fitting it into `OneHotEncoder`
'''
onehotlabels = X 