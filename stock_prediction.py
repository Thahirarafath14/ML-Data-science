# -*- coding: utf-8 -*-
"""Stock-Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bspJOnuK9iMW1DuHvCQ4aUzB-n-hzIwK
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#eda
#model building
#linear
#dt
#rf
#svm
#ridge
#lasso

df = pd.read_csv('/content/NFLX (2).csv')
df

df.info()

df.head()

df.tail()

df.columns = df.columns.str.lower()

df[['year', 'month','day']] = df['date'].apply(lambda x: pd.Series(map(int, x.split('-'))))

df.drop(['date'], axis = 1,inplace = True)

df

df.info()

df.isnull().sum().any()

for col in df.columns:
    if df[col].dtype != 'object':
        sns.boxplot(x=col, data=df)
        plt.show()

df.hist(figsize=(15,9),bins =50)
plt.show()

sns.heatmap(df.corr(),annot = True)

#split the data
x = df.drop(columns = ['adj close'])
y = df['adj close']

x

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

x_train,x_test,y_train,y_test = train_test_split (x,y, test_size = 0.20,random_state= 42)

#linear
lr = LinearRegression()
lr.fit(x_train,y_train)
lr_pred = lr.predict(x_test)
lr_r2 = r2_score(y_test,lr_pred)

lr_r2

dt = DecisionTreeRegressor()
dt.fit(x_train, y_train)
dt_pred = dt.predict(x_test)
dt_r2 = r2_score(y_test,dt_pred)

dt_r2

rf = RandomForestRegressor()
rf.fit(x_train, y_train)
rf_pred = rf.predict(x_test)
rf_r2 = r2_score(y_test,rf_pred)

rf_r2

svr = SVR()
svr.fit(x_train, y_train)
svr_pred = svr.predict(x_test)
svr_r2 = r2_score(svr_pred,y_test)

svr_r2

#param grid ----'epsilon --- 0.1,0.2,0.3kernel ---linear,rbf
ridge = Ridge()
ridge.fit(x_train, y_train)
ridge_pred = ridge.predict(x_test)
ridge_r2 = r2_score(ridge_pred,y_test)

ridge_r2

#lasso
lasso = Lasso(alpha=0.1)
lasso.fit(x_train, y_train)
lasso_pred = lasso.predict(x_test)
lasso_r2 = r2_score(lasso_pred,y_test)

lasso_r2

