#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:52:48 2020

@author: balajiponnambalam
"""

#Data preprocessing
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

#Taking care of missing data

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = 'NaN', strategy = 'mean')
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

missingvalues = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose = 0)



missingvalues = missingvalues.fit(x[:, 1:3])



x[:, 1:3]=missingvalues.transform(x[:, 1:3])

