"""@author: Tanzim"""
# Cross Validation Regression MAE
import pandas as pd
filename = "PUT THE .csv file"
colnames = ['Column names in quotes seperated by comma']
dataset = pd.read_csv(filename, names=colnames).values
# separate array into input and output components
X = dataset[:,0:8] # rows:columns
Y = dataset[:,8]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
kfold = KFold(n_splits=10, random_state=0)
results = cross_val_score(model, X, Y, cv=kfold, scoring='neg_mean_absolute_error')
print("MAE: %.3f (%.3f)" % (results.mean(), results.std()))