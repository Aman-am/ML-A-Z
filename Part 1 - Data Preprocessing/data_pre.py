# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:48:41 2019

@author: smsak
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import DataSet
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values


#Handle missing data altogether 
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

#from sklearn.impute import SimpleImputer
#imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose =0 )
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print("hello world!")

#Handling missing data individually
dataset$Age = ifelse(is,na(dataset$Age),
                     ave(dataset$Age, FUN = funtion(x) mean(x, na.rm = TRUE)),
                     dataset$Age)